import favicon
import wikipedia
import youtubesearchpython as youtube

from duckduckgo_search import ddg

def search_wiki(query: str) -> list:
    result_list = []
    results = wikipedia.search(query=query, results=5)
    
    for result_name in results:
        try:
            result = wikipedia.page(result_name)

            result_list.append({
                'url': result.url,
                'title': result.title,
                'text': result.content[:100] + '...',
                'info': 'Wikipedia',
                'details': result.pageid,
                'image': './static/web.png'
            })

            try:
                for img in result.images:
                    if img.endswith('jpg') or img.endswith('png'):
                        result_list[-1]['image'] = img
                        break
            except:
                pass   

        except:
            pass

    return result_list

def search_youtube(query: str) -> list:
    result_list = []
    results = youtube.VideosSearch(query, limit=10).result()['result']
    
    for result in results:
        result_list.append({
            'url': f'https://youtu.be/{result["id"]}',
            'title': result['title'][:30] + '...' if len(result['title']) > 30 else '',
            'text': result["descriptionSnippet"][0]["text"][:100] + '...' if len(result["descriptionSnippet"][0]["text"]) > 100 else '',
            'info': result['channel']['name'],
            'details': f'{result["viewCount"]["short"]} • {result["publishedTime"]}',
            'image': result['thumbnails'][0]['url'],
        })

    return result_list

def search_ddg(query: str):
    result_list = []
    results = ddg(query, max_results=5)
    
    for result in results:
        result_list.append({
            'url': result['href'],
            'title': result['title'][:30] + '...' if len(result['title']) > 30 else '',
            'text': result["body"][:100] + '...' if len(result["body"]) > 100 else '',
            'info': result['href'].replace('://www.', '://').split('://')[1].split('.')[0],
            'details': 'found on DuckDuckGo',
            'image': './static/web.png',
        })

        # try:
        #     url = 'https://' + result_list[-1]['url'].split('//')[1].split('/')[0]
        #     favs = favicon.get(url)
        #     fav = favs[0].url
        #     result_list[-1]['image'] = fav
        # except:
        #     pass

    return result_list
