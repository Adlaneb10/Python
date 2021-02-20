import string

def create_dict():
    fo = open("hare_and_tortoise.txt","r")
    fstop = open("stopwords.txt")
    stopwords = fstop.read().splitlines()

    dict = {}
    for line in fo:
        line = line.lower()
        line = line.split()
        #print(line)
        for w in line:
            if (w in stopwords):
                continue
            w = w.strip(string.punctuation)
            w = w.strip(string.whitespace)
            add_to_dict(w,dict)

    fo.close()
    return dict

def add_to_dict(word,dict):
    for key in dict.keys():
        if key == word:
            dict[key] = dict[key] + 1
            return dict
        else:
            dict[word] = 1
            return dict


def create_html(dict):
    html = '<!DOCTYPE html><html><head lang="en"><meta charset="UTF-8"><title>Tag Cloud Generator</title></head><body><div style="text-align: center; width: 15%; vertical-align:middle; font-family: arial; color: white;background-color:black; border:1px solid black">'
    count = 0
    for key in dict.keys():

        html += '<span style="font-size: '
        html += str(dict[key]*10)
        html += 'px"> '
        html += key
        html += '</span>'
        count += 1
        if count % 4 == 0:
            html += '<br>'

    html += '</div> </body> </html>'
    fo = open("output.html","w")
    fo.write(html)


dict = create_dict()
create_html(dict)

print(dict)

