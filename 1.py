def isPrime(number):

	flag = False

	if number == 2:
		flag = True
	else :
		for i in range(2,number):
			if number % i == 0 :
				break
			if i == number-1:
				flag = True
	if flag == True :
		return True
	else :
		return False


x = int(input("請輸入一個數字(>1)"))

sum = 0

for j in range (2,x):
	if isPrime(j) :
		sum+=1
print("質數有",sum)
	
				
				