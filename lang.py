# note to translators: if you want to use the symbol % in your translation, please add another % afterward to make %% or it will bug

english = {
    'yes': 'yes',
    'no': 'no',
    'primer': 'Before you start:',
    'rule1': 'Put the armour on that you will optimise with',
    'rule2': 'Put all your talismen in your inventory or talisman bag',
    'rule3': 'Enable your skyblock API settings [skyblock menu > settings > api settings]',
    'rule4': 'Log out of Hypixel so that the API syncs',
    'welcome': 'Hi %s!\nWelcome to notnotmelon\'s talisman optimiser!',  # self.user.mention
    'username?': 'What is your minecraft username?',
    'unameaccept': 'Username accepted',
    'neverplayedsb': 'You have never played skyblock! Try again',
    'invaliduname': 'Invalid username! Try again',
    'profile?': 'Which profile do you want to use?',
    'sortbydate': '(Sorted by date created)',
    'apidisabled': 'Your API settings are (probably) disabled!',
    'reenable': 'Re-enable them with [skyblock menu > settings > api settings]',
    'thisappearsif': 'Sometimes this message appears even if your API settings are enabled. If so, exit Hypixel and try again. It\'s also possible that Hypixel\'s API servers are down.',
    'chooselisted': 'Choose one of the listed profiles',
    'unnecessary': 'You have unnecessary talismen!',
    'noweapon': 'You are not carrying any weapons!\nPlace one in your inventory and try again',
    'weapon?': 'Which weapon do you want to use?',
    'usenameornumber': 'Enter the weapon name or the weapon number',
    'profileaccepted': 'Profile accepted!',
    'correctequip?': 'Is this the correct equipment? [YES/NO]',
    'ansy/n': 'Please answer with YES or NO',
    'potion?': 'Do you use %s pots with this build? [YES/NO]',  # potion_name
    'potionlvl?': 'Which level of %s potions do you use?',  # damaging_potions[self.potion_id]["name"]
    'enternumb': 'Invalid response! Enter a number',
    'critgoal?': '''You indicated that you don\'t want to use crit pots
Do you want to have 80 crit chance anyway? [YES/NO]''',
    'overflux': 'I detected an overflux orb. Should I include that in the calculations? [YES/NO]',
    'manaflux': 'I detected a mana flux orb. Should I include that in the calculations? [YES/NO]',
    'tuba': 'I detected a weird tuba. Should I include that in the calculations? [YES/NO]',
    'target?': 'Which mob will you target with this setup?',
    'pickactivities': 'Invalid response! Pick one of the activities',
    'algstarted': 'Please wait. Your results will be sent shortly...',
    'finished': 'Calculations complete!',
    'disclaimer': '''Damage multipliers from weapons such as
scorpion foil or reaper falchion are not included.
Talisman results should still be correct.''',
    'shoulddeal': 'This setup should deal %s damage',  # round(damage)
    'withoutcrit': '> %s without crit',  # round(non_crit)
    'noroute': '''It\'s impossible for you to reach 100%% crit chance.
Level up your combat and get more talismans before trying the optimiser again.''',
    'currsetup': 'Current Setup'
}

