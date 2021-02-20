import string

def list_store():
    word_tag = "<NEW DOCUMENT>"
    list_docs = {}
    doc_num = 0
    counter = 0
    with open("ap_docs.txt","r")as file:
        #content = file.read().splitlines()
        for line in file.readlines():
            if word_tag in line:

                counter += 1
            else:
                try:
                    list_docs[counter] += line
                except:
                    list_docs[counter] = line

    print(list_docs)


list_store()
