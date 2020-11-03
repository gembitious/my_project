from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# client = MongoClient('localhost', 27017)
# db = client.pokemonDB


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/types')
def types():
    return render_template('types.html')


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