spanish = {
    'yes': 'si',
    'no': 'no',
    'primer': 'Antes de empezar:',
    'rule1': 'Coloca la armadura con la que optimizaras:',
    'rule2': 'Coloca todos tus talismanes en tu inventario o en la bolsa de talismanes',
    'rule3': 'Activa tu configuración de API [Menu de Skyblock > Configuración > Configuración de API]',
    'rule4': 'Reconectate a Hypixel para que la API se sincronice',
    'welcome': '''Hola %s!
Bienvenido al optimizador de talismanes de notnotmelon!''',
    'username?': '¿Cual es tu nombre de usuario en Minecraft?',
    'unameaccept': 'Nombre de usuario aceptado',
    'neverplayedsb': 'Nunca has jugado skyblock! Intenta de nuevo',
    'invaliduname': 'Nombre de jugador invalido! Intenta de nuevo',
    'profile?': '¿Qué perfil te gustaria usar?',
    'sortbydate': '(Ordenado por la fecha de creación)',
    'apidisabled': 'Tu configuracion API esta (probablemente) deshabilitada!',
    'reenable': 'Reactivala con [Menu de Skyblock > Configuración > Configuración de API]',
    'thisappearsif': 'A veces este mensaje aparece cuando la configuración de API ya esta activada. Si es asi, sal de Hypixel',
    'chooselisted': 'Coloca uno de los perfiles de la lista',
    'unnecessary': 'Tienes talismanes innecesarios!',
    'noweapon': '''No tienes ningun arma!
Coloca una en tu inventario e intenta de nuevo''',
    'weapon?': '¿Qué arma te  gustaria usar?',
    'usenameornumber': 'Escribe el nombre del arma o el numero de ella',
    'profileaccepted': 'Perfil aceptado!',
    'correctequip?': '¿Este es el equipamiento correcto? [SI/NO]',
    'ansy/n': 'Por favor responde con SI o NO',
    'potion?': 'Usaras alguna pocion de %s en esta configuración? [SI/NO]',
    'potionlvl?': '¿Que nivel de pocion de %s usaras?',
    'enternumb': 'Respuesta invalida! Introduce un numero',
    'critgoal?': 'Has inidado que no quieres usar pociones de critico. De igual manera te gustaria tener 80%% de oportunidad de critico? [SI/NO]',
    'overflux': 'He detectado un overflux orb. Debo incluirla en el calculo? [SI/NO]',
    'manaflux': 'He detectado un mana flux orb. Debo incluirla en el calculo? [SI/NO]',
    'tuba': 'He detectado un weird tuba. Debo incluirla en el calculo? [SI/NO]',
    'target?': '¿Que enemigo quieres matar con esta configuración?',
    'pickactivities': 'Respuesta invalida! Selecciona uno de la lista',
    'algstarted': 'Por favor espera, tus resultados se enviaran en breve...',
    'finished': 'Sesión terminada!',
    'disclaimer': '''Multiplicadores de daño como
el Scorpion Foil o la Reaper Falchion no estan incluidos
Los resultados deberian ser correctos.''',
    'shoulddeal': 'Esta configuracion deberia hacer %s de daño',
    'withoutcrit': '> %s Daño sin critico'
}

german = {
    'yes': 'ja',
    'no': 'nein',
    'primer': 'Bevor du startest:',
    'rule1': 'Ziehe die Rüstung an, mit der du deine Talismane optimieren möchtest',
    'rule2': 'Lege alle Talismane in dein Inventar oder in den Talisman Bag',
    'rule3': 'Aktiviere deine Skyblock API Einstellungen [skyblock menu > settings > api settings]',
    'rule4': 'Melde dich von Hypixel ab, damit die API synchronisiert wird',
    'welcome': 'Hi %s!\nWillkommen zu notnotmelons Talisman Optimizer!',  # self.user.mention
    'username?': 'Was ist dein Minecraft Nutzername?',
    'unameaccept': 'Nutzername akzeptiert',
    'neverplayedsb': 'Du hast noch nie Skyblock gespielt. Versuche es noch einmal',
    'invaliduname': 'Ungültiger Nutzername! Versuche es noch einmal',
    'profile?': 'Welches Profil möchtest du verwenden?',
    'sortbydate': '(Sortiert nach Erstellungsdatum)',
    'apidisabled': 'Deine API Einstellung ist (warscheinlich) deaktiviert!',
    'reenable': 'Aktivieren Sie sie erneut [skyblock menu > settings > api settings]',
    'thisappearsif': 'Manchmal erscheint diese Nachricht, auch wenn du deine API Einstellung aktiviert hast. Wenn ja, Melde dich von Hypixel ab und versuche es noch einmal. Es ist auch möglich, dass Hypixels API Server ausgefallen sind.',
    'chooselisted': 'Wähle eines der aufgelisteten Profile',
    'unnecessary': 'Du hast nicht notwendige Talismane!',
    'noweapon': 'Du trägst keine Waffen!\nLege eins in dein Inventar und versuche es noch einmal',
    'weapon?': 'Welche Waffe möchtest du benutzen?',
    'usenameornumber': 'Gebe den Waffennamen oder die Waffennummer ein',
    'profileaccepted': 'Profil akzeptiert!',
    'correctequip?': 'Ist das die korrekte Ausrüstung? [JA/NEIN]',
    'ansy/n': 'Bitte antworte mit JA oder NEIN',
    'potion?': 'Benutzt du %s  Tränke mit dieser Ausrüstung? [JA/NEIN]',  # potion_name
    'potionlvl?': 'Welche Stufe von %s Tränken benutzt du?',  # damaging_potions[self.potion_id]["name"]
    'enternumb': 'Ungültige Antwort! Gebe eine Nummer ein',
    'critgoal?': '''Du hast angegeben, dass du Critical Tränke nicht verwenden möchtest.
Willst du die 80%% Crit Chance trotzdem haben? [JA/NEIN]''',
    'overflux': 'Ich habe einen Overflux orb gefunden. Soll ich den in die Berechnungen einbeziehen?? [JA/NEIN]',
    'manaflux': 'Ich habe einen Mana flux orb gefunden. Soll ich den in die Berechnungen einbeziehen?? [JA/NEIN]',
    'tuba': 'Ich habe eine Weird Tuba gefunden. Soll ich die in die Berechnungen einbeziehen?? [JA/NEIN]',
    'target?': 'Welchen Mob wirst du mit diesem Setup anvisieren?',
    'pickactivities': 'Ungültige Antwort! Wähle eine der Aktivitäten',
    'algstarted': 'Bitte warte. Deine Ergebnisse werden dir gleich gesendet...',
    'finished': 'Berechnungen abgeschlossen!',
    'disclaimer': '''Schadensmultiplikatoren von Waffen wie
Scorpion Foil oder Reaper Falchion sind nicht enthalten.
Talisman Ergebnisse sollten trotzdem korrekt sein.''',
    'shoulddeal': 'Dieses Setup sollte %s Schaden machen',  # round(damage)
    'withoutcrit': '> %s ohne crit'  # round(non_crit)
}

