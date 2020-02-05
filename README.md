# hackit
Demo site for Cypurr presentation on password security

All password lists were scraped from the [SecLists/Passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords) index


## Installation
1. Create a Python3 virtual enviornment

```
virtualenv -p $(which python3) venv
source venv/bin/activate
```

2. Install dependencies

`(venv) pip install -r requirements.txt`

## Usage
1. Run the flask app

`(venv) python app.py`

2. Run the hacker script for a given user

`(venv) python hackit.py <username>`

- Usernames can be found from the username (part before the @evilcorp.com) in the [found_users.txt](https://github.com/nickdibari/hackit/blob/master/found_users.txt) file
- Pass `--use_myspace` for the `vhedie` user to use the Myspace password list
