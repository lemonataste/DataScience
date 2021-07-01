
menu = ["orange", "strawberry", "peach", "mango", "grape", "종료"]

while True:
	print("****** 홍익 대학교 과일 판매머신 V02 ******")
	for num in range(6):
		print(num+1,menu[num])
	print("=======================================")
	num = int(input("구매 번호를 입력하세요 ( 1~6 )"))
	if num == 1:
			print("orange 1000원 입니다.\n") 
	elif num == 2:
			print("strawberry 2500원 입니다.\n") 
	elif num == 3:
			print("peach  1500원 입니다.\n")
	elif num == 4:
			print("mango 2000원 입니다.\n")
	elif num == 5:
			print("grape 2000원 입니다.\n")
	else:
			print("종료 되었습니다.")
			break
		
	