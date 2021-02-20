import string
def create_dict():
    dict = {}
    i = 0
    word_tag = "new"
    new_doc_check = 0
    with open("ap_docs2.txt","r") as file:
        for line in file.readlines():
            splitline = line.lower()
            splitline = splitline.split()
            for word in splitline:
                new_words = word.strip(string.punctuation)
                dict[new_words] = new_doc_check
                if word_tag in word:
                    new_doc_check += 1

    #print(dict)
    return dict
def searcher(search_key):
    search_key = input("Enter the word you would like to find: \n")
    print(dict)
    return search_key



create_dict()
num = 0
searcher(num)
print(dict)
