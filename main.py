import nltk
import math
import numpy as np
import pandas as pd
from numpy.linalg import norm
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer
from operator import itemgetter
import standardize
import QandA

qna_lst = standardize.qna_lst
detokenizer = TreebankWordDetokenizer()
stop_words = set(stopwords.words('english'))

def make_QandA_lst(qna_lst):
    QandA_lst = []     # a list stores all class variable of QandA
    for qna in qna_lst:
        new_QandA = QandA.QandA(qna[0], nltk.word_tokenize(qna[1]), qna[2])
        QandA_lst.append(new_QandA)
        
    return QandA_lst

def count_occur(QandA_lst):     # count the occurance of certain word in all query
        occur = {}
        for qna in QandA_lst:
            word_lst = set(qna.que)     # remove repetition
            for word in word_lst:
                if not (word in occur):
                    occur[word] = 1
                else:
                    occur[word] = occur[word] + 1
        return occur

def get_tfidf(QandA_lst):
    for qna in QandA_lst:
        for word in qna.que:
            tf = qna.que.count(word)
            tf = tf/len(qna.que)
            idf = math.log((len(QandA_lst) / occur[word]))
            qna.tfidf[word]= tf*idf 

def get_input_tfidf(input_query):
    # for qna in QandA_lst:
    tfidf = {}
    for word in input_query:
        tf = input_query.count(word)
        tf = tf/len(input_query)
        idf = 1
        tfidf[word]= tf*idf 

    return tfidf

def get_similarity(input_tfidf, tfidf):
    vec1 = np.array(input_tfidf)
    vec2 = np.array(tfidf)
    if not vec1.any() or not vec2.any():
        return 0
    simi = np.dot(vec1,vec2)/(norm(vec1)*norm(vec2))

    return simi


# preparation before input 
QandA_lst = make_QandA_lst(qna_lst)     # the list stores all class variable of QandA
occur = count_occur(QandA_lst)
get_tfidf(QandA_lst)
again = "yes"
answered = "yes"
print("<========== Welcome to the COVID19 Chatbot!!! ==========>\n")

while (again=="yes"):
    if answered !="yes":
        input_query = input("<========== Please re-enter your question. Please be more specific this time: ==========>\n")
    else:
        input_query = input("<========== Please enter your question. Please make sure your spellings are correct: ==========>\n")

    input_tokens = nltk.word_tokenize(input_query.lower())
    # remove stopwords
    clean_tokens = []
    for word in input_tokens:
        if word not in stop_words:       
                    if not word.isnumeric():        
                        clean_tokens.append(word) 

    input_tfidf = get_input_tfidf(clean_tokens)

    rank_lst = []
    for qna in QandA_lst:
        simi_tfidf = []
        for key in input_tfidf:
            if key in qna.que:
                simi_tfidf.append(qna.tfidf[key])
            else:
                simi_tfidf.append(0)

        simi = get_similarity(list(input_tfidf.values()), simi_tfidf)
        output = [simi, qna.origin_que, qna.ans]
        rank_lst.append(output)
        rank_lst = sorted(rank_lst, key=itemgetter(0))     # the last one will be the optimal one 
        original_quest = sorted(rank_lst, key=itemgetter(0))[-1][1]
        answer = sorted(rank_lst, key=itemgetter(0))[-1][2]

    print(original_quest)
    print(answer)

    answered = input("<========== Does this answer addresses you question? (yes/no) ==========>\n")
    if answered =="yes":
        again = input("<========== Do you have other question? (yes/no) ==========>\n")

print("<========== Thank you for using our Chatbot, have a nice day!!! ==========>\n")






