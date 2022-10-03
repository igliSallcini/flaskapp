from crypt import methods
from curses.ascii import isupper
from distutils.log import debug
from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)

app.secret_key = "12345abcde"


@app.route("/set-cookie")
def setCookie():
    expire = 60*60*24*20
    resp = make_response(render_template("cookies.html"))
    resp.set_cookie("email", "iglisallcini@gmail.com", expire)
    return resp


@app.route("/get-cookie")
def getCookie():
    return request.cookies.get("email ")

# @app.route("/set-session")
# def setSession():
#     session['username'] = "iglisallcini"
#     return "Session was set successfully"

# @app.route("/get-session")
# def getSession():
#     return render_template("session.html")
    # return session.get("username")



# @app.route("/", methods=['GET', 'POST'])
# def home():
#     if request.method == "POST":
#         username = request.form['username']
#         password = request.form['password']
#         if validator_username (username) is True:
#             return "Username duhet te permbaje shkronja te vogla"
#         if validator_password(password):
#             return "Your username is :" + username + " Your password is :" + password
#         return "password duhet te jete me shume se 6 karaktere"

#     return render_template ("form.html")

# def validator_username(username):
#         return (not username.lower() == username)

# def validator_password(password):
#     return (len(password)>6) and (type(password) is str)


@app.route("/")
def indexx():
    return render_template("form.html")

@app.route("/form/action", methods=["POST"])
def form_action():
    username = request.form['username']
    password = request.form['password']
    return "Your username is :" + username + " Your password is :" + password
    # username = request.args.get ('username')
    # password = request.args.get ('password')
    # return "Your username is :" + username + " Your password is :" + password
    # return request.args.get("username")
    # return render_template ("010101.html")


# @app.route ("/<string:article_id>")
# def index(article_id):
#     article = None
#     posts = {
#         "1": {
#             'title' : 'Lorem Ipsum Title',
#             'image' : 'https://peoplescience.maritz.com/-/media/Maritz/Project/PeopleScience/Articles/sample_size.ashx?h=900&w=1200&la=en&hash=A1D4DAFBD0685E53F9C00536FCD8EE47CE892206',
#             'content' : "1 - Lorem ipsum dolor sit amet. Aut voluptates atque est sunt quas et aliquam aperiam qui blanditiis modi qui nesciunt eius qui molestiae aperiam.",
#         },
#         "2": {
#             'title' : 'Lorem Ipsum Title - 2',
#             'image' : 'https://www.viewbug.com/media/mediafiles/2016/05/28/66284132_medium.jpg',
#             'content' : "2 - Lorem ipsum dolor sit amet. Aut voluptates atque est sunt quas et aliquam aperiam qui blanditiis modi qui nesciunt eius qui molestiae aperiam.",
#         }

#     }
#     if article_id in posts.keys():
#         article = posts[article_id]
#         return render_template("index.html", indx=article_id, article=article )
#     else:
#         return render_template("not_found.html", indx=article_id, nr=len(posts))

@app.route ("/not_found.html")
def not_found(article_id):
    return render_template("not_found.html", indx=article_id)

if __name__== '__main__':
    app.run(debug = True)