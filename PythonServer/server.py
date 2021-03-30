from flask import Flask
from flask import render_template
from data import db_session
from data.users import User

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
    db_session.global_init("db/users.db")
    db_sess = db_session.create_session()
    userCapt = User()
    userCapt.surname = "Scott"
    userCapt.name = "Ridley"
    userCapt.age = 21
    userCapt.position = "captain"
    userCapt.speciality = "research engineer"
    userCapt.address = "module_1"
    userCapt.email = "scott_chief@mars.org"
    user1 = User()
    user1.surname = "Alex"
    user1.name = "Punika"
    user1.age = 22
    user1.speciality = "research engineer"
    user1.email = "user1@mars.org"
    user2 = User()
    user2.surname = "Mattew"
    user2.name = "Uniklo"
    user2.age = 23
    user2.speciality = "research engineer"
    user2.email = "user2@mars.org"
    user3 = User()
    user3.surname = "Elton"
    user3.name = "Ferguson"
    user3.age = 20
    user3.speciality = "research geologist"
    user3.email = "user3@mars.org"
    db_sess.add(userCapt)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()
# app.run(port=8080, host='127.0.0.1')
