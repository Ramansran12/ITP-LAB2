# user input
x=int(input("Starting number of organisms:"))
y=int(input("Average daily percentage increase:")) 
                                  
                      
z=int(input("Enter the number of the days to display the finaly data:")) 

#printing the organisms data for each day
print(" population ")
print("--------------------------")
for i in range(1,z):
    x=x+(x*(y/100))                           
  #printing percentage
    
    print(x,"\n")                          

