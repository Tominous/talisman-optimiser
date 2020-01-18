from skypy_constants import *
import re

# API Calls
import requests, json
from datetime import datetime
# --------

# Inventory parsing
from base64 import b64decode as one
from gzip import decompress as two
from io import BytesIO as three
from struct import unpack


# -----------------

class SkyblockError(Exception):
    """A general exception from the skyblock library"""


class NeverPlayedSkyblockError(SkyblockError):
    """This user has never played skyblock before!"""


class APIDisabledError(SkyblockError):
    """This profile has disabled their API settings!"""


def decode_inventory_data(raw):
    """Takes a raw string representing inventory data.
    Returns a json object with the inventory's contents"""

    raw = three(two(one(raw)))  # Unzip raw string from the api

    def read(type, length):
        if type in 'chill':
            return int.from_bytes(raw.read(length), byteorder='big')
        if type == 's':
            return raw.read(length).decode('utf-8')
        return unpack('>' + type, raw.read(length))[0]

    def parse_list():
        subtype = read('c', 1)
        payload = []
        for _ in range(read('i', 4)):
            parse_next_tag(payload, subtype)
        return payload

    def parse_compound():
        payload = {}
        while parse_next_tag(payload) != 0:  # Parse tags until we find an endcap (type == 0)
            pass  # Nothing needs to happen here
        return payload

    payloads = {
        1: lambda: read('c', 1),  # Byte
        2: lambda: read('h', 2),  # Short
        3: lambda: read('i', 4),  # Int
        4: lambda: read('l', 8),  # Long
        5: lambda: read('f', 4),  # Float
        6: lambda: read('d', 8),  # Double
        7: lambda: raw.read(read('i', 4)),  # Byte Array
        8: lambda: read('s', read('h', 2)),  # String
        9: parse_list,  # List
        10: parse_compound,  # Compound
        11: lambda: [read('i', 4) for _ in range(read('i', 4))],  # Int Array
        12: lambda: [read('l', 8) for _ in range(read('i', 4))]  # Long Array
    }

    def parse_next_tag(dictionary, tag_id=None):
        if tag_id is None:  # Are we inside a list?
            tag_id = read('c', 1)
            if tag_id == 0:  # Is this the end of a compound?
                return 0
            name = read('s', read('h', 2))

        payload = payloads[tag_id]()
        if isinstance(dictionary, dict):
            dictionary[name] = payload
        else:
            dictionary.append(payload)

    raw.read(3)  # Remove file header (we ingore footer)
    root = {}
    parse_next_tag(root)
    return [Item(x, i) for i, x in enumerate(root['i']) if x]


class Item:
    def __init__(self, nbt, slot_number):
        self.__nbt__ = nbt

        self.slot_number = slot_number
        self.internal_name = self['tag']['ExtraAttributes'].get('id', None)
        self.description = self['tag']['display'].get('Lore', None)
        
        try:
            self.enchantments = self['tag']['ExtraAttributes']['enchantments']
        except KeyError:
            self.enchantments = {}
        
        if self.description:
            for i, txt in enumerate(self.description):
                self.description[i] = re.sub('§.', '', txt)

            rarity_type = self.description[-1].split()
            self.rarity = rarity_type[0].lower()
            self.type = rarity_type[1].lower() if len(rarity_type) > 1 else None
            for type, list in {'sword': sword_enchants, 'bow': bow_enchants, 'fishing rod': rod_enchants}.items():
                for e in list:
                    if e in self.enchantments:
                        self.type = type
                        break
        else:
            self.rarity = None
            self.type = None

        self.name = re.sub('§.', '', self['tag']['display']['Name'])

    def __getitem__(self, name):
        return self.__nbt__[name]

    def __str__(self):
        return self['tag']['display']['Name']

    def __repr__(self):
        return self['tag']['display']['Name']

    def rarity_level(self):
        return ['common', 'uncommon', 'rare', 'epic', 'legendary', 'special'].index(self.rarity)

    def reforge(self):
        try:
            return self['tag']['ExtraAttributes']['modifier']
        except KeyError:
            return None

    # Why do we have to sift the lorestring for this?
    # Can't it just be in the nbt data?
    def stats(self, use_reforge=True):
        results = {}
        # §7Attack Speed: §c+2% §8(Itchy +2%)
        # §7Intelligence: §a+9 §c(Godly +3)
        reg = re.compile(
            '(Damage|'
            'Strength|'
            'Crit Chance|'
            'Crit Damage|'
            'Attack Speed|'
            'Health|'
            'Defense|'
            'Speed|'
            'Intelligence)'
            ': \+(\d+).*'
        )
        for line in self.description:
            match = reg.match(line)
            if match:
                results[match[1].lower()] = int(match[2])

        name = self.internal_name

        def add(stat, amount):
            results[stat] = results.get(stat, 0) + amount

        if name == 'RECLUSE_FANG':
            add('strength', 370)
        elif name == 'SHREDDER':
            add('damage', 115)
            add('strength', 15)
        elif name == 'NIGHT_CRYSTAL' or name == 'DAY_CRYSTAL':
            add('strength', 2.5)
            add('defense', 2.5)
        elif name == 'CAKE_BAG':
            print(self.__nbt__)
             add('health', len(decode_inventory_data(self[][][])))
            pass
        elif name == 'GRAVITY_TALISMAN':
            add('strength', 10)
            add('defense', 10)

        if use_reforge is False:
            reforge = self.reforge()
            if reforge:
                for stat, amount in reforges[self.reforge()][self.rarity_level()].items():
                    if stat in results:
                        results[stat] -= amount
        return results


