def least_common_multiple(num_1,num_2):
	h=1
	k=1
	q=[]
	a=[]
	while(h<=num_2):
		o=num_1*h
		q.append(o)
		h=h+1
	while(k<=num_1):
		m=num_2*k
		a.append(m)
		k=k+1
	q_set=set(q)     
	a_set=set(a)       
	b=q_set & a_set               
	s=min(b)                     
	print(s)
