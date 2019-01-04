import symbolTable1
import literal_table
import all_reg_dict
def seperatFromMain(filename):
	flag=0
	line=0
	fromMain=[]
	f=open(filename,"r").readlines()
	for i in range(len(f)):
		if "main:" in f[i]:
			break
		line+=1
	f[i]=f[i].replace('main:','')
	for j in range(i,len(f)):
		f[j]=f[j].replace('\n','').replace('\t','').replace(',',' ').split()
		fromMain.append(f[j])

	return fromMain

def spaces(im):
	return im+(30-len(im))*' '
def set_instructions(filename):
	im=''
	frommain=seperatFromMain(filename)
#	print(frommain)
	st=symbolTable1.symbolTable(filename)
	reg=all_reg_dict.reg
	#ins=all_reg_dict.ins
	for i in range(len(frommain)):
		if len(frommain[i])==3:
				im=frommain[i][0]+' '+','.join(frommain[i][1:])
#				print(im)
		elif len(frommain[i])==2:
				im=' '.join(frommain[i])
#				print(im)
		for j in range(len(frommain[i])):
			if ':' in frommain[i][j]:
				frommain[i][j]=frommain[i][j][frommain[i][j].index(':')+1:]
				#print(frommain[i][j])
			if frommain[i][j] in reg:
				frommain[i][j]=reg[frommain[i][j]]	
			#if frommain[i][j] in ins:
				#frommain[i][j]=ins[frommain[i][j]]
			for k in st:
				if k[1]==frommain[i][j]:
					frommain[i][j]="sym#"+str(k[0])
					break 
			for k in st:
				if k[1] in frommain[i][j]:
					frommain[i][j]="val#"+str(k[0])
					break 
			for k in lt:
				if k[-1]==frommain[i][j]:
					frommain[i][j]="lit#"+str(k[0])
					break
		if len(frommain[i])==3:
			print(spaces(im)+frommain[i][0]+' '+','.join(frommain[i][1:]))
		elif len(frommain[i])==2:
			print(spaces(im)+' '.join(frommain[i]))
#	print(frommain)
filename="test.asm"
st=symbolTable1.symbolTable(filename)
lt=literal_table.literal_Table(filename)
set_instructions(filename)
 
