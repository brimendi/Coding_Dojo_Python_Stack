from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'bats'

@app.route('/') 
def root():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_languages'] = request.form.getlist('favorite_languages[]')
    session['comment'] = request.form['comment']
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)