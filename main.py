import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
import standardize
import QandA

qna_lst = standardize.qna_lst
detokenizer = TreebankWordDetokenizer()

def make_QandA_lst(qna_lst):
    QandA_lst = []     # a list store all class variable of QandA
    for qna in qna_lst:
        new_QandA = QandA.QandA(qna[0], nltk.word_tokenize(qna[1]), qna[2])
        QandA_lst.append(new_QandA)
    


make_QandA_lst(qna_lst)