def palindrome_checker(user_input):
    half_length = len(user_input) // 2
    for index in range(half_length):
        if user_input[index] != user_input[len(user_input) - index - 1]:
            return False
        else:
            return True

user_input = input("Enter a word to check if it's a palindrome >")
if palindrome_checker(user_input):
    print("Palindrome!")
else:
    print("Not a palindrome.")

def anagram_checker(user_input1, user_input2):
    user_input1 = user_input1.lower()
    user_input2 = user_input2.lower()
    user_input1 = user_input1.replace(' ', '')
    user_input2 = user_input2.replace(' ', '')
    word1_list = list(user_input1)
    word2_list = list(user_input2)
    word1_list.sort()
    word2_list.sort()
    if word1_list == word2_list:
        return "Anagram!"
    else:
        return "Not an anagram!"

user_input1 = input("Welcome to the anagram checker. Type a word >")
user_input2 = input("Type another word >")

print(anagram_checker(user_input1, user_input2))
