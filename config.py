"""Module to store all the settings constants for the application."""

import os
import sqlalchemy as sa

PATH_CLI_DRIVER = "C:/Users/vp.vincentelli/envs/env_bq_3_11_pip/Lib/site-packages/clidriver/bin/amd64.VC12.CRT"
PATH_CLI_DRIVER_2 = (
    "C:/Users/vp.vincentelli/envs/env_bq_3_11_pip/Lib/site-packages/clidriver/bin/icc64"
)

PATH_LOG = "log/logs.log"
PATH_LOG_SQL = "log/logs_sql.log"

# si windows
if os.name == "nt":
    PATH_DATA_FOLDER = "data/"
else:
    PATH_DATA_FOLDER = "/app/data/"
    
lil_nav = {
    "MARINA II": "MAR",
    "MEGA VICTORIA": "MVI",
    "MEGA ONE": "ME1",
    "MEGA TWO": "ME2",
    "MEGA THREE": "ME3",
    "MEGA FOUR": "ME4",
    "MEGA FIVE": "ME5",
    "MEGA SMERALDA": "SME",
    "MEGA ANDREA": "MEA",
    "PASCAL LOTA": "LOT",
    "MEGA REGINA": "MRE",
    "VERA": "VER",
    "EXPRESS III": "EX3",
    "MEGA GENE ONE": "MG1",
    "MEGA GENE TWO": "MG2",
    "MEGA GENE THREE": "MG3",
    "MEGA GENE FOUR": "MG4",
    "CRUISE GENE ONE": "CG1",
    "CRUISE GENE TWO": "CG2",
    "MEGA GENE FIVE": "MG5",
    "MEGA GENE SIX": "MG6",
    "MEGA GENE SEVEN": "MG7",
    "MEGA GENE EIGHT": "MG8",
}

cod_nav_lil = {
    4: "MAR",
    9: "ME1",
    6: "VER",
    7: "EX3",
    12: "ME2",
    14: "ME3",
    15: "ME4",
    16: "ME5",
    17: "SME",
    18: "MEA",
    19: "LOT",
    31: "MG1",
    32: "MG2",
    33: "MG3",
    34: "MG4",
    24: "MRE",
    35: "CG1",
    36: "CG2",
    37: "MG5",
    38: "MG6",
    39: "MG7",
    41: "MG8",
    28: "MVI",
}

lil_nav_olakala = {
    "CORSICA MARINA 2": "MAR",
    "MEGA VICTORIA": "MVI",
    "MEGA EXPRESS 1": "ME1",
    "MEGA EXPRESS 2": "ME2",
    "MEGA EXPRESS 3": "ME3",
    "MEGA EXPRESS 4": "ME4",
    "MEGA EXPRESS 5": "ME5",
    "MEGA SMERALDA": "SME",
    "MEGA ANDREA": "MEA",
    "PASCAL LOTA": "LOT",
    "MEGA REGINA": "MRE",
    "SARDINIA VERA": "VER",
    "CORSICA EXPRESS 3": "EX3",
}

