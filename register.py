from flask import Flask, render_template, request
app = Flask(__name__)
dict = {}
@app.route("/")
def main():
    return render_template("register.html")
@app.route("/r")
def reg():
    return render_template("upload.html")

@app.route("/upl",methods = ['post'])
def upl():
    f = request.files['file']
    f.save('static/img/'+f.filename)
    return "<h1>SUCCESSS</h1>"
@app.route("/s", methods = ['POST'])
def succes():
    result = request.form
    file_Data = request.files['file']
    file_Data.save(file_Data.filename)
    # dict = result
    # return "<h1>MAIN PAGE</h1>"
    return render_template("check.html", ress = result)
# @app.route("/j")
# def reg():
@app.route("/v",methods = ['POST'])
def vi():
    return "just checking"
app.run(debug = True)