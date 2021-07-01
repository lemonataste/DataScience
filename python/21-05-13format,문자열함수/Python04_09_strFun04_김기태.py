#왼쪽 / 오른쪽 / 양쪽 공백 지우기 
a = ' hi '

print(a)
print(a.lstrip()+'chk')
print(a.rstrip()+'chk')
print(a.strip()+'chk')
print('-'*15)

#문자열 바꾸기
a = 'Life is too short'
print(a)
cng = a.replace('Life','your leg')
print(cng)
print('-'*15)