import fileinput
import re
import glob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer
import stop_list


# concatenate all data in one file
file_list = glob.glob("data/*.jsonl")

with open('raw_dataset.jsonl', 'w') as file:
    input = fileinput.input(file_list)
    file.writelines(input)


# import raw_dataset.jsonl and convert to ideal data structure
detokenizer = TreebankWordDetokenizer()
stop_words = set(stopwords.words('english'))
with open("raw_dataset.jsonl") as raw_data:
    qna_lst = []      # create an empty list to store sets of original, q, and a [[original, q1, a1], ...]
    for line in raw_data:
        qna = []      # create an empty list to store the original, q, and a [original, q1, a1]

        # find query
        query = re.search('"questionText":', line)
        q_start = query.start()
        query = re.search('"answerOriginal"', line)
        q_end = query.start()
        qna.append(line[q_start:q_end].replace('\\n',''))      # now qna[0] becomes the original query
        qna[0] = qna[0][16:-3]     # remove questionText and unecessay punctuation

        # clean up the query
        clean_query = []
        query_tokens = nltk.word_tokenize(qna[0].lower())
        for word in query_tokens:
            if word not in stop_words:   
                if word not in stop_list.closed_class_stop_words:       
                    if not word.isnumeric():        
                        clean_query.append(word) 
        clean_query.pop(1)     # remove the first element, which is "questionText"
        qna.append(re.sub(r'[^\w\s]', '', detokenizer.detokenize(clean_query)))

        # find answer
        ans = re.search('"answerText":', line)
        a_start = ans.start()
        ans = re.search('"ID":', line)
        a_end = ans.start()
        qna.append(line[a_start:a_end].replace('\\n',''))
        qna[2] = qna[2][15:-3]     # remove answerText and unecessay punctuation

        qna_lst.append(qna)

# print(len(qna_lst))

