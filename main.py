from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/api/v1/<station>/<date>")
def temp(station , date):
    temp = 23
    return {"station" : station ,
            "date" : date ,
            "temperature" : 23}

if __name__ == "__main__":
    app.run(debug=True)
