
from flask import Flask, Response, render_template



server = Flask(__name__,template_folder='templates')
Index.register(server)

# @server.route('/')
# def index():
#     return render_template('index.html')


@server.route('/login',methods=['POST'])
def login():
    resp={'msg':'deu certo'}
    return resp,200


@server.route('/dashboard')
def dashboard():
    
    return render_template('dashboard.html')




if __name__ == "__main__":
    server.run(debug=True,host='0.0.0.0')
