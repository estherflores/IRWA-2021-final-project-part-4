import random

from myapp.core.utils import get_random_date
import text_processing
import index_ranking

def build_demo_data():
    """
    Helper method, just to demo the app
    :return: a list of demo docs sorted by ranking
    """
    samples = ["Messier 81", "StarBurst", "Black Eye", "Cosmos Redshift", "Sombrero", "Hoags Object",
            "Andromeda", "Pinwheel", "Cartwheel",
            "Mayall's Object", "Milky Way", "IC 1101", "Messier 87", "Ring Nebular", "Centarus A", "Whirlpool",
            "Canis Major Overdensity", "Virgo Stellar Stream"]

    res = []
    for index, item in enumerate(samples):
        res.append(DocumentInfo(item, (item + " ") * 5, get_random_date(),
                                "doc_details?id={}&param1=1&param2=2".format(index), random.random()))
    # simulate sort by ranking
    res.sort(key=lambda doc: doc.ranking, reverse=True)
    print(res)
    return res


class SearchEngine:
    """educational search engine"""
    i = 12345

    def search(self, search_query):
        print("Search query:", search_query)
        results= []
       # index, tf, df, idf = index_ranking.create_index_tfidf(text_processing.all_tweets, num_documents = len(text_processing.all_tweets))
       # results = index_ranking.search_tf_idf(search_query, index)
        ##### your code here #####
        results = build_demo_data()  # replace with call to search algorithm
        ##### your code here #####

        return results


class DocumentInfo:
    def __init__(self, title, description, doc_date, url, ranking):
        self.title = title
        self.description = description
        self.doc_date = doc_date
        self.url = url
        self.ranking = ranking
