n= 385916
chislo1= n//1000
chislo2 = n%1000
sum1 = (chislo1//100) + (chislo1%10) + ((chislo1%100)//10)
sum2 = (chislo2//100) + (chislo2%10) + ((chislo2%100)//10)
if sum1 == sum2:
    print("yes")
else:
    print("no")