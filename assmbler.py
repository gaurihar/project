import intermediate
import symbolTable1
import literal_table
filename='fact.asm'
st=symbolTable1.symbolTable(filename)
lt=literal_table.literal_Table(filename)

def spaces(im):
	return im+(20-len(im))*' '

def print1(lt):
	for i in lt:
		for j in i:
			print(spaces(str(j)),end='')
		print()
#print1(st)
print1(lt)
intermediate.set_instructions(filename)

