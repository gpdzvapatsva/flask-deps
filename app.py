from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ =='__main__':
    app.debug=True
    app.run()