from flask import Flask, render_template, request, redirect, url_for
from YuriMangaListAccess import SpreadSheetAccess
from ReadingList import UserReadingList
from ReadingList.Websites import Websites

app = Flask(__name__)


@app.route('/')
def home():
    return _render_index()


@app.route('/search_manga', methods=['POST'])
def search_manga():
    query = request.form['manga_title']

    nsfw_enabled = request.form.get('nsfw_enabled', False)
    nsfw_enabled = nsfw_enabled == 'on'

    results = SpreadSheetAccess.search_by_name(query, nsfw_enabled)

    if results is None:
        return render_template('index.html')

    genres = SpreadSheetAccess.get_all_genres()
    return _render_index(mangas=results, search_query=query, nsfw_enabled=nsfw_enabled)


@app.route('/get_manga', methods=['POST'])
def get_manga():
    query = request.args.get('title')
    result = SpreadSheetAccess.get_by_name(query)

    if result is None:
        return render_template('index.html')

    genres = SpreadSheetAccess.get_all_genres()
    return _render_index(manga=result)


@app.route('/manga-list')
def manga_list():
    return render_template('manga_list.html')


@app.route('/load-user-list')
def load_user_list():
    username = request.args.get('username')
    source = request.args.get('source')

    

    return render_template('manga_list.html')


def _render_index(**context):
    genres = SpreadSheetAccess.get_all_genres()
    return render_template('index.html', genres=genres, **context)


def run():
    app.run(debug=True)


if __name__ == '__main__':
    run()
