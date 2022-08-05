from flask import Flask  
app = Flask(__name__) 

@app.route('/')          
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')
def dojo():
    return 'Dojo'


@app.route('/say/hi/<name>')
def hi_name(name):
    print(name)
    return 'Hi ' + name + "!"

@app.route('/say/<name>/<int:repeat>')
def name_repeated(name, repeat):
    repeat = (repeat)
    str = name * repeat
    return str

@app.errorhandler(404)
def error_page(e):
    return 'ERROR. The page you are trying to access does not exist. Go back to home and try again.'

if __name__=="__main__":      
    app.run(debug=True)