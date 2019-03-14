import string

#opens the file
with open('little_folks.txt', 'r') as f:
    text = f.read()
# print(text)

#make everything lowercase
text_lower = text.lower()
# print(text_lower)
#strip punctuation
text_punc = text_lower.strip()
# print(text_punc)

#split list into words
# text_list=text_punc.split()
# print(text_list)

#split list into word pairs
text_list=text_punc.split()
#make a dictionary with keys and value counts.  for each word, the key counter goes up one.

def word_counter(text):

    for word in text:
        if word in word_dict.keys():
            word_dict[word] += 1
                # emotion_dict[user_input] = emotion_dict[user_input] + 1
        else:
            word_dict[word] = 1
    return(word_dict)
word_dict = {}
# word_counter(text_list)



# word_dict is a dictionary where the key is the word and the value is the count
# words = list(word_dict.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])


#i want to pair every other word in my list of strings
