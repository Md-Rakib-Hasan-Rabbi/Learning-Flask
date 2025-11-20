from flask import Flask, request,make_response

app = Flask(__name__)


@app.route('/Hello')
def hello():
    response = make_response('Rakib Hasan\n')
    response.status_code = 202
    response.headers['Content-type'] = 'application/octet-stream'
    return response
@app.route('/Name', methods=['POST'])
def name():
    if request.method == 'POST':
        return "You made a POST request\n"
    elif request.method == 'GET':
        return "You made a GET request\n"
    else:
        return "You will not see this"
    return "<h4>My name is Rakib</h4>"

@app.route('/Learning/<course>')
def learning(course):
    return f"I am learning {course} "

@app.route('/add/<int:num1>/<int:num2>') # This route is only for integer values
def add(num1 , num2):
    return f"{num1} + {num2} = {num1+num2}"

@app.route('/handle_url_parameters')
def handle_url_parameters():
    if 'username' in request.args and 'name' in  request.args:
        username = request.args.get('username')
        name = request.args.get('name')
        return f"Username is {username} and name is {name}"
    else:
        return "Some parameters are missing !"

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port = 5555 , debug=True)