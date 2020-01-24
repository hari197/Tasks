#This program takes a number as input from user and returns list of its digits

n= input( "  Please enter the number: ")#Takes input from user#

list=[] #intializing list
c=str(n)#converting the number entered to a string

#Logic to return list of digits from the number
for i in range (len(c)):
	list.append(int(c[i]))
	
# Printing the output list
print ("The list of digits is ", list)

##########


