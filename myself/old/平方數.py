def prove(num):
     a=1
     b=1
     c=1
     d=[]
     """print(a)"""
     for count in range(num):
        while((b<=a) and (c<=a)):
                     """平方"""
                     """print('a=',a)
                     print('b=',b)
                     print('c=',c)"""
                     j=b*b
                     k=c*c
                     n=a*a
                     if((j+k)==n):
                             d.append(n)
                             d.append(j)
                             d.append(k)
                     c=c+1
                     if(c==(a+1)):
                             b=b+1
                             c=b
             a=a+1
             b=1
             c=1
     print(d)
