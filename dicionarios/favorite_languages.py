
favorite_language = {
    'Jan': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())
    if name in friends:
        print(f" Hi {name.title()}, \n I see your favorite language is {favorite_language.get(name).title()}." )

if 'erin' not in favorite_language.keys():
    print('Erin, please take our poll')

print("Linguagems: ")
for language in sorted(set((favorite_language.values()))):
    print(f"{language}")
