from flask import Flask
app=Flask(__name__)
###request object, response  object 
 

@app.route('/hello')
def hello():
 return "hello barch 4"

@app.route('/')
def hello_world():
 return 'hello, world'

if __name__=='__main__':
 app.run(debug=True)