# Dictionnaire des problématiques pour les commentaires globaux
problematiques_global = {
    "Orari nave": [
        "retard",
        "heure",
        "arrivée",
        "départ",
        "late",
        "ritardo",
        "ora",
        "arrivo",
        "partenza",
        "departure",
        "arrival",
        "hour",
        "orari",
    ],
    "Garage": [
        "bÃ£Â©tail",
        "parkings",
        "vÃ£Â©hicules",
        "vÃ£Â©hicule",
        "parqués",
        "parquées",
        "bétail",
        "chauffeur",
        "véhicule",
        "véhicules",
        "garage",
        "garages",
        "place",
        "parking",
        "circuler",
        "posto",
        "parcheggio",
        "circolatore",
        "serrer",
        "serré",
        "serrés",
        "serrées",
        "stretto",
        "stretta",
        "strette",
        "squeeze",
        "squeezed",
        "tight",
        "serrées",
        "serrés",
        "garer",
        "garés",
        "garé",
        "garée",
        "garées",
        "collées",
        "collée",
        "voiture",
    ],
    "Amabilità Personale": [
        "stewards",
        "friendly",
        "réception",
        "reception",
        "dÃ£Â©sagrÃ£Â©ables",
        "personnels",
        "personel",
        "personnelle",
        "politesse",
        "poli",
        "équipe",
        "personnel",
        "amabilité",
        "aimable",
        "courtois",
        "éducation",
        "personale",
        "amabile",
        "accueil",
        "désagréable",
        "educato",
        "cortese",
        "educazione",
        "istruzione",
        "cortesia",
        "scortese",
        "educazione",
        "maleducato",
        "souriant",
        "soridente",
        "smile",
        "agréable",
    ],
    "Rumorosità": [
        "craquement",
        "vibre",
        "bruits",
        "grincement",
        "craquements",
        "métalliques",
        "moteur",
        "vibration",
        "bruit",
        "motore",
        "vibrazioni",
        "rumore",
        "bruyant",
        "rumorosa",
        "rumoroso",
        "bruyante",
        "noisy",
        "noise",
        "ventilation",
        "vibrations",
        "moteur",
        "moteurs",
        "ventilée",
    ],
    "Wifi": ["connexion", "wifi", "connessione", "connecter", "wi-fi"],
    "Comunicazione": [
        "langue",
        "parle",
        "français",
        "language",
        "speak",
        "lingua",
        "parlare",
    ],
    "Pulizia Cabina": [
        "pulita",
        "sporco",
        "propres",
        "sporca",
        "propreté",
        "propre",
        "hygiène",
        "sale",
        "saleté",
        "poussière",
        "pulizia",
        "clean",
        "dirty",
        "dirt",
        "gross",
        "filthy",
        "joints",
        "cleaning",
        "propres",
    ],
    "Biancheria": [
        "serviette",
        "serviettes",
        "drap",
        "draps",
        "oreiller",
        "oreillers",
        "couette",
        "couettes",
        "teli bagno",
        "lenzuola",
        "cuscino",
        "piumino",
        "piumini",
        "sheet",
        "sheets",
        "pillow",
        "pillows",
        "towel",
        "towels",
        "duvet",
        "duvets",
        "cuscini",
    ],
    "Materassi": ["literie", "matelas", "letti", "materassi", "bedding"],
    "Checkout / Check-in (cabina)": [
        "liberer",
        "prêt",
        "prête",
        "leave the cabin",
        "libération",
        "liberation",
        "libère",
        "libere",
        "libérer",
        "liberare",
        "release",
        "check-out",
        "check out",
        "checkout",
        "prête",
        "pronto",
        "pronta",
    ],
    "Temperatura": [
        "température",
        "cold",
        "temperatura",
        "aircondition",
        "conditioning",
        "conditioned",
        "surchauffÃ©",
        "surchauffé",
        "surchauffée",
        "temperature",
        "climatisation",
        "conditionning",
        "chaud",
        "air condition",
        "ventilation",
        "glacial",
        "glacé",
        "chaude",
        "chaudes",
        "chauffage",
        "freddo",
        "clim",
        "ac",
        "température",
        "chaud",
        "froid",
        "condizionata",
        "conditioner",
        "climatisation",
        "surchauffé",
        "surchauffée",
        "glacial",
        "chaleur",
        "heating",
    ],
    "Acqua calda": ["eau", "acqua"],
    "Bagni": [
        "salle de bain",
        "bathrooms",
        "bathroom",
        "toilet",
        "douche",
        "doccia",
        "fuite",
        "perdita",
        "bouché",
        "lavabo",
        "toilette",
        "toilettes",
        "wc",
        "bagni",
        "otturati",
        "bagno",
        "bouchée",
        "bouchées",
        "otturato",
    ],
    "Odori": [
        "odeur",
        "odore",
        "égoûts",
        "fogna",
        "ombrinale",
        "ombrinali",
        "scarico",
        "odour",
        "smell",
        "odeurs",
        "odours",
    ],
    "Prezzi": [
        "chÃ£Â¨res",
        "chères",
        "costo",
        "pognon",
        "onéreux",
        "€",
        "pagato",
        "exorbitant",
        "tarif",
        "tarifs",
        "prezzo",
        "prix",
        "price",
        "cher",
        "chère",
        "caro",
        "cara",
        "expensive",
        "euro",
        "euros",
        "prezzi",
        "exhorbitant",
        "cout",
        "coût",
        "chers",
        "chere",
    ],
    "Nave vetusta": [
        "entretenu",
        "vieux",
        "vétuste",
        "vecchio",
        "fatiscente",
        "délabré",
        "obsolete",
        "outdated",
        "vieillissant",
        "ancien",
        "ancienne",
    ],
    "Meteo": [
        "mouvementé",
        "mouvementée",
        "agité",
        "agitée",
        "meteo",
        "weather",
        "vent",
        "wind",
        "vento",
        "vague",
        "vagues",
        "onde",
        "wave",
        "waves",
        "tempête",
        "tempete",
        "tempesta",
        "intempérie",
        "intempéries",
    ],
    "PMR": [
        "pmr",
        "PMR",
        "handicap",
        "handicapé",
        "handicapée",
        "handicapés",
        "handicapées",
        "disabilitata",
        "disabilitato",
        "disabilitati",
        "disabilità",
        "disabilitate",
        "disabled",
        "mobilità",
        "disabilities",
        "handicapped",
    ],
    "Sveglia": [
        "expulser",
        "expulse",
        "réveiller",
        "réveil",
        "sveglia",
        "wake up",
        "wake",
        "wakeup",
        "reveiller",
        "réveillé",
        "réveillés",
        "lever",
    ],
    "Videogiochi": [
        "jeux video",
        "video game",
        "monnayeur",
        "videogiochi",
        "cambio monete",
    ],
    "Imbarco/sbarco": [
        "indications",
        "signalisation",
        "signalling",
        "top position",
        "express boarding",
        "disembarking",
        "onboarding",
        "sortie",
        "dÃ£Â©barquement",
        "disembarkation",
        "embarquement",
        "débarquement",
        "imbarco",
        "sbarco",
        "boarding",
        "landing",
        "embarquer",
        "embarqué",
        "debarquement",
        "l'uscita",
        "uscita",
    ],
    "Arredo cabine": [
        "insonorisation",
        "modernes" "ancienne",
        "moderniser",
        "ampoule",
        "vieille",
        "vieilles",
        "lamp",
        "lampe",
        "lampe",
        "lamps",
        "televisore",
        "télévision",
        "tv",
        "televisione",
        "hublot",
        "oblo",
        "superposés",
        "moquette",
        "tappeto",
        "castello",
        "télé",
    ],
    "Ristorazione": [
        "intolleranze alimentari",
        "pain",
        "pane",
        "gluten",
        "repas",
        "restauration",
        "restaurant",
        "self",
        "manger",
        "déjeuner",
        "diner",
        "dîner",
        "petit déjeuner",
        "petit-déjeuner",
        "plat",
        "menu",
        "ristorazione",
        "ristorante",
        "mangiare",
        "pranzo",
        "cena",
        "cenare",
        "colazione",
        "piatti",
        "piatto",
        "plats",
        "cuisine",
        "nourriture",
    ],
    "Sicurezza": ["barrière", "barra anticaduta", "anticaduta"],
    "Passaggio d'informazioni": [
        "micro",
        "information",
        "informé",
        "informazione",
        "sms",
        "annonce",
        "annunci",
        "informations",
        "announcement",
        "message",
        "messages" "communication",
        "announcements" "audible",
        "inaudible",
    ],
    "Bar": [
        "boire",
        "bars",
        "bar",
        "café",
        "caffè",
        "coffee",
        "cocktail",
        "cocktails",
        "apéritif",
        "aperitivo",
        "apéritifs",
        "coktails",
        "coktail",
    ],
    "Cani": [
        "cane",
        "cani",
        "chien",
        "chiens",
        "dog",
        "dogs",
        "bark",
        "aboyer",
        "déjection",
        "abbaiare",
        "promenade",
    ],
    "Ascensori": [
        "ascensori",
        "ascenseur",
        "elevator",
        "lift",
        "lifts",
        "ascensore",
        "ascenseurs",
    ],
    "Complimenti generichi": [
        "servizio ottimo",
        "très satisfaisant",
        "très satisfait",
        "bonne traversÃ£Â©e",
        "tutto ok",
        "trÃ£Â¨s bonne prestation",
        "très bonne prestation",
        "trÃ£Â¨s bien",
        "trés bien",
        "bonne traversée",
        "belle traversée",
        "bonne traversée",
        "très bonne traversée",
        "très satisfait",
        "très satisfaite",
        "rien à signaler",
        "très bien",
        "tres bien",
        "impeccable",
        "parfait",
        "impeccabile",
        "perfetto",
        "perfect",
        "super",
        "ras",
        "merci",
        "grazie",
        "excellent",
    ],
    "Pagamento": [
        "CB",
        "carte bleue",
        "carte bancaire",
        "carte",
        "cartes bleu",
        "espèces",
        "especes",
    ],
    "Spazzi publichi": [
        "endroits",
        "music",
        "musica",
        "musique",
        "sièges",
        "siÃ£Â¨ges",
        "sofas",
        "area",
        "corridori",
        "corridoi",
        "passage",
        "per terra",
        "par terre",
        "allongés",
        "allongé",
        "places",
        "place",
        "loungers",
        "sun loungers",
        "allongé",
        "place assise",
        "places assises",
        "espace extérieur",
        "d'espace extérieur",
    ],
    "Salle poltrone": [
        "excellente traversée",
        "salon fauteuils",
        "armchair",
        "poltrona",
        "poltrone",
        "fauteuil",
        "fauteuils",
        "lumière",
        "lumiÃ£Â¨re",
        "luci",
        "lumiÃ£Â¨res",
        "lumières",
        "salons",
    ],
    "Zona bambini": ["jeux enfants", "giocchi di bambini"],
    "Tipologia Luxe": ["luxe"],
}

