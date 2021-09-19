users = {
    'aeinstein': {
        'first' : 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first' : 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for user_name, user_info in users.items():
    print(f"UserName: {user_name.title()}")
    full_name = f"{user_info.get('first').title()} {user_info.get('last').title()}"
    location = f"{user_info.get('location').title()}"

    print(f" \tFullName: {full_name} \n\t Location: {location}")
