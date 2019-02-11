from flask import Flask, redirect, render_template, request, jsonify
from onoff import detect, on, off
app = Flask(__name__)

@app.route('/')
def main():
    '''PC = ""
    PC = detect()
    
    if PC == "on":
        return render_template("on.html")
    elif PC == "off":
        return render_template("off.html")
    elif PC == "WTF":
        return render_template("main.html")
        '''
    return render_template("settings.html")

@app.route('/background_process')
def background_process():
    power = request.args.get('power')
    if str(power) == 'on':
        Command = on()
        PC = detect()
        if Command == PC:
            return "done!"
        else:
            on()
            return "done!"
    else:
        off()
        return "done!"



if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080, debug = True,)