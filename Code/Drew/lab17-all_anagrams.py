def anagrams(word):
    if len(word) <=1:
        return word
    else:
        a_dict = []
        for x in anagrams(word[1:]):
            for i in range(len(word)):
                a_dict.append(x[:i] + word[0:1] + x[i:])
        return a_dict

user_string = input("Enter a word or phrase:\n")
print(anagrams(user_string))
