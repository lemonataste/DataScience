a=0
b=0
c=0
d=0
fuco=[]
answer = []
while True:
	
	num =int(input("10 이상의숫자를 입력하세요 :  [Exit : 0]"))
	
	if num>=10:
		for i in range (1,num+1):
			if i %3 == 0:
				answer.append("Apple")
			if i %4 == 0:
				answer.append("Melon")
			if i %5 == 0:
				answer.append("Grape")
			if i %8 == 0:
				answer.append("StrawBerry")
			fuco+=answer
			if len(answer) == 0:
				print("%d."%i)
			else:
				print("%d. "%i,str(answer))
			answer = []
		print("==<< Fruit Counter List >>==")
		print("Apple : %d회"%fuco.count('Apple'))
		print("Melon : %d회"%fuco.count('Melon'))
		print("Grape : %d회"%fuco.count('Grape'))
		print("StrawBerry : %d회"%fuco.count('StrawBerry'))

	elif (num==0):
		print("^ 종료")
		break
	else:
		print("^ 10이상의 숫자를 확인하세요")
		continue

		
	