from flask import Flask, render_template, flash

app = Flask(__name__)


app.secret_key = 'pythonmach'
@app.route("/")
def index():
    flash('Python flask')
    return render_template("form.html")






if __name__ == '__main__':
    app.run(debug=True)
