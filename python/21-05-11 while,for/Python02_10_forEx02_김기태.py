
marks = [90, 25, 67, 45, 80]

num = 0
for mark in marks:
	num = num + 1
	if mark >= 60 :
		print(num, "번 학생은 합격입니다")
	else:
		print("%d 번 학생은 불합격입니다."%num)