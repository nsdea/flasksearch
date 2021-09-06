import searching

from waitress import serve
from flask import Flask, render_template, request

app = Flask(__name__)

def search(platform):
    platforms = {
        'yt': 'YouTube',
        'wiki': 'Wikipedia',
        'ddg': 'YouTube'
    }

    search_query = request.args['q']
    search_query = f'"{search_query}" • on {platforms[platform]} via FlaskSearch'

    if not search_query:
        return render_template('home.html')

    if platform == 'yt':
        search_results = searching.search_youtube(query=search_query)

    elif platform == 'wiki':
        search_results = searching.search_wiki(query=search_query)
    
    elif platform == 'ddg':
        search_results = searching.search_ddg(query=search_query)

    return search_query, search_results

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/yt')
def yt():
    search_query, search_results = search('yt')

    return render_template(
        'search.html',
        query=search_query,
        results=search_results
    )

@app.route('/ddg')
def ddg():
    search_query, search_results = search('ddg')

    return render_template(
        'search.html',
        query=search_query,
        results=search_results
    )

@app.route('/wiki')
def wiki():
    search_query, search_results = search('wiki')

    return render_template(
        'search.html',
        query=search_query,
        results=search_results
    )

if __name__ == '__main__':
    # serve(app, host='0.0.0.0', port=8080)
    app.run(host='0.0.0.0', port=8080)