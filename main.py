from flask import Flask, request,redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

@app.route("/add", methods=['POST'])
def user_signup():
    # look inside the request to figure out what the user typed
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    # if the user typed nothing at all, redirect and tell them the error
    if (username) == "":
        error = "Please complete the name field."
        return redirect("/?error=" + error)

    if (password) == "":
        error2 = "Please complete the password field."
        return redirect("/?error=" + error2)

    if (verify) == "":
        error3 = "Please verify the password you chose."
        return redirect("/?error=" + error3)
    #if the password and verify don't match, give an error
    if (password) != (verify):
        error3 = "The passwords you entered do not match"
        return redirect("/?error=" + error3)

    if len(password) < 4:
        error2 = "Your password is too short!"
        return redirect("/?error=" + error2)

    if len(password) > 20:
        error2 = "Your password is too long!"
        return redirect("/?error=" + error2)

    # if the e-mail isn't an e-mail, give an error
    emaillength=0
    periods=0
    atsigns=0
    for char in (email):
        emaillength +=1
        if char == '.':
            periods +=1
        if char == '@':
            atsigns +=1
    if email =="":
        return render_template('hello.html', username=username)
    elif (emaillength <4) or (emaillength > 20):
        error4 = "Please enter a valid e-mail address"
        return redirect("/?error=" + error4)
    elif periods != 1:
        error4 = "Please enter a valid e-mail address"
        return redirect("/?error=" + error4)
    elif atsigns !=1:
        error4 = "Please enter a valid e-mail address"
        return redirect("/?error=" + error4)
    

    return render_template('hello.html', username=username)


app.run()