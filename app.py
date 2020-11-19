from flask import Flask, render_template, jsonify, request
# import requests
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('mongodb://kandalf123:db7575@3.34.181.37', 27017)
db = client.STGpoke


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/battlelog')
def battle_log():
    return render_template('battlelog.html')

@app.route('/battlelog/save', methods=['POST'])
def save_result():
    index = request.form['index']
    my_first = request.form['my_first']
    my_second = request.form['my_second']
    my_third = request.form['my_third']
    opp_first = request.form['opp_first']
    opp_second = request.form['opp_second']
    opp_third = request.form['opp_third']
    result = request.form['result']
    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    star = db.battlelog.find_one({'name': name_receive})
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = star['like'] + 1
    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    # 참고: '$set' 활용하기!
    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})

@app.route('/battlelog/modify', methods=['GET'])
def modify_result():

@app.route('/battlelog/delete', methods=['GET'])
def delete_result():

@app.route('/types')
def types():
    return render_template('types.html')

@app.route('/pokedex')
def poke_dex():
    return render_template('pokedex.html')


# API 역할을 하는 부분
# @app.route('/api/list', methods=['GET'])
# def show_stars():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # stars = list(db.mystar.find({}, {'_id': False}).sort('like', -1))
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    # return jsonify({'result': 'success', 'stars_list': stars})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)