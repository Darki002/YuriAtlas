from flask import Flask, render_template, request

from yuri_manga_processing.manga_source import MangaSource
from yuri_manga_spreadsheet import spreadsheet_access
from yuri_manga_processing.recommendation_system import main as rec_system
from readinglist import user_readinglist, websites, my_anime_list

app = Flask(__name__)

genres = spreadsheet_access.get_all_genres()


@app.route('/')
def home():
    return _render_index()


@app.route('/manga')
def manga():

    source = request.args.get('source')
    manga_id = request.args.get('id')

    print(f"Source: {source}, ID: {manga_id}")

    if source.isdigit() is False:
        return _render_index()

    source = int(source)
    match source:
        case MangaSource.SpreadSheet.value:
            result = spreadsheet_access.get_by_id(manga_id)
            if result is None:
                return _render_index()
            return render_template('manga.html', manga=result)

        case MangaSource.MyAnimeList.value:
            result = my_anime_list.get_manga(manga_id)
            if result is None:
                return _render_index()
            return render_template('manga.html', manga=result[0], image_url=result[1])

        case _:
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


@app.route('/recommendation', methods=['GET'])
def recommendation():
    return render_template('rec_system/index.html')


@app.route('/recommendation', methods=['POST'])
def recommendation_post():
    user_name = request.form.get('username')

    source = request.form.get('source')
    source = websites.Websites.try_from(source)

    rec = rec_system.recommend_for(user_name, source)

    return render_template('rec_system/recommendation.html', rec=rec, username=user_name)


def run():
    app.run(debug=True)