french = {
    'yes': 'oui',
    'no': 'non',
    'primer': 'Avant de commencer:',
    'rule1': 'Équiper votre armure avant de commencer',
    'rule2': 'Mettez tous vos talismans dans votre inventaire ou accessory bag',
    'rule3': 'Activer votre api skyblock [skyblock menu > settings > api settings]',
    'rule4': 'Déconnecter vous d\'hypixel et reconnecter vous pour synchroniser',
    'welcome': 'Salut %s!\nBienvenue sur notnotmelon\'s talisman optimizer!',  # self.user.mention
    'username?': 'Qu\'elle est votre pseudo Minecraft?',
    'unameaccept': 'Pseudo accepter',
    'neverplayedsb': 'Vous n\'avez jamais joué au skyblock! Réessayer',
    'invaliduname': 'Pseudo invalide! Réessayer',
    'profile?': 'Quel profil souhaitez-vous utiliser?',
    'sortbydate': '(Trié par date de création)',
    'apidisabled': 'Vos paramètres API sont (probablement) désactivés!',
    'reenable': 'Réactivez-les avec [skyblock menu > settings > api settings]',
    'thisappearsif': 'Parfois, ce message apparaît même si vos paramètres API sont activés. Si tel est le cas, quittez Hypixel et réessayez. Il est également possible que les serveurs API d\'Hypixel soient en panne.',
    'chooselisted': 'Choisissez l\'un des profils',
    'unnecessary': 'Vous avez des talismen inutiles!',
    'noweapon': 'Vous ne portez aucune arme!\nPlacez-en un dans votre inventaire et réessayez',
    'weapon?': 'Quelle arme voulez-vous utiliser?',
    'usenameornumber': 'Entrez le nom ou le numéro de l\'arme',
    'profileaccepted': 'Profil accepté!',
    'correctequip?': 'Est-ce le bon équipement? [OUI/NON]',
    'ansy/n': 'Veuillez répondre par OUI ou NON',
    'potion?': 'Utilisez-vous une potion de %s avec cette version? [OUI/NON]',  # potion_name
    'potionlvl?': 'Quel niveau de potion de %s utilisez-vous?',  # damaging_potions[self.potion_id]["name"]
    'enternumb': 'Réponse invalide! Entrez un nombre',
    'critgoal?': '''Vous avez indiqué que vous ne souhaitez pas utiliser les potions de critiques
Voulez-vous quand même avoir 80%% de chances de critique? [OUI/NON]''',
    'overflux': 'J\'ai détecté une overflux orb. Dois-je inclure cela dans les calculs? [OUI/NON]',
    'manaflux': 'J\'ai détecté une mana flux orb. Dois-je inclure cela dans les calculs? [OUI/NON]',
    'tuba': 'J\'ai détecté un weird tuba. Dois-je inclure cela dans les calculs? [OUI/NON]',
    'target?': 'Quelle monstre ciblerez-vous avec cette configuration?',
    'pickactivities': 'Réponse invalide! Choisissez l\'une des activités',
    'algstarted': 'S\'il vous plaît, attendez. Vos résultats seront envoyés sous peu...',
    'finished': 'Les calculs sont terminés!',
    'disclaimer': '''Multiplicateurs de dégâts des armes telles que
le scorpion foil ou la reaper falchion ne sont pas inclus.
Les résultats de Talisman devraient toujours être corrects.''',
    'shoulddeal': 'Cette configuration devrait infliger %s de dégâts',  # round(damage)
    'withoutcrit': '> %s Sans critiques'  # round(non_crit)
}

