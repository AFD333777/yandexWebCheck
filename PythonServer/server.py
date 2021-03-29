from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lyceum333'


@app.route('/index')
@app.route('/')
def missionName():
    return render_template('index.html')


@app.route('/list_prof/<typeList>')
def getSpec(typeList):
    param = {}
    param['typeList'] = typeList
    param['list_prof'] = ['Инженер-исследователь', 'Пилот', 'Врач', 'Строитель', 'Климатолог']

    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
