import fileinput
import re
import glob
import nltk
from nltk.corpus import stopwords
import stop_list
import QandA


# concatenate all data in one file
# file_list = glob.glob("data/*.jsonl")

# with open('raw_dataset.jsonl', 'w') as file:
#     input = fileinput.input(file_list)
#     file.writelines(input)


# import raw_dataset.jsonl and convert to ideal data structure
with open("test_dataset.jsonl") as raw_data:
    qna_lst = []
    for line in raw_data:
        # find query
        qna_set = QandA.QandA()
        query = re.search('"questionText":', line)
        q_start = query.start()
        query = re.search('"answerOriginal"', line)
        q_end = query.start()
        qna_set.query = line[q_start:q_end]
        # print(qna_set.query)
        

        # find answer
        ans = re.search('"answerText":', line)
        a_start = ans.start()
        ans = re.search('"ID":', line)
        a_end = ans.start()
        qna_set.ans = line[a_start:a_end]
        # print(qna_set.ans)

        qna_lst.append(qna_set)

print(qna_lst[1].query)
print(qna_lst[1].ans)

