import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/songs', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        all_songs = get_all_songs()
        return json.dumps(all_songs)
    elif request.method == 'POST':
        data = request.form
        result = add_song(data['artist'], data['title'], data['rating'])
        return jsonify(result)


@app.route('/api/songs/<id>', methods=['GET', 'PUT', 'DELETE'])
def resource(id):
    if request.method == 'GET':
        song = get_song(id)
        return json.dumps(song)
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


def get_all_songs():
    with sqlite3.connect('songs.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM songs ORDER BY id desc;")
        all_songs = cursor.fetchall()
        return all_songs


def get_song(id):
    with sqlite3.connect('songs.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM songs WHERE id =?', (id,))
        song = cursor.fetchone()
        return song


if __name__ == '__main__':
    app.debug = True
    app.run()
