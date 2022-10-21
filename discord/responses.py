import settle


def handle_response(message, user) -> str:
    u = ''
    if user == 'MARK_DISCORD_USERNAME':
        u = 'Mark'
    elif user == 'ERIC_DISCORD_USERNAME':
        u = 'Eric'
    elif user == 'JON_DISCORD_USERNAME':
        u = 'Jon'
    elif user == 'ANDREW_DISCORD_USERNAME':
        u = 'Andrew'

    p_message = message.lower()
    if p_message == '!hello':
        return 'Hey there!'

    if p_message[0:3] == '!ac':
        words = p_message.split()
        name = words[1][0:1].upper() + words[1][1:].lower()
        return settle.add_charge(u, name, words[2], words[3])

    if p_message[0:3] == '!rc':
        words = p_message.split()
        name = words[1][0:1].upper() + words[1][1:].lower()
        return settle.remove_charge(u, name, words[2])

    if p_message == '!cc':
        return settle.check_charges(u)

    if p_message == '!co':
        return settle.check_owed(u)

    if p_message == '!help':
        msg = '**Accountant Bot Help: ** \n\n`' \
              'Check Charges: \"!cc\"\n' \
              'Check Owed Balances: \"!co\"\n' \
              'Add Charge to User: \"!ac <user> <amount> <note>\"\n' \
              'Remove Charge from User: \"!rc <user> <amount> <note>\"`'
        return msg

