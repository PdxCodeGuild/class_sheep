def palindrome_checker(user_input):
    list_of_letters = list(user_input)
    list_length = len(list_of_letters)
    palindrome_status = True
    current_index = 0
    for index in list_of_letters:
        if current_index <= ((list_length - current_index) - 1):
            current_index += 1
            if list_of_letters[current_index] != list_of_letters[(list_length - current_index) - 1]:
                palindrome_status = False
    return palindrome_status

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
