


while True:
	a=0
	b=0
	c=0
	d=0
	num =int(input("10 이상의숫자를 입력하세요 :  [Exit : 0]"))
	
	if num==0:
		break
	
	elif num<10:
		print("10 이상의 수를 입력하세요")
	
	else:
		for j in range(1,num+1):
			col=[]
			if j%3==0:
				col.append("Apple")
				a=a+1
			if j%4==0:
				col.append("Melon")
				b=b+1
			if j%5==0:
				col.append("Grape")
				c=c+1
			if j%8==0:
				col.append("StrawBerry")
				d=d+1
			if len(col)==0:
				print("%d"%j)
			else:
				print("%d."%j,col)

		print("==== << Fruit Count List >> ====")
		print("Apple:%5d회"%a)
		print("Melon:%5d회"%b)
		print("Grape:%5d회"%c)
		print("StrawBerry:%5d회"%d)
		print("-"*30)
	