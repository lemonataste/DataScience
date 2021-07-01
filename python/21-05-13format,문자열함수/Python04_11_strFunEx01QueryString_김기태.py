a = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python"

url1 = a.split("?")
que=url1[1].split("&")
co=0
print("URL : %s"%url1[0])
print("===QueryString===")
for i in range(len(que)):
	print(que[i])
	co=co+1
print("QueryString 개수 : %d"%co)

