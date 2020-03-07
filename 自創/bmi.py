def BMI():
  with open('bmi.txt') as f:
    a = f.readline()
    k=a.split()
    a,b,c,d=k[0],k[1],k[2],k[3]
    fmt=' {:^8}{:^8}{:^8}{:^8}{:>6}{:^10}'.format(a,b,c,d,'BMI','Memo')
    print(fmt)
    print('_ '*25)
    for line in f:  
        r=line.split()
        a,b,c,d=r[0],r[1],int(r[2]),float(r[3])
        bmi=round(d/(c/100)**2,2)
        if(bmi<18.5):
            t='體重過輕'
        if(18.5<=bmi<22.9):
            t='正常範圍'
        if(22.9<=bmi<27):
            t='過    重'
        if(27<=bmi<30):
            t='輕度肥胖'
        if(30<=bmi<35):
            t='中度肥胖'
        if(bmi>=35):
            t='重度肥胖'
        fmt2='{:>7}{:^11}{:>4}{:>9}{:>9}{:^8}'.format(a,b,c,d,bmi,t)
        print(fmt2)
BMI()