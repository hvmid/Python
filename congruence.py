def gcd(x, y):
	if y>x:
		return gcd(y, x)
	r = x%y
	if r==0:
		return y
	return gcd(y, x%y)		

def congruence(mod, c, a):
	if c>1:
		n=[]
		#find greatest common divisor and divide all values by it.
		d=gcd(c, mod)
		mod=int(mod/d)
		c=int(c/d)
		a=int(a/d)
		#set the algorithm to find 
		i=1
		while i<(mod*d):
			
			if ((c*i)-a)%mod==0:
				n.append(i)
				i=i+mod
			else:
				i+=1	
		print(n, "(Mod "+str(mod*d)+")")
				
	else:
		positive=[]
		neqative=[]
		b=a%mod
		c=b
		while b<100:
			b=b+mod
			positive.append(b)
			c=c-mod
			neqative.append(c)
		print(neqative)
		print(positive)			




print(congruence(5, 6, 2))