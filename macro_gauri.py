def replace_def(macros,macro_names,after_main):
	fp1=open('write.txt','w')
	ll=[]
	for i in range(len(after_main)):
		k=after_main[i].split()
		if len(k)!=0:
			if k[0] in macro_names:
				def1=macro_names.index(k[0])
				param=k[1].split(',')
				for j in range(len(macros[def1])):
					#print(macros[def1][i])
					if "%macro" not in macros[def1][j] and "%endmacro" not in macros[def1][j]:
						if '%' in macros[def1][j]:
							macros[def1][j]=macros[def1][j].split()
							macros[def1][j][1]=macros[def1][j][1].split(',')
							macros[def1][j][1][1]=param[int(macros[def1][j][1][1].replace('%',''))-1]
							macros[def1][j][1]=','.join(macros[def1][j][1])
							macros[def1][j]=' '.join(macros[def1][j]) 
							#print(macros[def1][i])
				after_main[i]=macros[def1][1:len(macros[def1])-1]
			else:
				after_main[i]=[after_main[i]]
	fp1.write('main:\n')
	for i in after_main:
		if len(i)!=0:
			for j in i:
				fp1.write(' '*5+j+'\n')
	fp1.close()
	print(after_main)
def separate_macro(pgm):
	flag=0
	macros=[]
	sub_macro=[]
	macro_names=[]
	after_main=[]
	for i in range(len(pgm)):
		if flag==2:
			after_main.append(pgm[i].replace('\n','').replace('\t',''))
		if "%macro" in pgm[i]:
			macro_names.append(pgm[i].replace('\n','').split()[1])
			flag=1
		if flag==1:
			sub_macro.append(pgm[i].replace('\n','').replace('\t',''))
		if "%endmacro" in pgm[i]:
			flag=0
			macros.append(sub_macro)
			sub_macro=[]
		if "main:" in pgm[i]:
			flag=2
	replace_def(macros,macro_names,after_main)
def main(filename):
	macro_names=[]
	fp=open(filename,'r').readlines()
	separate_macro(fp)
#	print(macro_names)
filename="macro1.asm"
main(filename)
