
while True:
	print("****** 홍익 대학교 과일 판매머신 V01 ******")
	print("1. orange                :  1000 원")
	print("2. strawberry            :  2500 원")
	print("3. peach                 :  1500 원")
	print("4. mango                 :  2000 원")
	print("5. grape                 :  2000 원")
	print("=======================================")
	num = int(input("구매 번호를 입력하세요 ( 1~5 )"))
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
	