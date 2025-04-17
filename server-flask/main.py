from flask import Flask
from flask-cors import CORS

app = Flask(__name__)
CORS(app) #ENABLE CORS ON ALL ROUTES


@app.route('/')
def home():
    return "¡El servidor Flask está funcionando!"

@app.route('/api/users')
def getusers():
    return{
        'users':['alice','bob','charlie']
    }

@app.route('/api/fruits')
def get_fruits():
    return['banan','aple','naranja']



if __name__ == '__main__':
    app.run(debug=True)