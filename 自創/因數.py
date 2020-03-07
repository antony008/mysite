"""caculate least common factor of num 1 and num 2"""
def least_common_factor(num_1,num_2):
	h=1
	q=[]
	count_number=0
	if(num_1>num_2):
		while(h<=num_2):
			j=num_1/h
			k=num_2/h
			if((j==int(j)) and (k==int(k))):
				q.append(h)
				count_number= count_number+1
			h=h+1
	else:
        while(h<=num_1):
            j=num_1/h
            k=num_2/h
            if((j==int(j)) and (k==int(k))):
                q.append(h)
                count_number= count_number+1
            h=h+1
	print(q)
	if(count_number==1):
		print('它們互質')
