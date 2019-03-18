#Lab 13: Rot 13/Cipher

#Objectives:
#1.get a word as a string
#2.convert letters to numbers
#3.shift numbers to new alphabet sequence
#4.convert numbers back into letters
#5.Combine the letters back together


#version 1
def cipher(input):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated = 'nopqrstuvwxyzabcdefghijklm'
    output = '' #open string waiting for output, empty string is like the pan waiting for the cake batter to go in it
    for letter in input:
        index = alphabet.find(letter) #find the index/number for each letter in the input word
        output += rotated[index] #gets the rotated alphabet index for the user input word

    print(output)

user_input = (input("What do you want to encrypt?: "))

cipher(user_input)


#version 2
def cipher(input, shifted_number):

#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

    output = '' #open string waiting for output, empty string is like the pan waiting for the cake batter to go in it
    for letter in input: #turn letters into numbers
        index = alphabet.find(letter) #find the number/index of each letter in the input word
        index += shifted_number #adds the number of letters shifted with the original letters index

        if index >= len(alphabet): #ie if the number is greater than 26
            index -= len(alphabet) #subtract the index number by the length of the alphabet (26)
        output += alphabet[index] #add the new shifted number back to each letter's index in the original alphabet

    return output

user_input = (input("What do you want to encrypt?: "))
user_input2 = int(input("How many digits do you want to shift the alphabet by?: "))

string = cipher(user_input, user_input2)

print(string)
