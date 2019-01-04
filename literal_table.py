def literal_Table(fname):
	literal=[]
	literal_Table=[]
	line_no=0
	value=[]
	hex1=[]
	h=""
	k=""
	h1=""
	p=[]
	instruction=["mov","add","sub"]
	asm_list=[]
	f=open(fname,"r")
	for str1 in  f.readlines():
		asm_list=str1.split()
		#print(asm_list)
		for i in range(len(asm_list)):
			#print(asm_list[1])
			if asm_list[i]=='dd':
				p=asm_list[i+1].split(',')
				for i in range(len(p)):
					value.append(p[i])
				for i in range(len(p)):
					h=hex(int(p[i]))[2:]
					if(len(h)==1):
						k=str(0)+h+(7-len(h))*'0'
						h1=h1+k
						
					else:
						k=h+(8-len(h))*'0'
						h1=h1+k
				literal.append(line_no)
				line_no+=1
				literal.append(h1)
				literal.append(value)
				literal_Table.append(literal)
				value=[]
				literal=[]
				h=""
				k=""
				h1=""
			elif asm_list[i]=='db':
				literal.append(line_no)
				line_no=line_no+1
				p4=' '.join(asm_list[i+1:])
				h=hexValue(p4)
				literal.append(h)
				literal.append(p4)
				literal_Table.append(literal)	
				literal=[]
			elif asm_list[i] in instruction:
				#print(i)
				p=asm_list[i+1].split(",")
				if(p[1].isnumeric()):
					literal.append(line_no)
					line_no+=1
					h=hex(int(p[1]))[2:]
					if(len(h)==1):
						k=str(0)+h+(7-len(h))*'0'
					else:
						k=h+(8-len(h))*'0'
					#print(k)	
					literal.append(k)
					literal.append(p[1])
					literal_Table.append(literal)
					literal=[]
					k=""
					h=""
					
	return literal_Table






def hexValue(str1):
	h=""
	for i  in range (len(str1)):
		ascii1=ord(str1[i])
		#print(ascii1,end="  ")
		v=hex(ascii1)
		v1=v[2:5]
		if(len(v1)==1):
			h=h+'0'+v1
		else:
			h=h+v1	
	return h


filename="fact.asm"
lt=literal_Table(filename)
for i in range (len(lt)):
	print(lt[i]	)
