from flask import *
import datetime
import os

app = Flask(__name__, static_folder='static')
img = os.path.join('static', 'Images')


@app.route("/index")
def hello_world():
    _width = 400
    _filename = "sg.png"
    fullpath = os.path.join(img, _filename)
    print(fullpath)
    return render_template('image_render.html', filename=_filename, image_file=fullpath, wdt=_width,
                           CopyrightYear=datetime.datetime.today().strftime("%d/%m/%Y %A"))


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route("/bye")
@make_bold
@make_underlined
def bye():
    return "Bye"


@app.route("/g/<name>")
def guess(name):
    import requests
    country = "TR"
    # response = requests.get(url="https://api.genderize.io?name="+name+"&country_id="+country)
    response = requests.get(f"https://api.genderize.io?name={name}&country_id={country}")
    data = response.json()
    _gender = data["gender"]
    names = ["C#", "Python", "Java"]
    return render_template('guess.html', gender=_gender, _name=name, _names=names)


@app.route("/image/<number>/<width>")
def show_image(number, width):
    _filename = None
    _width = width

    if number == "1":
        _filename = "sg.png"
    if number == "2":
        _filename = "vhd.jpg"

    fullpath = os.path.join(img, _filename)
    return render_template('image_render.html', filename=_filename, image_file=fullpath, wdt=_width)


@app.route("/name/<name>")
def show_name(name):
    return f"<h1>Ad: {name}</h1>"


@app.route("/message")
def write_message():
    return render_template("message.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"Name:{name}, Password: {password}"


if __name__ == "__main__":
    app.run(debug=False)
