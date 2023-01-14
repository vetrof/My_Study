from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summ")
def summa():
    # return render_template("greet.html", name=request.args.get("name", "world"))
    n1 = request.args.get("num1", '0')
    n2 = request.args.get("num2", '0')
    s = int(n1) ** int(n2)

    return render_template("summ.html", summ_calc=s)

if __name__ == '__main__':
    app.run()