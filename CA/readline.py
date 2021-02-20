fopen = open('ap_docs2.txt','r')

fread = fopen.readlines()
file_doc_check = 0

x = "<NEW DOCUMENT>"

for line in fread:
    if x in line:
        print("Found")
        file_doc_check += 1
        break
print("word has been located in document",file_doc_check)