# Dictionnaires des problématiques pour embarquement et cabine
problematiques_embarquement = {
    "Ritardo della nave": [
        "retard",
        "heure",
        "arrivée",
        "départ",
        "late",
        "ritardo",
        "ora",
        "arrivo",
        "partenza",
        "departure",
        "arrival",
        "hour",
    ],
    "Garage": [
        "garage",
        "garages",
        "place",
        "parking",
        "circuler",
        "posto",
        "parcheggio",
        "circolatore",
        "serrer",
        "serré",
        "serrés",
        "serrées",
        "stretto",
        "stretta",
        "strette",
        "squeeze",
        "squeezed",
        "tight",
    ],
    "Amabilità Personale": [
        "équipe",
        "personnel",
        "amabilité",
        "aimable",
        "courtois",
        "éducation",
        "personale",
        "amabile",
        "accueil",
        "désagréable",
        "educato",
        "cortese",
        "educazione",
        "istruzione",
        "cortesia",
        "scortese",
        "educazione",
        "maleducato",
        "souriant",
        "soridente",
        "smile",
    ],
    "Rumorosità": [
        "grince",
        "craque",
        "alarme",
        "alarmes",
        "grincements",
        "grincement",
        "isolation",
        "craquements",
        "craquement",
        "métalliques",
        "moteur",
        "vibration",
        "bruit",
        "motore",
        "vibrazioni",
        "rumore",
        "bruyant",
        "rumorosa",
        "rumoroso",
        "bruyante",
        "noisy",
        "noise",
    ],
    "Wifi": ["connexion", "wifi", "connessione", "internet"],
    "Comunicazione": [
        "langue",
        "parle",
        "français",
        "language",
        "speak",
        "lingua",
        "parlare",
    ],
    "Pulizia Cabina": [
        "miettes",
        "poils",
        "pisse",
        "propreté",
        "propre",
        "hygiène",
        "sale",
        "saleté",
        "poussière",
        "pulizia",
        "clean",
        "dirty",
        "dirt",
        "gross",
        "filthy",
        "joints",
        "usé",
        "usée",
        "vomis",
        "vomi",
    ],
    "Biancheria": [
        "savon",
        "soap",
        "serviette",
        "serviettes",
        "drap",
        "draps",
        "oreiller",
        "oreillers",
        "couette",
        "couettes",
        "teli bagno",
        "lenzuola",
        "cuscino",
        "piumino",
        "piumini",
        "sheet",
        "sheets",
        "pillow",
        "pillows",
        "towel",
        "towels",
        "duvet",
        "duvets",
        "cuscini",
    ],
    "Materassi": ["literie", "matelas", "letti", "materassi", "bedding"],
    "Checkout (liberare la cabina)": [
        "libérer",
        "liberare",
        "release",
        "check-out",
        "check out",
        "checkout",
    ],
    "Aria Condizionata": [
        "glacial",
        "glacé",
        "chaude",
        "chaudes",
        "chauffage",
        "freddo",
        "clim",
        "ac",
        "température",
        "chaud",
        "froid",
        "condizionata",
        "conditioner",
        "climatisation",
        "surchauffé",
        "surchauffée",
        "glacial",
        "chaleur",
    ],
    "Acqua calda": ["eau", "acqua", "eau chaude", "acqua calda"],
    "Bagni": [
        "bouché",
        "lavabo",
        "toilette",
        "toilettes",
        "wc",
        "bagni",
        "otturati",
        "bagno",
        "bouchée",
        "bouchées",
        "otturato",
    ],
    "Odori": [
        "odeur",
        "odore",
        "égoûts",
        "fogna",
        "ombrinale",
        "ombrinali",
        "scarico",
        "odour",
        "smell",
        "smells",
    ],
    "Prezzi": [
        "€",
        "pagato",
        "exorbitant",
        "tarif",
        "tarifs",
        "prezzo",
        "prix",
        "price",
        "cher",
        "chère",
        "caro",
        "cara",
        "expensive",
        "euro",
        "euros",
        "prezzi",
        "exhorbitant",
        "cout",
        "coût",
        "chers",
    ],
    "Nave vetusta": [
        "vieux",
        "vétuste",
        "vecchio",
        "fatiscente",
        "délabré",
        "obsolete",
        "outdated",
        "vieillissant",
    ],
    "Meteo": [
        "meteo",
        "weather",
        "vent",
        "wind",
        "vento",
        "vague",
        "vagues",
        "onde",
        "wave",
        "waves",
        "tempête",
        "tempete",
        "tempesta",
    ],
    "PMR": [
        "handicap",
        "handicapé",
        "handicapée",
        "handicapés",
        "handicapées",
        "disabilitata",
        "disabilitato",
        "disabilitati",
        "disabilità",
        "disabilitate",
        "disabled",
        "mobilità",
        "disabilities",
        "handicapped",
    ],
    "Sveglia": ["réveil", "sveglia", "wake up", "wake", "wakeup"],
    "Videogiochi": [
        "jeux video",
        "video game",
        "monnayeur",
        "videogiochi",
        "cambio monete",
    ],
    "Imbarco/sbarco": [
        "embarquement",
        "débarquement",
        "imbarco",
        "sbarco",
        "boarding",
        "landing",
        "embarquer",
        "embarqué",
    ],
    "Arredo cabine": [
        "cassé",
        "cassés",
        "cassée",
        "cassées",
        "tablette",
        "table",
        "siège",
        "asseoir",
        "s'asseoir",
        "tabouret",
        "chaise",
        "seat",
        "televisore",
        "télévision",
        "tv",
        "televisione",
        "hublot",
        "oblo",
        "superposés",
        "moquette",
        "tappeto",
        "castello",
        "télé",
        "couchette",
        "veilleuse",
        "veilleuses",
    ],
    "Ristorazione": [
        "charcuterie",
        "plateau",
        "repas",
        "restauration",
        "restaurant",
        "self",
        "manger",
        "déjeuner",
        "diner",
        "dîner",
        "petit déjeuner",
        "petit-déjeuner",
        "plat",
        "menu",
        "ristorazione",
        "ristorante",
        "mangiare",
        "pranzo",
        "cena",
        "cenare",
        "colazione",
        "piatti",
        "piatto",
    ],
    "Furto": ["furto", "vol", "voler", "volare", "volo", "rubare"],
}
problematiques_cabine = {
    "Ritardo della nave": [
        "retard",
        "heure",
        "arrivée",
        "départ",
        "late",
        "ritardo",
        "ora",
        "arrivo",
        "partenza",
        "departure",
        "arrival",
        "hour",
    ],
    "Garage": [
        "garage",
        "garages",
        "place",
        "parking",
        "circuler",
        "posto",
        "parcheggio",
        "circolatore",
        "serrer",
        "serré",
        "serrés",
        "serrées",
        "stretto",
        "stretta",
        "strette",
        "squeeze",
        "squeezed",
        "tight",
    ],
    "Amabilità Personale": [
        "équipe",
        "personnel",
        "amabilité",
        "aimable",
        "courtois",
        "éducation",
        "personale",
        "amabile",
        "accueil",
        "désagréable",
        "educato",
        "cortese",
        "educazione",
        "istruzione",
        "cortesia",
        "scortese",
        "educazione",
        "maleducato",
        "souriant",
        "soridente",
        "smile",
    ],
    "Rumorosità": [
        "grince",
        "craque",
        "alarme",
        "alarmes",
        "grincements",
        "grincement",
        "isolation",
        "craquements",
        "craquement",
        "métalliques",
        "moteur",
        "vibration",
        "bruit",
        "motore",
        "vibrazioni",
        "rumore",
        "bruyant",
        "rumorosa",
        "rumoroso",
        "bruyante",
        "noisy",
        "noise",
    ],
    "Wifi": ["connexion", "wifi", "connessione", "internet"],
    "Comunicazione": [
        "langue",
        "parle",
        "français",
        "language",
        "speak",
        "lingua",
        "parlare",
    ],
    "Pulizia Cabina": [
        "miettes",
        "poils",
        "pisse",
        "propreté",
        "propre",
        "hygiène",
        "sale",
        "saleté",
        "poussière",
        "pulizia",
        "clean",
        "dirty",
        "dirt",
        "gross",
        "filthy",
        "joints",
        "usé",
        "usée",
        "vomis",
        "vomi",
    ],
    "Biancheria": [
        "savon",
        "soap",
        "serviette",
        "serviettes",
        "drap",
        "draps",
        "oreiller",
        "oreillers",
        "couette",
        "couettes",
        "teli bagno",
        "lenzuola",
        "cuscino",
        "piumino",
        "piumini",
        "sheet",
        "sheets",
        "pillow",
        "pillows",
        "towel",
        "towels",
        "duvet",
        "duvets",
        "cuscini",
    ],
    "Materassi": ["literie", "matelas", "letti", "materassi", "bedding"],
    "Checkout (liberare la cabina)": [
        "libérer",
        "liberare",
        "release",
        "check-out",
        "check out",
        "checkout",
    ],
    "Aria Condizionata": [
        "glacial",
        "glacé",
        "chaude",
        "chaudes",
        "chauffage",
        "freddo",
        "clim",
        "ac",
        "température",
        "chaud",
        "froid",
        "condizionata",
        "conditioner",
        "climatisation",
        "surchauffé",
        "surchauffée",
        "glacial",
        "chaleur",
    ],
    "Acqua calda": ["eau", "acqua", "eau chaude", "acqua calda"],
    "Bagni": [
        "bouché",
        "lavabo",
        "toilette",
        "toilettes",
        "wc",
        "bagni",
        "otturati",
        "bagno",
        "bouchée",
        "bouchées",
        "otturato",
    ],
    "Odori": [
        "odeur",
        "odore",
        "égoûts",
        "fogna",
        "ombrinale",
        "ombrinali",
        "scarico",
        "odour",
        "smell",
        "smells",
    ],
    "Prezzi": [
        "€",
        "pagato",
        "exorbitant",
        "tarif",
        "tarifs",
        "prezzo",
        "prix",
        "price",
        "cher",
        "chère",
        "caro",
        "cara",
        "expensive",
        "euro",
        "euros",
        "prezzi",
        "exhorbitant",
        "cout",
        "coût",
        "chers",
    ],
    "Nave vetusta": [
        "vieux",
        "vétuste",
        "vecchio",
        "fatiscente",
        "délabré",
        "obsolete",
        "outdated",
        "vieillissant",
    ],
    "Meteo": [
        "meteo",
        "weather",
        "vent",
        "wind",
        "vento",
        "vague",
        "vagues",
        "onde",
        "wave",
        "waves",
        "tempête",
        "tempete",
        "tempesta",
    ],
    "PMR": [
        "handicap",
        "handicapé",
        "handicapée",
        "handicapés",
        "handicapées",
        "disabilitata",
        "disabilitato",
        "disabilitati",
        "disabilità",
        "disabilitate",
        "disabled",
        "mobilità",
        "disabilities",
        "handicapped",
    ],
    "Sveglia": ["réveil", "sveglia", "wake up", "wake", "wakeup"],
    "Videogiochi": [
        "jeux video",
        "video game",
        "monnayeur",
        "videogiochi",
        "cambio monete",
    ],
    "Imbarco/sbarco": [
        "embarquement",
        "débarquement",
        "imbarco",
        "sbarco",
        "boarding",
        "landing",
        "embarquer",
        "embarqué",
    ],
    "Arredo cabine": [
        "cassé",
        "cassés",
        "cassée",
        "cassées",
        "tablette",
        "table",
        "siège",
        "asseoir",
        "s'asseoir",
        "tabouret",
        "chaise",
        "seat",
        "televisore",
        "télévision",
        "tv",
        "televisione",
        "hublot",
        "oblo",
        "superposés",
        "moquette",
        "tappeto",
        "castello",
        "télé",
        "couchette",
        "veilleuse",
        "veilleuses",
    ],
    "Ristorazione": [
        "charcuterie",
        "plateau",
        "repas",
        "restauration",
        "restaurant",
        "self",
        "manger",
        "déjeuner",
        "diner",
        "dîner",
        "petit déjeuner",
        "petit-déjeuner",
        "plat",
        "menu",
        "ristorazione",
        "ristorante",
        "mangiare",
        "pranzo",
        "cena",
        "cenare",
        "colazione",
        "piatti",
        "piatto",
    ],
    "Furto": ["furto", "vol", "voler", "volare", "volo", "rubare"],
}

dtypes_resa_sa = dtype_dict = {
    "dat_dep": sa.DateTime,
    "cod_lign": sa.String,
    "hor_dep": sa.String,
    "dat_resa": sa.DateTime,
    "cod_navi": sa.Integer,
    "cod_comp": sa.Integer,
    "cod_pays": sa.String,
    "canal": sa.String,
    "qte_pax": sa.Integer,
    "qte_veh": sa.Integer,
    "qte_cab": sa.Integer,
    "mnt_resa": sa.Float,
    "qte_ml": sa.Integer,
    "mnt_fret": sa.Float,
    "qte_pax0": sa.Integer,
    "qte_veh0": sa.Integer,
    "qte_cab0": sa.Integer,
    "mnt_resa0": sa.Float,
    "qte_ml0": sa.Integer,
    "mnt_fret0": sa.Float,
    "is_generic": sa.Boolean,
    "matching_date_dema_current_year": sa.DateTime,
}
