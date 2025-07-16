from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/home')
def Home():
    return render_template('home.html')

@app.route('/newpage')
def NewPage():
    return render_template('newpage.html')

@app.route('/dashboard/<name>')
def Dashboard(name):
    if name == 'admin':
        return redirect(url_for('Home'))
    elif name == 'user':
        return redirect(url_for('NewPage'))
    elif name == 'index':
        return redirect(url_for('Index'))
    else:
        return "Invalid user type", 404
    
@app.route('/if')
def If_example():
    message = 'hello'
    return render_template('if.html', message=message)

@app.route('/for')
def for_example():
    courses = ['Python', 'Java', 'C++']
    return render_template('for_example.html', courses=courses)


# @app.route('/square', methods=['GET'])
# def square():
#     if request.method == 'GET':
#         if request.args.get("num")==None:
#             return render_template('square.html', result=None)
#         elif request.args.get("num")=="":
#             return f"Invalid Number", 400
#         else:
#             number = request.args.get("num")
#             square = int(number) ** 2
#             return render_template('result.html', num=number,  square=square )
@app.route('/square', methods=['POST','GET'])
def square():
    if request.method == 'POST':
        if request.form.get("num") == None:
            return render_template('square.html', result="Please enter a number")
        elif request.form.get("num") == "":
            return f"Please enter a number"
        else:
            number = request.form.get('num')
            square = int(number) ** 2
            return render_template('result.html', num = number, square=square)
    return render_template('square.html')


# @app.route('/feedback', methods=['GET', 'POST'])
# def feedback():
#      if request.method == 'POST':
#         if request.form.get("first") == None:
#             return render_template('feedbackform.html', result="Please enter your name !!")
#         elif request.form.get("feed") == "":
#             return f"Please Enter the Feedback !!"
#         else:
#             name = request.form.get('first')
#             feed = request.form.get('feed')
#             return render_template('submitted.html', first = name , feed=feed)
#      return render_template('feedbackform.html')

@app.route('/feedback', methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        if request.form.get("name") == None or request.form.get("feedback") == None:
            return render_template('feedbackform.html', result="Please fill in all fields")
        elif request.form.get("name") == "" or request.form.get("feedback") == "":
            return render_template('feedbackform.html', result="Please fill in all fields")
        else:
            name = request.form.get('name')
            feedback = request.form.get('feedback')
            return render_template('submitted.html', name=name, feedback=feedback)
    return render_template('feedbackform.html')

if __name__ == '__main__':
    app.run(debug=True)