polish = {
    'yes': 'tak',
    'no': 'nie',
    'primer': 'Zanim zaczniesz:',
    'rule1': 'Załóż zbroję, z którą będziesz optymalizować',
    'rule2': 'Włóż wszystkie twoje akcesoria do ekwipunku oraz torby z akcesoriami',
    'rule3': 'Musisz mieć włączony Skyblock API [skyblock menu > settings > api settings]',
    'rule4': 'Wyjdź z serwera, aby zaaktualizować swój ekwipunek dla API',
    'welcome': '%s Hej, rozpoczynamy optymalizację! (moim właścicielem jest notnotmelon)',  # self.user.mention
    'username?': 'Jaki jest twój nick w Minecrafcie?',
    'unameaccept': 'Aha, znalałem!',
    'neverplayedsb': 'Hej hej, nie grałeś w Skyblocka na tym koncie! Spróbuj ponownie!',
    'invaliduname': 'Nie ma cię na liście graczy, spróbuj jeszcze raz',
    'profile?': 'Więc, jaki profil wybieramy?',
    'sortbydate': '(Sortuję według daty założenia)',
    'apidisabled': 'Uhh, API masz wyłączone. Chyba. Spróbuj ponownie?',
    'reenable': 'Włącz je ponownie z [skyblock menu > settings > api settings]',
    'thisappearsif': 'Czasem Hypixel potrafi się wykrzaczyć z serwerami API, więc trzeba brać to pod uwagę',
    'chooselisted': 'Wybierz profil z listy',
    'unnecessary': 'Masz niepotrzebne talizmany!',
    'noweapon': 'Nie masz przy sobie broni, włóż tę którą używasz do ekwipunku',
    'weapon?': 'Jaką broń używasz?',
    'usenameornumber': 'Wpisz nazwę, bądź numer',
    'profileaccepted': 'Zaakceptowano!',
    'correctequip?': 'Czy to właściwy ekwipunek?[TAK/NIE]',
    'ansy/n': 'przyjmuję tylko tak i nie',
    'potion?': 'Czu używasz %s potek z tym ekwipunkiem? [TAK/NIE]',  # potion_name
    'potionlvl?': 'Który poziom %s używasz?',  # damaging_potions[self.potion_id]["name"]
    'enternumb': 'zła odpowiedź! wprowadź liczbę',
    'critgoal?': '''Zaznaczyłeś że nie korzystasz z crit potions, czy chcesz mieć 80%% szans na krytyczne trafienie tak czy siak? W innym wypadku będziemy ciągnąć do 100% [TAK/NIE]''',
    'overflux': 'Wyczuwam overflux orb w twoim ekwipunku, dodać go do kalkulacji? [TAK/NIE]',
    'manaflux': 'Wyczuwam mana flux orb w twoim ekwipunku, dodać go do kalkulacji?  [TAK/NIE]',
    'tuba': 'Wyczuwam weird tuba w twoim ekwipunku. Dodać do kalkulacji? [TAK/NIE]',
    'target?': 'Twój cel do zabijania?',
    'pickactivities': 'Zła odpowiedź! Wybierz prawidłową aktywność',
    'algstarted': 'Teraz liczenie, poczekaj nieco... Im więcej talizmanów, tym więcej liczenia',
    'finished': 'Liczenie zakończone',
    'disclaimer': '''Kalkulator ignoruje bonusy typu +ileś% do obrażeń przeciw zombie ''',
    'shoulddeal': 'Powninieneś zadawać %s obrażeń',  # round(damage)
    'withoutcrit': '> %s bez krytyków',  # round(non_crit)
    'noroute': '''Nie masz szans aby zdobyć obecnie 100%% szansy na uderzenie krytyczne. Zwiększ liczbę talizmanów, jak i poziom walki i spróbuj ponownie'''
}

