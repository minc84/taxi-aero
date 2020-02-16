from flask import Flask
from config import Configuration
from flask import render_template
import os

app = Flask(__name__)
app.config.from_object(Configuration)

@app.route('/')
@app.route('/blog')
def index():
    return render_template('index.html')

@app.route('/aeroport-minsk2')
def aero2():
    return render_template('aeroport-minsk2.html')

@app.route('/arenda-micro')
def micro():
    return render_template('arenda-micro.html')

@app.route('/city')
def city():
    return render_template('city-blr.html')

@app.route('/arenda-bus')
def bus():
    return render_template('arenda-bus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/brest')
def brest():
    return render_template('brest.html')

@app.route('/grodno')
def grodno():
    return render_template('grodno.html')
    
@app.route('/vitebsk')
def vitebsk():
    return render_template('vitebsk.html')

@app.route('/gomel')
def gomel():
    return render_template('gomel.html')

@app.route('/mogilev')
def mogilev():
    return render_template('mogilev.html')


@app.route('/dududki')
def dududki():
    return render_template('dududki.html')

@app.route('/lida')
def lida():
    return render_template('lida.html')

@app.route('/pinsk')
def pinsk():
    return render_template('pinsk.html')

@app.route('/slon')
def slon():
    return render_template('slon.html')

@app.route('/stolin')
def stolin():
    return render_template('stolin.html')

@app.route('/volko')
def volko():
    return render_template('volko.html')

@app.route('/zlob')
def zlob():
    return render_template('zlob.html')


    
if __name__ == '__main__':
      app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))
