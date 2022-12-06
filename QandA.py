class QandA:
    origin_que = ""         # original query
    que = []                # tokennized clean query, with repetition
    ans = ""                # answer
    tfidf = {}              # dictionary, stores tfidf for each word, the key is the word, no repetition

    def __init__(self, origin_que, que, ans):
        self.origin_que = origin_que
        self.que = que
        self.ans = ans
        self.tfidf = {}

