from flask import Flask, render_template, request
from YuriMangaListAccess import SpreadSheetAccess

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search_manga', methods=['POST'])
def search_manga():
    query = request.form['manga_title']
    results = SpreadSheetAccess.get_by_name(query)

    if results is None:
        return render_template('index.html')

    return render_template('index.html', manga=results)


def run():
    app.run(debug=True)


if __name__ == '__main__':
    run()
