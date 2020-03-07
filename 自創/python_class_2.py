
def read():
    cnt=int(input())
    i=1
    for count in range(cnt):
        cnt_2=int(input())
        print('input',i,': ',cnt_2,' sprt',i,': ',round(cnt_2**0.5*1000)/1000)
        i=i+1
read()