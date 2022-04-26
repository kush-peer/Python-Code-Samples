from pip import List


# Creating a List with
# the use of multiple values
List = ["Test", "For", "test", "On", "GitHub"]
print("\nList containing multiple values: ")
print(List)
 
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List2 = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List2)
 
# accessing a element from the
# list using index number
print("Accessing element from the list")
print(List[0])
print(List[2])
 
# accessing a element using
# negative indexing
print("Accessing element using negative indexing")
     
# print the last element of list
print(List[-1])
     
# print the third last element of list
print(List[-3])

# tuple are faster than list and are immutable in nature. if your list is constant then go for tuples
tuple = ("Test", "For", "test", "On", "GitHub")
print("\nTuple containing multiple values: ", tuple)

