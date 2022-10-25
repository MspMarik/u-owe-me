import requests
import json
import yaml

info = 'INFO_YAML_PATH'

with open(info) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)


def handle_link(user):
    for i in data["contact"]["ha_push"]:
        if i == user:
            return data["contact"]["ha_push"][i]


def add(rec, amt, user, note):
    url = handle_link(rec)
    msg = f"New charge has been added to your account - You now owe {user} ${amt} for {note}"
    ttl = f"New Charge Notification: ${amt}"

    send = {'value1': f"{msg}", 'value2': f'{ttl}'}
    response = requests.post(url, data=json.dumps(send), headers={'Content-Type': 'application/json'})


def delete(rec, amt, user, note):
    url = handle_link(rec)
    msg = f"Charge removed from your account: {user} ${amt} for {note}"
    ttl = f"Charge Removal Notification: ${amt}"

    send = {'value1': f"{msg}", 'value2': f'{ttl}'}
    response = requests.post(url, data=json.dumps(send), headers={'Content-Type': 'application/json'})


def remind(rec, amt, user, note):
    url = handle_link(rec)
    msg = f"Don't forget to send your payment!"
    ttl = f"Charge Reminder: You owe {user} ${amt} for {note}"

    send = {'value1': f"{msg}", 'value2': f'{ttl}'}
    response = requests.post(url, data=json.dumps(send), headers={'Content-Type': 'application/json'})
