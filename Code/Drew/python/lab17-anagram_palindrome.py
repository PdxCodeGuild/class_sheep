# Function to make a backward copy of string and compare with the original (as lists)
def palindrome_check(var):
    fwd = []
    bwd = []
    for i in range(len(var)):
        fwd.append(var[i])
        bwd.append(var[(len(var)-1)-i])
    return fwd == bwd

# Function to copy the string, sort both, and compare
def anagram_check(a, b):
    a = a.lower()
    b = b.lower()
    a = a.replace(' ','')
    b = b.replace(' ','')
    return ''.join(sorted(a)) == ''.join(sorted(b))

# Get user to choose between anagram and palindrome
func_choice = input("Type 'a' for anagram check, 'p' for palindrome check:\n")

# Apply the appropriate function:
if func_choice == 'a':
    user_string1 = input("Enter a word or phrase:\n")
    user_string2 = input("Enter another word or phrase:\n")
    if anagram_check(user_string1, user_string2) == True:
        print("These are anagrams.")
    else:
        print("These are not anagrams.")
if func_choice == 'p':
    user_string = input("Enter a string:\n")
    if palindrome_check(user_string) == True:
        print(f'"{user_string}" is a palindrome.')
    else:
        print(f'"{user_string}" is not a palindrome.')
