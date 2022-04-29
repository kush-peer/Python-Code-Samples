def main():
    print("Test set")

# remove dupliates from list  
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'i', 'a', 'a', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def setFunction(list):
    duplicates = set([x for x in list if list.count(x)>1])
    print(duplicates)

setFunction(list)


list = set(list)
print(list)
Set = set([1,2,'test',4,5,6])
print("\nSet containing multiple values: ", Set)
for i in Set:
    print(i)

# A frozen set
frozen_set = frozenset(["e", "f", "g"])
 
print("\nFrozen Set")
print(frozen_set)

#check element in set
print("test" in Set)
 
arr = [1,2,3,4,5,6,7,8,9,10]
for i, ar in enumerate(arr):
    if ar == 5:
        print("Found at index: ", i)
        break
arr[i] = ar+i;
print(arr)

if __name__ == "__main__":
    main()

