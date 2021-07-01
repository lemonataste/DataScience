#문제1
'''
a = "Life is too short, you need python"

if "wife" in a: print("wife")     #wife가 a에 포함될때 출력 (X)
elif "python" in a and "you" not in a: print("python")#python이 a에 포함되고, you가 포함되지 않을떄 출력(X)
elif "shirt" not in a: print("shirt")  #shirt가 포함되지 않을때 출력 (O)  
elif "need" in a: print("need")    #조건은 맞으나 위에서 멈춤
else: print("none")    #위와 동일
의 결과값은?
'''
# 정답은 shirt

#문제2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
a=0
sul=0
while a<=1000:
	a=a+1
	if a%3==0:
		sul=sul+a
print(sul)	

#문제3 while을 사용해 별을 표시하는 프로그램을 작성
a=0
while True:
	a=a+1
	print("*"*a)
	if a>=5:
		brake

#문제4 for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

a=0
for a in range(1,101):
	print(a)


#문제5
list01=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum =0


for jum in list01:
	sum= sum+jum

print("합계 :%d"%sum)
print("평균 :%0.2f"%(sum/len(list01)))

#문제6 
'''
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
를 리스트 내포형으로 만들기		'''

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)
[2, 6, 10]