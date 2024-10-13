def tokeniser(text):
    text = text.lower()
    text = "".join(ch for ch in text if ch.isalnum() or ch.isspace())
    return text

class DocProcesser:
    def __init__(self, document):
        self.document = document
        self.vocab_list = self.vocab()
        

    def vocab(self):
        l1 = []
        srt = ""
        for i in self.document:
            if i != " ":
                srt += i
            else:
                l1.append(srt)
                srt = ""
            
        return l1
    
def unique_vocab(bow):
    return list(set(bow))

quary = input("Enter the para >> ")

d1 = tokeniser(quary)

d1_bow = DocProcesser(d1)
d1_u1 = unique_vocab(d1_bow.vocab())

dict1 = {}

len1 = len(d1_bow.vocab())
# print(len1)

#frequency of each word
for i in d1_u1:
    count = 0
    for j in d1_bow.vocab():
        if i == j:
            count += 1
    dict1[i] = count

dict2 = {}

print("The probabilty of each word occuring is:\n")
for i in dict1:
    dict2[i] = (dict1[i]/len1)
    
for i in dict2:
    print(f"{i} : {dict2[i]}")



