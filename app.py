from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/main")
def msg():
    return "<h1>YE DYNAMIC MESSAGE HAI REDIRECT KRKE</h1>"

# @app.route("/h")
# def h():
#     return "<h1>HOME PAGE IS HERE</h1>"
app.run(debug = True)
