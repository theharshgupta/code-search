from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    name = """from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    name = ""
    return render_template('hoe.html', name=name)

if __name__ == "__main__":
    app.run()
"""
    return render_template('hoe.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