def damage(weapon_dmg, strength, crit_dmg, ench_modifier):
    return (5 + weapon_dmg + strength // 5) * (1 + strength / 100) * (1 + crit_dmg / 100) * ench_modifier


def get_uuid(uname):
    try:
        req = requests.get('https://api.mojang.com/users/profiles/minecraft/' + uname).content
        return json.loads(req)['id']
    except (KeyError, json.JSONDecodeError):
        raise SkyblockError('Invalid uname!') from None


def get_uname(uuid):
    try:
        req = requests.get('https://api.mojang.com/user/profiles/' + uuid + '/names').content
        return json.loads(req)[-1]['name']
    except (KeyError, json.JSONDecodeError):
        raise SkyblockError('Invalid uuid!') from None


class Player:
    """A class representing a Skyblock player.
    Instantiate the class with Player(api_key, username) or Player(api_key, uuid)
    Use profiles() and set_profile() to retrieve and define all the profile data.
    Use weapons() and set_weapon() to retrieve and set the player's weapon."""

    def __init__(self, key, uname=None, uuid=None):
        self.api_key = key
        if uname and uuid:
            self.uname = uname
            self.uuid = uuid
        elif uname:
            self.uname = uname
            self.uuid = get_uuid(uname)
        elif uuid:
            self.uuid = uuid
            self.uname = get_uname(uuid)
        else:
            raise SkyblockError('You need to provide either a minecraft username or uuid!')

        try:
            self.profiles = {}
            player = self.__call_api__('/player?uuid=' + self.uuid)
            profile_ids = player['player']['stats']['SkyBlock']['profiles']

            for k, v in profile_ids.items():
                self.profiles[v['cute_name']] = k
        except (KeyError, TypeError):
            raise NeverPlayedSkyblockError from None
        if not self.profiles:
            raise NeverPlayedSkyblockError

    def __call_api__(self, endpoint):
        base_url = 'https://api.hypixel.net'

        # build endpoint url
        endpoint_url = base_url

        if '?' in endpoint:
            endpoint_url += endpoint + '&key=' + self.api_key
        else:
            endpoint_url += endpoint + '?key=' + self.api_key

        # send request
        resp = requests.get(endpoint_url).content
        resp = json.loads(resp)

        # check if invalid api key
        if not resp['success'] and resp['cause'] == 'Invalid API key!':
            raise SkyblockError('Invalid API key!')

        return resp

    def set_profile(self, profile):
        """Sets a player's profile based on the provided profile id. Also retrieves all api data for that profile."""
        self.profile = profile

        try:
            self.__api_data__ = self.__call_api__('/skyblock/profile?profile=' + self.profile)['profile']['members'][
                self.uuid]
            v = self.__api_data__

            def parse_collections(data):
                try:
                    tuples = []
                    for s in v[data]:
                        temp = re.split('_(?!.*_)', s, maxsplit=1)
                        temp[1] = int(temp[1])
                        tuples.append(temp)
                    dictionary = {}
                    for s in set(name for name, level in tuples):
                        max = 0
                        for name, level in tuples:
                            if name == s and level > max:
                                max = level
                        dictionary[s.lower().replace('_', ' ')] = max
                    return dictionary
                except KeyError:
                    return {}

            self.collections = {name.lower().replace('_', ' '): level for name, level in v['collection'].items()}
            self.unlocked_collections = parse_collections('unlocked_coll_tiers')
            self.minons = parse_collections('crafted_generators')

            self.inventory = decode_inventory_data(v['inv_contents']['data'])
            self.echest = decode_inventory_data(v['ender_chest_contents']['data'])
            self.armor = decode_inventory_data(v['inv_armor']['data'])
            self.weapons = [item for item in self.inventory + self.echest if
                            item.type in ('sword', 'bow', 'fishing rod')]

            def optional_inv(*path):
                try:
                    result = v
                    for key in path:
                        result = result[key]
                    return decode_inventory_data(result)
                except KeyError:
                    return []

            self.candy_bag = optional_inv('candy_inventory_contents', ' data')
            self.talisman_bag = optional_inv('talisman_bag', 'data')
            self.potion_bag = optional_inv('potion_bag', 'data')
            self.fish_bag = optional_inv('fishing_bag', 'data')
            self.quiver = optional_inv('quiver', 'data')

            self.active_talismen = []
            active_talismen_names = []
            talisman_names = [x.internal_name for x in self.inventory + self.talisman_bag]
            for tali in self.inventory + self.talisman_bag:
                if tali.type == 'accessory':
                    add = True
                    if tali.internal_name in active_talismen_names:
                        add = False
                    else:
                        for familiy in tiered_talismen:
                            if add is False:
                                break
                            if tali.internal_name in familiy[:-1]:
                                for older_brother in familiy[familiy.index(tali.internal_name) + 1:]:
                                    if older_brother in talisman_names:
                                        add = False
                                        break
                    if add:
                        self.active_talismen.append(tali)
                        active_talismen_names.append(tali.internal_name)

            self.join_date = datetime.fromtimestamp(v['first_join'] / 1000.0)
            self.fairy_souls_collected = v.get('fairy_souls_collected', 0)
            self.purse = float(v.get('coin_purse', 0))

            self.kills = int(v['stats']['kills'])
            self.specifc_kills = {name.replace('kills_', '').replace('_', ' '): int(amount)
                                  for name, amount in v['stats'].items() if re.match('kills_', name)}
            self.deaths = int(v['stats']['deaths'])
            self.specifc_deaths = {name.replace('deaths_', '').replace('_', ' '): int(amount)
                                   for name, amount in v['stats'].items() if re.match('deaths_', name)}

            def parse_skill(skill):
                try:
                    return int(v['experience_skill_' + skill])
                except KeyError:
                    return 0

            self.skill_experience = {
                name: parse_skill(name)
                for name in ['farming', 'mining', 'foraging', 'combat', 'enchanting', 'alchemy', 'fishing', 'carpentry',
                             'runecrafting']
            }

            def parse_exp(exp, runecrafting=False):
                if exp == 0:
                    return 0
                for lvl, requirement in enumerate(
                        runecrafting_exp_requirements if runecrafting else skill_exp_requirements):
                    if exp > requirement:
                        exp -= requirement
                    else:
                        break
                return lvl

            self.skills = {
                name: parse_exp(parse_skill(name), name == 'runecrafting')
                for name in ['farming', 'mining', 'foraging', 'combat', 'enchanting', 'alchemy', 'fishing', 'carpentry',
                             'runecrafting']
            }

            def parse_slayer_api(name):
                try:
                    return int(list(v['slayer_bosses'][name]['claimed_levels'].keys())[-1].replace('level_', ''))
                except IndexError:
                    return 0

            self.slayer_levels = {
                'zombie': parse_slayer_api('zombie'),
                'spider': parse_slayer_api('spider'),
                'wolf': parse_slayer_api('wolf')
            }
        except KeyError as k:
            raise APIDisabledError(k)

    def is_player_online(self):
        player_data = self.__call_api__('/player?name=' + self.uname)['player']
        return player_data['lastLogout'] < player_data['lastLogin']

    def base_stats(self):
        return {'damage': 0, 'strength': 0, 'crit chance': 20, 'crit damage': 50, 'attack speed': 100, 'health': 100,
                'defense': 0,
                'speed': 100, 'intelligence': 0}

    def fairy_soul_stats(self):
        hp = 0
        num_souls = self.fairy_souls_collected
        for i, amount in enumerate(fairy_soul_hp_bonus):
            if i * 5 + 5 > num_souls:
                break
            hp += amount
        return {
            'health': hp,
            'defense': num_souls // 5 + num_souls // 25,
            'strength': num_souls // 5 + num_souls // 25,
            'speed': num_souls // 50
        }

    def slayer_stats(self):
        stats = {}
        for rewards, level in zip(list(slayer_rewards.values()), list(self.slayer_levels.values())):
            for i, (reward, amount) in enumerate(rewards):
                if level > i and reward:
                    stats[reward] = stats.get(reward, 0) + amount
        return stats

    def skill_stats(self):
        return {
            'crit chance': self.skills['combat'],
            'strength': self.skills['foraging'] + min(0, self.skills['foraging'] - 15)
        }

    def talisman_stats(self, include_reforges=True):
        stats = {}
        names = [tali.internal_name for tali in self.active_talismen]
        for i in self.active_talismen:
            for stat, amount in i.stats(include_reforges).items():
                stats[stat] = stats.get(stat, 0) + amount
        return stats

    def armor_stats(self, include_reforges=True):
        stats = {}
        for armor in self.armor:
            for stat, amount in armor.stats().items():
                if 'ENDER' in armor.internal_name:
                    stats[stat] = stats.get(stat, 0) + amount * 2
                else:
                    stats[stat] = stats.get(stat, 0) + amount
        return stats

    def stat_modifiers(self):
        modifers = {}

        def add_modifier(name, mod):
            if name in modifers:
                if name == 'crit damage':
                    modifers[name] = lambda stat, strength: mod(modifers[name](stat, strength))
                else:
                    modifers[name] = lambda stat: mod(modifers[name](stat))
            else:
                modifers[name] = mod

        helmet = next((piece for piece in self.armor if piece.type == 'helmet'), None)
        tarantula_helmet = helmet and helmet.internal_name == 'TARANTULA_HELMET'
        superior = 0
        mastiff = 0
        for i in self.armor:
            if 'SUPERIOR' in i.internal_name:
                superior += 1
            elif 'MASTIFF' in i.internal_name:
                mastiff += 1
            else:
                break
        if superior == 4:
            for name in ['damage', 'strength', 'crit chance', 'attack speed', 'health', 'defense', 'speed',
                         'intelligence']:
                add_modifier(name, lambda stat: stat * 1.05)
            add_modifier('crit damage', lambda stat, strength: stat * 1.05)
        elif mastiff == 4:
            add_modifier('crit damage', lambda stat, strength: stat / 2)
        elif tarantula_helmet:
            add_modifier('crit damage', lambda stat, strength: stat + strength / 10)
        return modifers

    # Method is unfinished, only works for damage stats. feel free to send me a corrected version!
    def stats(self, weapon):
        """Returns a dictionary containing all the player's stats including their weapon's stats."""
        stats = self.base_stats()

        def apply_stats(additional):
            for key, value in additional.items():
                stats[key] += value

        apply_stats(self.fairy_soul_stats())
        apply_stats(self.slayer_stats())
        apply_stats(self.cake_stats())
        apply_stats(self.skill_stats())
        apply_stats(self.talisman_stats(include_reforges=True))
        apply_stats(weapon.stats())

        stats = self.armor_modifiers(stats)

        return stats

    def talisman_counts(self):
        counts = {'common': 0, 'uncommon': 0, 'rare': 0, 'epic': 0, 'legendary': 0}
        for tali in self.active_talismen:
            counts[tali.rarity] += 1
        return counts

    def auctions(self):
        resp = self.__call_api__('/skyblock/auction?uuid=' + self.uuid + '&profile=' + self.profile)

        player_auctions = []
        for i in range(len(resp['auctions'])):
            curr_auction = resp['auctions'][i]

        if not curr_auction['claimed']:
            player_auctions.append(
                {
                    'item_name': curr_auction['item_name'], 'starting_bid': curr_auction['starting_bid'],
                    'highest_bid': curr_auction['highest_bid_amount'],
                    'highest_bidder': curr_auction['claimed_bidders'] if len(
                        curr_auction['claimed_bidders']) > 0 else None,
                    'end': curr_auction['end']
                })

    def dump_all_player_data(self):
        return self.__call_api__('/skyblock/profile?profile=' + self.profile)['profile']['members']
