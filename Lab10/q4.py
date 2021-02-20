def checker(number):
    words = ['o','He','is','over','there']
    count = 0
    i = 0
    for i in range(1,4):
        if words[0] in words[i][:1]:
            count += 1
            i += 1

    print(count)
    return number

num = 0
checker(num)
