def remove_o(number):
    count = 0
    i = 0
    words = ['Always','look','on','the','bright','side','of','life']
    for i in range(0,7):
        if 'o' in words[i][:1]:
            count += 1
            i += 1
    
    print(count)
    return number

num = 0
remove_o(num)

