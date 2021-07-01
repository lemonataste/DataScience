menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]
manco=0
idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];
def menuList(a):
	for i in range(len(a)):
		print("%s\t"%a[i],end="")
	
def inputData(a,b):
    for i in range(len(a)):
        dic[a[i]]=b[i]

def score():
	for i in range(len(MenuList)):
		print(MenuList[i],end="\t")
	print("")
	print("-"*60)
			
	vList = list(dic.values())
	kList = list(dic.keys())

	for i in kList:
		print(i,end="\t")
		for j in range(len(dic[i])):					
			print(dic[i][j],end="\t")
		print("")




dic = {}
deleteIDList = []
idx = 0;

print("-"*80)
print("학생 관리 시스템v01")
print("-"*80)
menuList(menu)
print("\n")
print("-"*80)

inputData(idList,scoreList)

while True:
	num=input("메뉴의 번호를 선택해주세요 : ")
	if num=="":
		print("chk")
	else:
		num=int(num)

		if num==1:
			print("%s Algorithm Chk"%menu[num-1])
		
		elif num==2:
			print("%s Algorithm Chk"%menu[num-1])
		elif num==3:
			score()

		elif num==4:
			print("%s Algorithm Chk"%menu[num-1])
		elif num ==9:
			break
		else:
			print("메뉴를 다시 선택해 주세요")