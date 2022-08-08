from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'unicorns'

# displays the number of times the client has visited this site
@app.route('/') 
def root():
    if 'visit' in session:
        session['visit'] += 1
    else:
        session['visit'] = 1
    return render_template('index.html')

# route that clears the session and redirects to the root route
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

# NINJA BONUS: +2 route that will increment the counter by 2
@app.route('/add_2') 
def add_2():
    if 'counter' in session:
        session['counter'] += 2
    else:
        session['counter'] = 2
    return redirect('/')

# NINJA BONUS: Reset button to reset the counter
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

#SENSEI BONUS: allows the user to specify the increment of the counter and have the counter increment accordingly
@app.route('/increment', methods=['POST'])
def increment_choice():
    increment_number = int(request.form['increment_number'])
    if 'counter' in session:
        session['counter'] += increment_number
    else:
        session['counter'] = increment_number
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)