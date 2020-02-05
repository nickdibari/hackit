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

## Demo

1. Run the flask app

`(venv) python app.py`

2. Open the login page
- 127.0.0.1:5000/

3. Show the found users list
- Could have come from LinkedIn

4. Show information gathering on login page
- What happens when you submit a login?
- Where does the request go?
- What information is included in the request?
- What happens when you try to login with a fake username?
- What happens on a failed login?

5. Show hack script
- Where do the password lists come from?
- How can we test logins?
- How do we know when we found a login combo?

