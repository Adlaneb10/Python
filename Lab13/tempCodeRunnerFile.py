import string
file_open = ("ap_docs2.txt")
dict = {}
new_doc_check = 1
#lines = file_open
#np = 0
#i = 0
for line in file_open:
    if "<NEW DOCUMENT>" in line:
        print("This is document {}",new_doc_check.format())
        new_doc_check += 1