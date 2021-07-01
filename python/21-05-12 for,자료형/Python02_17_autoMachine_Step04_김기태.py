
menu = ["orange", "strawberry", "peach", "mango", "grape", "종료"]
price = [1000,2500,1500,2000,2000]

while True:
	print("****** 홍익 대학교 과일 판매머신 V03 ******")
	for num in range(6):
		print("%d.%s"%(num,menu[1]))
	print("=======================================")
	num = int(input("구매 번호를 입력하세요 ( 1~6 )"))
	if num == 6:
		print("프로그램을 종료합니다")
		break
	elif num > 6 or num ==0:
		print("잘못된 숫자입니다. 다시 입력해주세요")
	else:
		print(menu[num-1], "는", price[num-1], "원 입니다.\n") 