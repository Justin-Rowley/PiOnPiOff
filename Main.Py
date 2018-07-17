from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def login():
    login = True
    return redirect("/main", code=302)

@app.route('/main')
def main():
    login = True
    if login == True:
        return render_template('main.html')
    else:
        return redirect("/")


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80, debug = True,)