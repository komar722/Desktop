"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marie Koblizkova
email: mariekoblizkova@seznam.cz
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

slova = []
for text in TEXTS:
  slova.append(text.split())

pocet_slov = []
for slovo in slova:
  pocet_slov.append(len(slovo))

titlecase_slova = []
for slovo in slova:
  titlecase_slova.append(sum(word.istitle() for word in slovo))

uppercase_slova = []
for slovo in slova:
  uppercase_slova.append(sum(word.isupper() and word.isalpha() for word in slovo))

lowercase_slova = []
for slovo in slova:
  lowercase_slova.append(sum(word.islower() for word in slovo))

numeric_strings = []
for slovo in slova:
  numeric_strings.append(sum(word.isnumeric() for word in slovo))

suma_cisel = []
for slovo in slova:
  suma_cisel.append(sum(int(word) for word in slovo if word.isnumeric()))


users = dict()

users['name'] = ['bob', 'ann', 'mike', 'liz']
users['password'] = ['123', 'pass123', 'password123', 'pass123']

username = input("Username: ")
password = input("Password: ")

oddelovac = '-' * 40

if users:
  if username not in users['name']:
    print('Unregistered user, terminating the program.')

  elif username in users['name'] and password not in users['password']:
    print('Wrong password, terminating the program.')

  else:
    print(oddelovac)
    print('Welcome to the app,', username)
    print('We have 3 texts to be analyzed.')
    print(oddelovac)

registered_user =  username in users['name'] and password in users['password']

if registered_user:
  vybrane_cislo = input('Enter a number btw. 1 and 3 to select: ')

  if int(vybrane_cislo) not in range(1, 4):
    print('Wrong selection, terminating the program.')
  else:
    print(oddelovac)

    vybrany_text = int(vybrane_cislo) - 1

    print('There are', pocet_slov[vybrany_text], 'words in the selected text.')
    print('There are', titlecase_slova[vybrany_text], 'titlecase words.')
    print('There are', uppercase_slova[vybrany_text], 'uppercase words.')
    print('There are', lowercase_slova[vybrany_text], 'lowercase words.')
    print('There are', numeric_strings[vybrany_text], 'numeric strings.')
    print('The sum of all the numbers is', suma_cisel[vybrany_text])
    print(oddelovac)

    word_lengths = {}
    text = TEXTS[vybrany_text]
    words = text.split()
    for word in words:
      length = len(word.strip(",.!?"))
      word_lengths[length] = word_lengths.get(length, 0) + 1


    print("LEN|  OCCURRENCES  |NR.")
    print("----------------------------------------")
    for length in sorted(word_lengths):
      occurrences = word_lengths[length]
      print(f"{length:>3}|{'*' * occurrences:<15}|{occurrences}")

      
