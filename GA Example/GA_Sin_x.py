import numpy as np
import math
import random

def sort_by_fitness(matrix,column_no):
	#sorting the matrix based on best fit
	ind=np.argsort(matrix[:,column_no])
	matrix=matrix[ind[::-1]]
	return matrix

def col_create(matrix):
	#Creating columns for bin2int, x in pi range, sin of x
	bin_int=[]
	in_pi_range=[]
	sin_value=[]

	for row in matrix:
		matri="".join(list(map(str,(row))))
		matri=int(matri,2)
		in_pi=((matri/255)*2*math.pi)-math.pi
		sin=math.sin(in_pi)
		bin_int.append([matri])
		in_pi_range.append([in_pi])
		sin_value.append([sin])

	#adding column to the original matrix
	matrix=np.hstack((matrix,bin_int,in_pi_range,sin_value))
	return (sort_by_fitness(matrix,10))

def mutate(matrix):
	row=random.randint(0,17)
	col=random.randint(0,7)	
	if float(matrix[row,col])==1.0:
		matrix[row,col]=0.0
	else:
		matrix[row,col]=1.0
	return matrix


#Random matrix of zero and one created
size=10
popu=np.random.randint(0,2,(size,8))

popu=col_create(popu)
count=0
runtime=0

while count<=100:
	pre_mut=popu[0,9]

	parent=popu[0:8,0:8]
	child=[]
	length=np.size(parent,0)
	while length>0:
		f_pos=random.randint(0,length-1)
		father=parent[f_pos,]
		father=father.astype(int)
		father="".join(list(map(str,(father))))
		m_pos=random.randint(0,length-1)
		while True:
			m_pos=random.randint(0,length-1)
			mother=parent[m_pos,]
			mother=mother.astype(int)
			mother="".join(list(map(str,(mother))))
			if m_pos!=f_pos:
				break

		position=random.randint(0,7)
		
		temp=father[position:]
		father=father[:position]+mother[position:]
		mother=mother[:position]+temp

		father=[int(elem) for elem in father]
		mother=[int(elem) for elem in mother]

		child.append(father)
		child.append(mother)

		if f_pos>m_pos:
			parent=np.delete(parent,(f_pos), axis=0)
			parent=np.delete(parent,(m_pos), axis=0)
		else:
			parent=np.delete(parent,(m_pos), axis=0)
			parent=np.delete(parent,(f_pos), axis=0)
		
		length=np.size(parent,0)
		
	child=np.array(child)
	child=col_create(child)

	popu=np.vstack((popu,child))
	# mutation
	popu=mutate(popu)
	popu=sort_by_fitness(popu,size)

	# Survival of fittest
	popu=popu[:size,:]

	post_mut=popu[0,9]

	if post_mut==pre_mut:
		count+=1
	runtime+=1
for row in popu:
	print(' '.join([str(elem) for elem in row]))

print("\n")
print(post_mut)

print("\n")
print(runtime)

# 1.58927628358-192 // 1.5646363412-191
