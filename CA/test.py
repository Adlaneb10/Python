import string
def dict_keystore():
    doc_count = 0
    dict = {}
    tag = "document"
    with open("ap_docs2.txt","r")as file:
        for line in file.readlines():
            splitline_lower = line.lower()
            splitline_split = splitline_lower.split()
            #print(splitline_split)
            for word in splitline_split:
                new_words = word.strip(string.punctuation)
                if tag in new_words:
                    doc_count += 1
                else:
                    try:
                        dict[new_words] += doc_count
                    except:
                        dict[new_words] = doc_count

    print(dict)
   #return dict

#print(dict)
dict_keystore()
