import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/songs', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        data = request.form
        result = add_song(data['artist'], data['title'], data['rating'])
        return jsonify(result)


@app.route('/api/songs/<id>', methods=['GET', 'PUT', 'DELETE'])
def resource():
    if request.method == 'GET':
        print('/GET')
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


# handlers

def add_song(artist, title, rating):
    try:
        with sqlite3.connect('songs.db') as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO songs (artist, title, rating) values (?, ?, ?);
                """, (artist, title, rating,))
            result = {'status': 1, 'message': 'Song Added'}
    except:
        result = {'status': 0, 'message': 'error'}
    return result


if __name__ == '__main__':
    app.debug = True
    app.run()
