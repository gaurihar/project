def space(string):
#    print(string+((20-len(string))*' '))
    return string+((5-len(string))*' ')

def symbolTable(filename):
	final=[]
	result=[]
	p=[]
	define_lable=[]
	list7=["jz","jnz","jnz","jmp","loop","call"]
	f=open(filename,"r")
	sum1=0
	sum2=0
	lineNo=1
	extern_list=[]
	for str1 in  f.readlines():
		asm_list=str1.split()
		#print(asm_list)
		for i in range(len(asm_list)):
			if asm_list[i]=='dd':
				#print(asm_list)
				result.append(lineNo)
				lineNo+=1	
				result.append(asm_list[i-1])
				result.append(4)
				p=asm_list[i+1].split(',')
				
				result.append(len(p)-1)
				result.append('S')
				result.append('D')
				result.append(sum1)
				sum1=sum1+len(p)*4		
				result.append(p)
				final.append(result)

				result=[]
			elif asm_list[i]=='db':
				result.append(lineNo)
				lineNo+=1	
				result.append(asm_list[i-1])
				result.append(1)
				p=asm_list[i+1]
				result.append(len(p))
				result.append('S')
				result.append('D')
				result.append(sum1)
				sum1=sum1+len(p)
				result.append(p)
				final.append(result)
				result=[]
			elif asm_list[i]=='dw':
				result.append(lineNo)
				lineNo+=1	
				result.append(asm_list[i-1])
				result.append(2)
				p=asm_list[i+1].split(",")
				result.append(len(p)-1)
				result.append('S')
				result.append('D')
				result.append(sum1)
				sum1=sum1+len(p)*2	
				result.append(p)
				final.append(result)
				result=[]
			elif asm_list[i]=='dw':
				result.append(lineNo)
				lineNo+=1	
				result.append(asm_list[i-1])
				result.append(2)
				p=asm_list[i+1].split(",")
				result.append(len(p)-1)
				result.append('S')
				result.append('D')
				#result[i][5]=		
				result.append(p)
				final.append(result)
				result=[]
			elif asm_list[i]=='resd':
				result.append(lineNo)
				lineNo+=1	
				
				result.append(asm_list[i-1])
				result.append(4)
				p=asm_list[i+1]
				result.append(1)
				result.append('S')
				result.append('D')
				result.append(sum2)
				sum2=sum2+int(asm_list[i+1])*4		
				result.append(asm_list[i+1])
				final.append(result)
				result=[]
			elif asm_list[i]=='resb':
				result.append(lineNo)
				lineNo+=1	
				result.append(asm_list[i-1])
				result.append(2)
				p=asm_list[i+1]
				result.append(1)
				result.append('S')
				result.append('D')
				result.append(sum2)
				sum2=sum2+int(asm_list[i+1])*4		
				result.append(asm_list[i+1])
				final.append(result)
				result=[]
			elif asm_list[i]=='resw':
				result.append(lineNo)
				lineNo+=1	
				result.append(asm_list[i-1])
				result.append(1)
				p=asm_list[i+1]
				result.append(1)
				result.append('S')
				result.append('D')
				result.append(sum1)
				sum1=sum1+int(asm_list[i+1])			
				result.append(asm_list[i+1])
				final.append(result)
				result=[]
			elif ':' in asm_list[i]:
				p=asm_list[i].split(':')
				l1=len(final)
				#print(l1)
					
				for i in range (l1):
					if p[0]==final[i][1]:
						#print(final[i][5])
						final[i][5]="D"
					else:
						define_lable.append(p[0])
						
						result.append(lineNo)
						result.append(p[0])
						result.append(0)
						result.append(0)
						result.append('L')
						result.append('D')
						result.append(0)
						result.append('-')
				final.append(result)
				result=[]
				lineNo+=1
			elif asm_list[i]=="extern":
					extern_list=asm_list[i+1].split(",")
					#print(extern_list)
						
			elif asm_list[i] in list7:
				result.append(lineNo)
				lineNo+=1	
				result.append(asm_list[i+1])
				
				result.append(0)
				result.append(0)
				result.append('L')
				#print(asm_list[i+1])
			
				if ((asm_list[i+1]  in extern_list )or(asm_list[i+1]  in define_lable)):
					#print(asm_list[i+1])
					result.append('D')
				else:
					result.append('U')
				result.append(0)
				result.append('-')
				final.append(result)
				result=[]
	
	return final
filename="fact.asm"
st=symbolTable(filename)

for i in range(len(st)):
	print("\n")
	for j in range(len(st[0])):
		print(space(str(st[i][j])),end=" ")
	print()

