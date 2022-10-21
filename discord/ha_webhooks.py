import requests
import json

eric_url = 'ERIC_LINK'
mark_url = 'MARK_LINK'
andrew_url = 'ANDREW_LINK'
jon_url = 'JON_LINK'


def add(rec, amt, user, note):

    url = ''
    msg = f"New charge has been added to your account - You now owe {user} ${amt} for {note}"
    ttl = f"New Charge Notification: ${amt}"
    if rec == 'Eric':
        url = eric_url
    elif rec == 'Mark':
        url = mark_url
    elif rec == 'Andrew':
        url = andrew_url
    elif rec == 'Jon':
        url = jon_url

    data = {'value1': f"{msg}", 'value2': f'{ttl}'}
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})


def delete(rec, amt, user, note):
    url = ''
    msg = f"Charge removed from your account: {user} ${amt} for {note}"
    ttl = f"Charge Removal Notification: ${amt}"
    if rec == 'Eric':
        url = eric_url
    elif rec == 'Mark':
        url = mark_url
    elif rec == 'Andrew':
        url = andrew_url
    elif rec == 'Jon':
        url = jon_url

    data = {'value1': f"{msg}", 'value2': f'{ttl}'}
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})


def remind(rec, amt, user, note):
    url = ''
    msg = f"Don't forget to send your payment!"
    ttl = f"Charge Reminder: You owe {user} ${amt} for {note}"
    if rec == 'Eric':
        url = eric_url
    elif rec == 'Mark':
        url = mark_url
    elif rec == 'Andrew':
        url = andrew_url
    elif rec == 'Jon':
        url = jon_url

    data = {'value1': f"{msg}", 'value2': f'{ttl}'}
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
