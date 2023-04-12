#Ramandeep singh
#22076254
# asking user for input
x = []
y = int(input("Enter the Number: "))
l = 0
#starting while
while(l<y):
  x.append(int(input("Enter the Element: ")))
  l=l+1
print(x)

z=[]
i=0
#ending while
#using another while for listing the numbers which are larger than 5
while (i < y):
  if(x[i] > 5):
    z.append(x[i])
  else:
    pass

  i = i+1
# printing the list of numbers
print("List of numbers that are larger than 5:",z,"")