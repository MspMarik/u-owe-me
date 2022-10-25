import settle
import yaml

info = 'LOGIN_YAML_INFO'

with open(info) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)


def handle_response(message, user) -> str:
    u = ''
    for i in data['contact']['discord']:
        if user == data['contact']['discord'][i]:
            u = i

    p_message = message.lower()
    if p_message == '!hello':
        return 'Hey there!'

    if p_message[0:3] == '!ac':
        words = p_message.split()
        name = words[1][0:1].upper() + words[1][1:].lower()
        try:
            amt = float(words[2])
            return settle.add_charge(u, name, amt, words[3])
        except:
            return "Unable to add charge, amount is not a number"

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
              'Remove Charge from User: \"!rc <user> <note>\"`'
        return msg

