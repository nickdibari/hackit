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

2. Open the login page at `127.0.0.1:5000/`

3. Show the found users list (scraped from LinkedIn search?)

4. Show information gathering on login page
- Try to login with the whole email (What status is printed?)
- Try to login with just the user part (What *different* status is printed?)

5. Show password lists
- Sourced from [SecLists passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords)
- Go through common list from the 10 million passwords list

6. Hack a user!
- Run `python hack.py jsmith`
- Show a successful login with retrieved password
- Run `python hack.py aadams` (How long did it take?)
- Show failure for vhedie when using common passwords (What else can we do?)
- Run `python hack.py vhedie --use_myspace` and show successful login
