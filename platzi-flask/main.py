from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    #return 'Hello World Platzi, tu IP es {}'.format(user_ip)
    return render_template('hello.html', user_ip=user_ip)

    #Siempre correr set FLASK_APP=main.py en la terminal para evitar el erro de varialbes
# if __name__ == '__main__':
#     app.run(debug=True)