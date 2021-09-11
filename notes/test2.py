def add():
    from random import randint
    a = randint(1, 5)
    b = randint(1, 5)
    c = a + b
    print (a,  '+',  b)
    d = int(input('What\'s the sum?'))
    while d != c:
        print ('Wrong, try again!')
        print (a,  '+',  b,' ? ')
        d = int(input())
    else:
        print ("Correct!")


while True:
    add()
    if input('Continue (Y/N) ? ') == 'N':
        break