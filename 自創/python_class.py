def read():
    total = 0
    with open('numbers') as f:
        for line in f:
            line=line.split()
            money = int(line[1]) * int(line[2])
            total=total+money
            print(line[0], money)
    print('all cost:', total)        
read()       