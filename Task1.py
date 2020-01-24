#Program to check if an element entered by the user exists in a list

LIST_A=[1,2,3,4,4,4] 	#List of numbers

print("Check if an element exists in list")

#Takes input from user for element to be checked
n=int(input("Enter the element that you need to check :"))

#Function to check if the element exists in list
if n in LIST_A:
 	print(" The element exists in the list")
else:
 	print("The element does not exists in the list")
 	
#################
         