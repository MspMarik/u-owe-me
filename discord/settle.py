import yaml
import ha_webhooks

info = 'INFO_YAML_PATH'

with open(info) as f:
    token = yaml.load(f, Loader=yaml.FullLoader)

PATH_TO_YAML = token["files"]["charges_yaml"]

with open(PATH_TO_YAML) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)


def check_charges(user):
    global data
    total = 0
    msg = ''
    for i in data["users"][user]['Owe']:
        msg += f'{i}: {str(data["users"][user]["Owe"][i])}\n'
        if (str(data["users"][user]['Owe'][i]) == "null") or (str(data["users"][user]['Owe'][i]) == "None"):
            total += 0
        else:
            for j in range(0, len(data["users"][user]['Owe'][i])):
                price = data["users"][user]['Owe'][i][j].split()
                total += float(price[0])
    return msg + f"**\nTotal Charges: ${round(total, 2)}**"


def check_owed(user):
    global data
    total = 0
    msg = ''
    for i in data["users"][user]['Owed']:
        msg += f'{i}: {str(data["users"][user]["Owed"][i])}\n'
        if str(data["users"][user]['Owed'][i]) == "None":
            total += 0
        else:
            for j in range(0, len(data["users"][user]['Owed'][i])):
                price = data["users"][user]['Owed'][i][j].split()
                total += float(price[0])
    return msg + f"\n**Total Owed: ${round(total, 2)}**"


def add_charge(user, subuser, amt, note):
    global data
    if subuser.lower() == 'all':
        people = []
        for x in data['users']:
            if not str(x) == user:
                people.append(str(x))
    else:
        people = [f'{subuser}']
    charge = [f'{amt} {note}']
    for i in people:
        if (str(data["users"][user]['Owed'][i]) == "null") or (str(data["users"][user]['Owed'][i]) == "None"):
            data["users"][user]['Owed'][i] = charge
            data["users"][i]['Owe'][user] = charge
        else:
            data["users"][user]['Owed'][i].extend(charge)
            data["users"][i]['Owe'][user].extend(charge)
        ha_webhooks.add(i, amt, user, note)
    with open(PATH_TO_YAML, 'w') as x:
        dt = yaml.dump(data, x)

    return f'Charge for the amount of ${amt} for {note} added to {subuser}'


def remove_charge(user, subuser, note):
    global data
    amount = 0
    if subuser.lower() == 'all':
        people = []
        for x in data['users']:
            if not str(x) == user:
                people.append(str(x))
    else:
        people = [f'{subuser}']

    for j in people:
        dt = data["users"][user]['Owed'][j]
        rdt = data["users"][j]['Owe'][user]
        i = 0
        x = 0
        elem1 = dt[i]
        while (i < len(dt)) and (note not in str(elem1)):
            i += 1
            elem1 = dt[i]

        amount = float(dt[i].split()[0])
        dt.remove(elem1)
        rdt.remove(elem1)
        ha_webhooks.delete(j, amount, user, note)

    with open(PATH_TO_YAML, 'w') as x:
        dta = yaml.dump(data, x)

    return f'Charge for the amount of ${amount} for {note} removed from {subuser}'


# outstanding balance reminder, runs every day at 9PM using scheduled task
def notify():
    global data
    for x in data['users']:
        for i in data["users"][x]['Owe']:
            if (str(data["users"][x]['Owe'][i]) == "null") or (str(data["users"][x]['Owe'][i]) == "None") or (str(data["users"][x]['Owe'][i]) == "[]"):
                continue
            else:
                for j in range(0, len(data["users"][x]['Owe'][i])):
                    words = str(data["users"][x]['Owe'][i][j]).split()
                    ha_webhooks.remind(str(x), words[0], str(i), words[1])
