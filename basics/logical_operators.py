# logical operators: or and not 
#bool:true or false 
b1= True
b2 = False
print(f"the type and value of 'b1' is {int(b1)} and {int(b1)} respectively");
print(f"the type of variable of 'b2' is {int(b2)}")
condition1= True
condition2 = True
condition3= False
print(condition1 and condition2)
if condition1 and condition2 and condition1:
    print("all conditions are satisfied")

print("practice2")
print(condition1 or condition2)
print(condition1 or condition3)
if condition1 or condition2 or condition3:
    print("one of teh conditions is satisfiedw")
condition1= not condition1
print(condition1)
#condition2= False
condition1 = True 
if not condition1 and condition2 or condition3:
    print("what is happening")

print("logical operators priority:" , True or False and True or True or False)