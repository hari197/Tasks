# Program to find the sum of the series 1 + 3^2/3^3 + 5^2/5^3... upto n terms

#Taking input from user for the number of terms
n=int(input("Please enter the number of terms: "))

sum=0		#initialize sum
i=1				#initialize increment variable for loop
counter=0	#initialize counter

#If the input from the user is 0, print the sum is 0
if(n==0):
	print("The sum of the series is 0")

#To find the sum of series upto n terms
while(i!=0):
	if(i%2!=0):
		sum=sum+((i*i)/(i*i*i))
		counter+=1
	i+=1
	if counter==n:
		break	

#Displays the sum of series	
print("The sum of the series is: ", sum)

###########


