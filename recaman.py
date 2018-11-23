
def recaman(num):

	sequence=[]
	count=0

	for i in range(0, num):
		if not sequence:
			sequence.append(0)
			count+=1
		elif (sequence[-1]-count) in sequence or sequence[-1]-count<0:
			sequence.append(sequence[-1]+count)
			count+=1
		else:		
			sequence.append(sequence[-1]-count)
			count+=1
	print(sequence)		


print(recaman(50))