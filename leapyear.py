startYear=int(input("Enter the start years:"))
print("Enter thr last year")
endYear=int(input("Enter the end years:"))
print("List of leap years:")
for year in range(startYear,endYear):
	if((year%4==0)and(year%100!=0))or(year%400==0):
		print(year)

