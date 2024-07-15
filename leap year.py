#year=int(input("which year do you want to know is or was a leap year "))
#if (year%4==0 and year!=100)or(year%400==0):
   # print("the year is a leap year")
#else:
   # print("the is not a leap year")
# Creating a List
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# Accessing Items
print("First item:", fruits[0])  # apple
print("Second item:", fruits[1])  # banana
print("Third item:", fruits[2])  # cherry

# Changing Items
fruits[1] = "blueberry"
print("After changing second item:", fruits)  # ["apple", "blueberry", "cherry"]

# Adding Items
fruits.append("date")
print("After appending an item:", fruits)  # ["apple", "blueberry", "cherry", "date"]

# Inserting Items
fruits.insert(1, "banana")
print("After inserting an item:", fruits)  # ["apple", "banana", "blueberry", "cherry", "date"]

# Removing Items by value
fruits.remove("blueberry")
print("After removing an item by value:", fruits)  # ["apple", "banana", "cherry", "date"]

# Removing Items by position
fruits.pop(2)
print("After removing an item by position:", fruits)  # ["apple", "banana", "date"]

# Length of the List
print("Length of the list:", len(fruits))  # 3

# Looping Through a List
print("Looping through the list:")
for fruit in fruits:
    print(fruit)

# Slicing a List
print("Slicing the list (items 1 to 2):", fruits[1:3])  # ["banana", "date"]

# Sorting a List
fruits.sort()
print("After sorting the list:", fruits)  # ["apple", "banana", "date"]

# Reversing a List
fruits.reverse()
print("After reversing the list:", fruits)  # ["date", "banana", "apple"]

# Copying a List
fruits_copy = fruits.copy()
print("Copy of the list:", fruits_copy)  # ["date", "banana", "apple"]

# Clearing a List
fruits.clear()
print("After clearing the list:", fruits)  # []
print ("\n")
colour=["gold","pink","rose gold" ]
print(colour)
colour.remove("pink")
print(colour)
print(len(colour))
for i in colour:
    print(i)