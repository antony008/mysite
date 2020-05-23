class Student:
    def __init__(self, name, math, chi, eng, bio):
        self.name = name
        self.math = math
        self.chi = chi
        self.eng = eng
        self.bio = bio
    def info(self):
        return '{:<10}{:<10}{:<10}{:<10}{:<10}'.format(self.name, self.math, self.chi, self.eng, self.bio)


def get_math_avg(sts):
    return sum([st.math for st in sts]) / len(sts)
def get_chi_avg(sts):
    return sum([st.chi for st in sts]) / len(sts) 
def get_eng_avg(sts):
    return sum([st.eng for st in sts]) / len(sts)
def get_bio_avg(sts):
    return sum([st.bio for st in sts]) / len(sts)
def select_math_larger(sts, score):
    chosen = []
    for st in sts:
        if st.math > score:
            chosen.append(st)
    return chosen        
def pr_sts(sts):
    for st in sts:
        print(st.info())


def read_scores():
    with open('student.txt') as f:
        sts = []
        line = f.readline()
        for line in f:
            ts = line.strip().split()
            st = Student(ts[0], float(ts[1]), float(ts[2]), float(ts[3]), float(ts[4]))
            sts.append(st)
    math_avg = get_math_avg(sts)  
    chi_avg = get_chi_avg(sts)    
    eng_avg = get_eng_avg(sts)
    bio_avg = get_bio_avg(sts)
    fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}'
    print(fmt.format('avg:', math_avg, chi_avg, eng_avg, bio_avg))
    print()
    lst1 = select_math_larger(sts, 70)
    pr_sts(lst1)


read_scores()