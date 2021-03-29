from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lyceum333'


@app.route('/index')
@app.route('/')
def missionName():
    param = {}
    param['spec'] = ""
    return render_template('index.html', **param)


@app.route('/training/<string:spec>')
def getSpec(spec):
    param = {}
    param['spec'] = spec
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
