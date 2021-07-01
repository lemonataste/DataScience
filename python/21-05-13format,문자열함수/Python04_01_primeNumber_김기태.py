


while True:
	
	num =int(input("숫자를 입력하세요 :  [Exit : 0]"))
	
	if num==0:
		break
	
	elif num<20:
		print("20 이상의 수를 입력하세요")
	
	else:
		print("1.소수X")
		for j in range(2,num+1):
			a=0
			for i in range(2,j):
				if j % i==0:
					a=1
			if a==0:
				print("%d.소수O"%j)
			else:
				print("%d.소수X"%j)
			