
menu = ["orange", "strawberry", "peach", "mango", "grape"]
price = [1000,2500,1500,2000,2000,0]

while True:
	print("****** 홍익 대학교 과일 판매머신 V04 ******")
	for num in range(5):
		print("%d번 %-10s %4d원 입니다."%(num+1,menu[num],price[num]))
	print("=======================================")
	num1 = int(input("구매 번호를 입력하세요 ( 1~5 )"))

	if num > 5 or num ==0:
		print("잘못된 숫자입니다. 다시 입력해주세요")
	else:
		print(menu[num1-1], "는", price[num1-1], "원 입니다.\n")
		money = int(input("금액을 넣어주세요 : "))
		print("투입된 금액은 %4d원 입니다."%money)
		print("="*30)
		print("선택한 과일 : %-10s"%menu[num1-1])
		print("받은 금액 : %4d원"%money)
		print("==거스름돈==")
		if price[num1-1]>money:
			print("금액 부족 확인.")
		else:
			print("거스름돈은 %5d원 입니다."%(money-price[num1-1]))