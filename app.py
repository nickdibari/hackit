from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_endpoint():
    # Database of username/password combos
    users = {
        'jsmith': 'soccer',         # common_passwords.txt
        'aadams': 'lebron23',       # darkweb.txt
        'vhedie': 'ungovernable',   # myspace.txt
    }

    username = request.form.get('username')
    password = request.form.get('password')

    if not users.get(username):
        return app.response_class(status=404)

    if password != users.get(username):
        return app.response_class(status=403)

    return app.response_class(status=200)


@app.route('/profile')
def profile():
    username = request.args.get('username')
    return render_template('profile.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
