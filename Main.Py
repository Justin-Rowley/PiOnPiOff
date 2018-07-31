from flask import Flask, redirect, render_template, request
from onoff import detect, on, off
import jsonify
app = Flask(__name__)

@app.route('/')
def main():
    PC = ""
    PC = detect()
    if request.method == 'POST':
        button = request.arg.get("Power")
        if button == 0:
            off()
            return jsonify(status="success")
        elif button == 1:
            on()
            return jsonify(status="success")
    if PC == "on":
        return render_template("on.html")
    elif PC == "off":
        return render_template("off.html")
    elif PC == "WTF":
        return render_template("main.html")

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80, debug = True,)