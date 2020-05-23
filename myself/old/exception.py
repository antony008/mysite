import random
def guess(): 
    a=random.randint(1,999)
    #print(a)#
    v=0
    m=10
    while True:
        try:
            x=int(input('Please input: '))
            if(x<a):
                print('too small')
                v=v+1
            if(x>a):
                print('too big')
                v=v+1
            if(x==a):
                print('hooray!')
                break
            if(v==m):
                print('Ha! You lose!') 
                break   
        except:
            print('please input a number')
            break

guess()        