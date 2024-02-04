from password_generator import PasswordGenerator
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    pwo = PasswordGenerator()
    
    pwo.minlen = int(request.form['minlen'])
    pwo.maxlen = int(request.form['maxlen'])
    pwo.minuchars = int(request.form['minuchars'])
    pwo.minlchars = int(request.form['minlchars'])
    pwo.minnumbers = int(request.form['minnumbers'])
    pwo.minschars = int(request.form['minschars'])

    password = pwo.generate()
    
    return render_template('result.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
