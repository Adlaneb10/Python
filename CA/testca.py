import string

new_doc_check = 0
dict = {}
bad_chars = string.whitespace + string.punctuation
word_tag =  "new"
i = 0


with open("ap_docs2.txt","r")as file:

    for line in file.readlines():
        #print((line))
        splitline_lower = line.lower()
        splitline_split = splitline_lower.split()
        for word in splitline_split:
            new_words = word.strip(string.punctuation)
            dict[new_words] = new_doc_check
            if word_tag in new_words:
               new_doc_check = new_doc_check + 1

        #remove all bad chars
print(dict)

search = "bright"


if search in dict:
    print("true")
else:
    print("false")





