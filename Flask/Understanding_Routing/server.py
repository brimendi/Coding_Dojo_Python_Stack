from flask import Flask  
app = Flask(__name__) 

@app.route('/')   #Create a root route ("/") that responds with "Hello World!"
def hello_world():         
    return 'Hello World!' 

@app.route('/dojo')  #Create a route that responds with "Dojo!"
def dojo():
    return 'Dojo'


@app.route('/say/hi/<name>') #Create a route that responds with "Hi" and whatever name is in the URL after /say/
def hi_name(name):
    print(name)               
    return 'Hi ' + name + "!"

@app.route('/say/<name>/<int:repeat>')   #Create a route that responds with the given word repeated as many times as specified in the URL
def name_repeated(name, repeat):          #Ensure the names provided in the 3rd task are strings
    repeat = (repeat)                    #ensure the 2nd element in the URL is an integer, and the 3rd element is a string
    str = name * repeat
    return str

@app.errorhandler(404)  #Ensure that if the user types in any route other than the ones specified, they receive an error message.
def error_page(e):
    return 'ERROR. The page you are trying to access does not exist. Go back to home and try again.'

if __name__=="__main__":      
    app.run(debug=True)