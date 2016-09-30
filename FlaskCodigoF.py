from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!a'


#localhost:5000/params?params1=Eduardo_Ismael
@app.route('/params')
def webos():
    param = request.args.get("params1", "no coincide este parametro")
    param2 = request.args.get("param2","no coincide" )
    return 'params! {}, {}'.format(param, param2)


if __name__ == '__main__':
    app.run(debug=True)