hebrew = {
    'yes': 'כן',
    'no': 'לא',
    'primer': 'לפני שאתה מתחיל:',
    'rule1': 'שים עליך את השריון שאתה רוצה להוציא את המיטב ממנו',
    'rule2': 'שים את כל הטליסמנים שלך באינבנטורי או בתיק האביזרים',
    'rule3': 'תפעיל את skyblock API settings [skyblock menu > settings > api settings]',
    'rule4': 'Log out of Hypixel so that the API syncs',
    'welcome': 'שלום %s!\nברוך הבא ל notnotmelon\'s talisman optimizer!',  # self.user.mention
    'username?': 'מה שמך במיינקראפט?',
    'unameaccept': 'שמך אושר',
    'neverplayedsb': 'אף פעם שיחקת בסקיי בלוק! נסה שוב',
    'invaliduname': 'שמך שגוי! נסה שוב',
    'profile?': 'באיזה פרופיל אתה רוצה להשתמש?',
    'sortbydate': '(ממוין לפי תאריך שנוצר)',
    'apidisabled': 'Your API settings (כנראה) לא מופעלים!',
    'reenable': 'תפעיל אותם שוב עם [skyblock menu > settings > api settings]',
    'thisappearsif': 'לפעמים הודעה זאת מופיעה גם כאשר API settings  פועלים. אם כך, תצא מהייפיקסל ונסה שנית. זה גם אפשרי שהשרתים של ה API של הייפיקסל מכובים. ',
    'chooselisted': ',תבחר אחד מהפרופילים שהוצגו',
    'unnecessary': 'יש לך טליסמן לא נחוץ!',
    'noweapon': 'אין עליך שום נשק!\nשים אחד באינבנטורי ונסה שנית',
    'weapon?': 'איזה נשק תרצה לבדוק?',
    'usenameornumber': 'תרשום את השם של הנשק או מספרו בטבלה',
    'profileaccepted': 'פרופיל אושר!',
    'correctequip?': 'האם זה הציוד הנכון? [כן/לא]',
    'ansy/n': 'בבקשה תענה עם כן או לא',
    'potion?': 'האם אתה משתמש %s שיקוי עם הסט הזה? [כן/לא]',  # potion_name
    'potionlvl?': 'איזה רמה של %s שיקוי אתה משתמש?',  # damaging_potions[self.potion_id]["name"]
    'enternumb': 'שגיאה! תרשום מספר',
    'critgoal?': '''אתה מתכוון להשתמש או לא להשתמש בשיקוי crit?
האם אתה רוצה שיהיה לך 80% crit בכל מקרה? [ כן/לא]''',
    'overflux': 'גיליתי שאתה משתמש ב overflux orb. להכניס אותו לחישובים? [כן/לא]',
    'manaflux': 'גיליתי שאתה משתמש mana flux orb. להכניס אותו לחישובים? [כן/לא]',
    'tuba': 'גיליתי שאתה משתמש weird tuba. להכניס אותה לחישובים? [כן/לא]',
    'target?': 'על איזה סוג מוב אתה מכוון את הבסיס?',
    'pickactivities': 'שגיאה! תבחר אחד מהאופציות',
    'algstarted': 'חכה בבקשה. התאמתך תשלח בקרוב...',
    'finished': 'החישובים הושלמו!',
    'disclaimer': '''תוספת כוח מנשקים מסוימים לא נכללת בחישוב כגון scorpion foil או reaper falchion.
החישוב  אמור להשאר נכון.''',
    'shoulddeal': 'הסט הזה אמור להוריד %s damage',  # round(damage)
    'withoutcrit': '> %s בלי crit',  # round(non_crit)
    'noroute': '''אתה לא יכול כרגע להשיג 100%% crit chance.
תשפר את רמת ה combat שלך ותשיג עוד טליסמנס לפני שאתה מתחיל חישוב חדש.'''
}
