from flask import Flask, redirect, render_template, request, jsonify
from onoff import detect, on, off
app = Flask(__name__)

@app.route('/')
def main():
    PC = ""
    PC = detect()
    
    if PC == "on":
        return render_template("on.html")
    elif PC == "off":
        return render_template("off.html")
    elif PC == "WTF":
        return render_template("main.html")

@app.route('/background_process')
def background_process():
    power = request.args.get('power')
    if str(power) == 'on':
        Command = on()
        PC = detect()
        if Command == PC:
            return jsonify(result='Switching On The Computer')
        else:
            on()
            return jsonify(result='Switching On The Computer')
    else:
        off()
        return jsonify(result='Switching Off The Computer')



if __name__ == '__main__':
      app.run(ssl_context='adhoc')