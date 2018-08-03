from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "29610CFB83FA70C360C77B07AAB215E240BBF836E34214E208E742AEB2DB681C"
import random 

@app.route('/')
def index():
# set up initial landing 
    if 'guessed' in session:
        sub = "display: none"
        rst = "display: show"
    else:
        sub = "display: show"
        rst = "display: none"
    x = ""
    if 'num' not in session:
        session['num'] = random.randrange(0,101)
    if 'win' not in session:
        session['color'] = "none"
    elif session['win'] == True:
        session['color'] = "Green"
    elif session['win'] == False:
        session['color'] = "Red"
    if 'old' in session: 
        x = "<p class = 'text'>Number is " + str(session['old']) + "!</p>"
    print(session)
    return render_template("index.html", num=x , clr = session['color'] ,sub=sub,rst=rst )

@app.route('/submitted', methods = ['POST'])
def evaluate():
    if int(request.form['guess']) == session['num']:
            session['win'] = True
    elif int(request.form['guess']) > session['num']:
            print("greater")
            session['win'] = False
    elif int(request.form['guess']) < session['num']:
            print("less")
            session['win'] = False
    session['guessed'] = 1            
    session['old'] = session['num']        
    session['num'] = random.randrange(0,101)
    print(session)
    return redirect('/') 

@app.route('/reset', methods = ['POST'])
def rangen():
    if 'win' in session:
        session.pop('win')
        session.pop('color')
    if 'guessed' in session:
       session.pop('guessed')
    sub = "display: show"    

    return redirect('/') 


app.run(debug=True)
