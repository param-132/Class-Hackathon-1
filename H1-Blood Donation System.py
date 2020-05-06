#ASSIGNMENT - 

#To develop a Blood donation system data structure

#Designing an efficient data structure for admin group of this system

lst1 = [] 
   
n = int(input("Enter number of elements in the data for donor : "))                    
   
for i in range(0, n):     #taking input from user about donor
    ele = (input()) 
  
    lst1.append(ele)  
      
print("Name of the donor ,Donor's blood group, Name of the hospital, Branch name : ")
print(lst1)

def Convert(toConvert):       #coverting the given list into dictionary
    finalDict={ toConvert[i]: toConvert[i+1] for i in range(0,len(toConvert),2)}
    return finalDict

print("The Dictionary form of above data is: ")
print(Convert(lst1))

lst2 = [] 
   
n = int(input("Enter number of elements in the data : ")) 
   
for i in range(0, n):        #taking input from the user about recipient
    ele = (input()) 
  
    lst2.append(ele)  
      
print("Name of the recipients, Recipient's blood group, Name of the hospital, Branch name : ")
print(lst2)

def Convert(toConvert):
    finalDict={ toConvert[i]: toConvert[i+1] for i in range(0,len(toConvert),2)}
    return finalDict

print("The Dictionary form of above data is: ")
print(Convert(lst2))

print("Following are the rare blood groups in the recipient's hospital : ")
a=input()
print("Name of rare BG's is: ")
print(a)

print("The details of Donor : ")    #displaying the data
print(Convert(lst1))
print("The details of recipient : ")
print(Convert(lst2))







