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
titlecase_slova = []
uppercase_slova = []
lowercase_slova = []
numeric_strings = []
suma_cisel = []

for slovo in slova:
  pocet_slov.append(len(slovo))
  titlecase_slova.append(sum(word.istitle() for word in slovo))
  uppercase_slova.append(sum(word.isupper() and word.isalpha() for word in slovo))
  lowercase_slova.append(sum(word.islower() for word in slovo))
  numeric_strings.append(sum(word.isnumeric() for word in slovo))
  suma_cisel.append(sum(int(word) for word in slovo if word.isnumeric()))

users = dict()

user_1 = {'name': 'bob', 'password': '123'}
user_2 = {'name': 'ann', 'password': 'pass123'}
user_3 = {'name': 'mike', 'password': 'password123'}
user_4 = {'name': 'liz', 'password': 'pass123'}

users = {
    user_1['name']: user_1['password'],
    user_2['name']: user_2['password'],
    user_3['name']: user_3['password'],
    user_4['name']: user_4['password']
}

username = input("Username: ")
password = input("Password: ")

oddelovac = '-' * 40

if users:
  if username not in users:  
    print('Unregistered user, terminating the program.')
  
  elif users.get(username) != password:  
    print('Wrong password, terminating the program.')
  
  else:
    print(oddelovac)
    print('Welcome to the app,', username)

registered_user = username in users and users.get(username) == password

if registered_user:
  pocet_textu = len(TEXTS)
  print('We have', pocet_textu, 'texts to be analyzed.')
  print(oddelovac)
  vybrane_cislo = input('Enter a number btw. 1 and ' + str(pocet_textu ) + ' to select: ')
  if vybrane_cislo.isnumeric() and int(vybrane_cislo) in range(1, pocet_textu + 1):
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


    print("LEN|    OCCURRENCES    |NR.")
    print("----------------------------------------")
    for length in sorted(word_lengths):
      occurrences = word_lengths[length]
      print(f"{length:>3}|{'*' * occurrences:<18}|{occurrences}")

  else:
    print('Wrong selection, terminating the program.')