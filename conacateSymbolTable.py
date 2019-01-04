import symbolTable2 as st
def conacateSymboltable(sym1,sym2,ext1):
	lst1=[]
	l=len(sym1)
	temp=""
	lineNo=sym1[l-1][0]
	for i in range(len(sym1)):
		lst1.append(sym1[i][1])
	#print(lst1)
	for i in range (len(sym2)):
		#print(sym2[i][1])
		if sym2[i][1] in lst1 and sym2[i][1] not in ext1":
			temp=str(sym2[i][1])+str("_replace")
			sym2[i][1]=temp
			sym2[i][0]=sym2[i][0]+lineNo
			sym1.append(sym2[i])
		else:
			sym2[i][0]=sym2[i][0]+lineNo
			sym1.append(sym2[i])
	return sym1


sym1=st.symbolTable("fact.asm")
sym2=st.symbolTable("fibo.asm")
print(sym2[1])
#print(sym1)
"""for i in range(len(sym1)):
	print("\n")
	for j in range(len(sym1[0])):
		print(st.space(str(sym1[i][j])),end=" ")
	print()
for i in range(len(sym2)):
	print("\n")
	for j in range(len(sym2[0])):
		print(st.space(str(sym2[i][j])),end=" ")
	print()
"""
sym=conacateSymboltable(sym1[0],sym2[0],sym1[1])
for i in range(len(sym)):
	print("\n")
	for j in range(len(sym[0])):
		print(st.space(str(sym[i][j])),end=" ")
	print()


