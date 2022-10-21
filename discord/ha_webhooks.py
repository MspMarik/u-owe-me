import requests
import json

eric_url = 'https://hooks.nabu.casa/gAAAAABjTxP5es2qD2jGeW6_6eP6E2weYRYpYLmdF_0PZ8anbokR0jU2J_XnR3eh-uDWDqfDzkJkj8AbFFTeQyOo_8uTvYxpwVvxYygeAwodjeiu_9_lBhZhgNj9XB9YN_bY6A8wm80OvK0AxqH4M7hAetW2ZcwH52W2Yz4RCQBricjRBLTJtS0='
mark_url = 'https://hooks.nabu.casa/gAAAAABjTyA_l8ZxHUFH-fm67Dh--e_ST8NJPHXoKHOajzhf3iFSZblA4qEjlT56_dGF6oYplPBynRenE1wz7Hpsq_bJ6AV4zIHh_vEpvs8G0X5pSUPqbolI41L-5WxB6pgDdTtLj97LiwE38bfAjbIHZ1T8NAXBuKaWyDu3jwt_9-mQmgdJIXI='
andrew_url = 'https://hooks.nabu.casa/gAAAAABjTyI4xStOEoOkI0eChZvbg-v3XDPb_1H5cmhLf1jJOD7viNE-tNUpFqSmjyHXpVpmkJeI9wHYQVUSgEQWx8fOuM9RDbH396TnRcGynQ74rBud2ioDuMt2F_iaFdReyyA-jXf1RRfeVumhnOlfERMPrp9gqHEZ5aoYkRFGHEt6HDyBWWI='
jon_url = 'https://hooks.nabu.casa/gAAAAABjTzLY7DqZF95VwBHv-UIEgt8gZDstwMLBfrKuOzz03kGpFRF7bXjl8kto2Dozk20mhiFpR7orvjYVt9876Ca4bhPclpJACTltYXpHgFQQXV-d7Tlfi5yQLi1aubxtPg44QIrmvwr7LI8u-54DXffqpbeXksQBFbTUTBZ7hxzswP7MYwk='


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
