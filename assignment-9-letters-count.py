sentence = input("Please enter a sentence to count letters : ")

sentence_list = list(sentence)

sentence_unique = set(list(sentence_list))

sentence_dict = {}

for i in sentence_unique:
    sentence_dict[i] = sentence_list.count(i)

print(sentence_dict)
