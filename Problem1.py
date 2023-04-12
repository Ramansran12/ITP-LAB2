#Ramandeep Singh
#22076254
#taking inpuit from user
l=0
num=(int(input("Enter the number of years: ")))
while(l<num):
  months=0
  rainfall=0
  total=0
  #while start
  while (months<12):
     print("Enter the rainfall for the month  :",months+1,"")
     k = int(input())
     total = total + k
     months += 1
  #while end
  
  l=l+1

    # Calculate and print the total and average rainfall for the year
print("Total rainfall:",total, "")

# Calculate and print the overall average monthly rainfall
print(f"Overall average monthly rainfall: {total/12} cm")