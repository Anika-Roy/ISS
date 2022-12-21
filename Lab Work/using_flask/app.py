from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'hello :)'

@app.route('/calc/sum', methods=['POST', 'GET'])
def num1_plus_num2():
    if request.method == 'GET':
        return render_template('num_in.html')
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        if(str. isdecimal(num1)==False or str. isdecimal(num2)==False):
            return 'enter only integers'
        num1=int(num1)
        num2=int(num2)
        return '%s' % (num1+num2)

@app.route('/calc/multiply', methods=['POST', 'GET'])
def num1xnum2():
    if request.method == 'GET':
        return render_template('num_in_mul.html')
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        if(str. isdecimal(num1)==False or str. isdecimal(num2)==False):
            return 'enter only integers'
        num1=int(num1)
        num2=int(num2)
        return '%s' % (num1*num2)

if __name__ == '__main__':
    app.run(debug=True)