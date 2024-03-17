from flask import Flask, render_template, request
from yuri_manga_spreadsheet import spreadsheet_access
from readinglist import user_readinglist, websites

app = Flask(__name__)

genres = spreadsheet_access.get_all_genres()


@app.route('/')
def home():
    return _render_index()


@app.route('/search_manga', methods=['POST'])
def search_manga():
    query = request.form['manga_title']

    nsfw_enabled = request.form.get('nsfw_enabled', False)
    nsfw_enabled = nsfw_enabled == 'on'

    genre_filter = [genre for genre in genres if request.form.get(genre) == "on"]

    results = spreadsheet_access.search_by_name(query, genre_filter, nsfw_enabled)

    if results is None:
        return _render_index()
    return _render_index(mangas=results, search_query=query, nsfw_enabled=nsfw_enabled)


@app.route('/get_manga', methods=['POST'])
def get_manga():
    query = request.args.get('title')
    result = spreadsheet_access.get_by_name(query)

    if result is None:
        return _render_index()
    return _render_index(manga=result)


@app.route('/user-list')
def user_list():
    return render_template('manga_list.html')


@app.route('/user-list', methods=['POST'])
def load_user_list():
    username = request.form.get('username')
    source = request.form.get('source')
    source = websites.Websites.try_from(source)

    result = user_readinglist.get_user_list_from(username, source)
    print(result)

    return render_template('manga_list.html', user_readinglist=result)


def _render_index(**context):
    return render_template('index.html', genres=genres, **context)


def run():
    app.run(debug=True)
