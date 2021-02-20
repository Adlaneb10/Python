word = input("Enter a string: ")

while word != ".":
    if word[0] in "aeiou":
        new_word = word + "yay"
    
    else:
        consonants = ""
        index = 0

        while index < len(word) and word[index] not in "aeiou":
            consonants += word[index]
            index += 1
        
        new_word = word[index:] + consonants + "ay"


    print("New word is ", new_word)
    word = input("Please enter another string or . to end: ")