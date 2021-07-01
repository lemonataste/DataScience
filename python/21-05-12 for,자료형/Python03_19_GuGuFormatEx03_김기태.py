
for a in range(2,10):
	print("# %d 단" %a,end="    ")

print("")
print("="*78)

for gu1 in range(2,10):
	for gu2 in range(2,10):
		print("%dx%d = %2d"%(gu2,gu1,gu2*gu1),end="  ")
	print("")
print("-"*78)