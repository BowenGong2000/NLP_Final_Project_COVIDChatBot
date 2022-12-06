class QandA:
    origin_que = ""     # original query
    que = []            # tokennized clean query, with repetition
    ans = ""            # answer
    tfidf = {}          # tfidf for each word, the key is the word, no repetition

    def __init__(self):
        self.origin_que = ""
        self.que = [] 
        self.ans = ""
        self.tfidf = {}
