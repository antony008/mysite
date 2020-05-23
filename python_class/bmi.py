class Student:
    sid = 'unknown'
    name = 'unknown'
    gender = 'unknown'
    h = 0
    w = 0
    def __init__(self, sid, name, gender):
        self.sid = sid
        self.name = name
        self.gender = gender
    def height(self, h):
        self.h = h
    def weight(self,w):
        self.w = w
    def info(self):
        fmt = '{:10}{:10}{:10}{:10}{:10}'
        return fmt.format(self.sid, self.name, self.gender, self.h, self.w)


class BmiReport:
    name = 'unknown'
    sts = None
    def __init__(self, name):
        self.name = name
        self.sts = []
    def add(self, st):
        self.sts.append(st)
    def find(self, sid):
        for st in self.sts:
            if st.sid == sid:
                return st
        return None        
    def remove(self, sid):
        for st in self.sts:
            if st.sid == sid:
                self.sts.remove(st) 
    def update(self, sid, opts):
        st = self.find(sid)
        if st:
            if opts.get('name'):
                st.name = opts.get('name') 
            if opts.get('gender'):
                st.gender = opts.get('gender')  
            if opts.get('h'):
                st.h = opts.get('h')     
            if opts.get('w'):
                st.w = opts.get('w')                   
    def pr_report(self):
        for st in self.sts:
            print(st.info())
    def save_file(self, filename):
        with open(filename, 'w') as f:
            for st in self.sts:
                f.write(st.info() + '\n')  
    def read_file(self, filename): 
        with open(filename) as f:
            name = f.readline()
            self.name = name
            for line in f:
                line = line.strip()
                ts = line.split(',')
                st = Student(ts[0], ts[1], ts[2])
                st.height(float(ts[3]))
                st.weight(float(ts[4]))
                self.add(st)


def test():
    report = BmiReport('dummy')
    report.read_file('bmi.txt')
    report.remove('A03')
    report.update('A02', {'h': 172.0, 'w': 50.0})
    report.pr_report()
        #report.save_file('test.txt')
            

test()