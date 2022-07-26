n = int(input("Enter the number = "))
prime = True
for i in range(2,n):
    if i%n == 0 :
        prime = False
        break
if prime==False:
    print(n,"is not Prime")   
else:
    print(n,"is Prime")  
