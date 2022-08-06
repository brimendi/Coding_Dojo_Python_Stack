from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>Welcome! Go to <a href=http://localhost:5000/play>Playground</a></h1>'

@app.route('/play')
def template():
    return render_template("index.html", number = 3, color = 'skyblue')

@app.route('/play/<number>')
def how_many_boxes(number):
    return render_template("index.html", number = int(number))

@app.route('/play/<number>/<color>')
def what_color(number, color):
    return render_template("index.html", number = int(number), color = color)


@app.errorhandler(404)
def error_page(e):
    return 'ERROR. The page you are trying to access does not exist. Go back to home and try again.'

if __name__=="__main__":
    app.run(debug=True)