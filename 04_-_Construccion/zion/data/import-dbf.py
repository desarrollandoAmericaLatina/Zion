from dbfpy import dbf
file = open('data.csv', 'r')  
for line in f:  
	line =  line.split(',')  
#	product = Product() 
#	product.name = line[2] + '(' + line[1] + ')'  
#	product.description = line[4]  
#	product.price = '' #data is missing from file  
#	product.save()  
	print line[0]
f.close()
