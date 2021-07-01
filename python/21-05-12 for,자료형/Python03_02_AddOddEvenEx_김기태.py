
add=0
for i in range(1,11):
	add=add+i

print("1 - 10 까지의 합 :",add)

odd = 0

#홀수의 합
for i in range(1,11,2):
	odd = odd +i
print("홀수의 합 :",odd)

even = 0
#짝수의 합
for i in range(2,11,2):
	even = even +i
print("짝수의 합 :",even)