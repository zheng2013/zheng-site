from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def a():
    return render_template('1.html')
@app.route('/saolei')
def b():
    return render_template('2.html')
@app.route('/daimayu')
def c():
    return render_template('3.html')
@app.route('/tanchishe')
def d():
    return render_template('4.html')
if __name__ == '__main__':
    app.run(port=5010, debug=True)
