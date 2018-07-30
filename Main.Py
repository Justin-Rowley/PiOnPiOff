from flask import Flask, redirect, render_template
from onoff import detect, on, off
app = Flask(__name__)

@app.route('/')
def main():
    PC = ""
    PC = detect()
    if PC == "on":
        render_template(on.html)
    elif PC == "off":
        render_template(off.html)
    elif PC == "WTF":
        render_template(main.html)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80, debug = True,)