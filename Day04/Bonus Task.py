favorites = ["pizza", "ice cream", "movies"]  # Creating a list

# Accessing elements
print(favorites[0])  # Prints "pizza"

# Appending an element
favorites.append("gaming")
print(favorites[-1])  # Prints "gaming"

# Inserting at a specific index
favorites.insert(1, "chocolate")
print(favorites)  # ['pizza', 'chocolate', 'ice cream', 'movies', 'gaming']

# Removing an element by value
favorites.remove("movies")
print(favorites)  # ['pizza', 'chocolate', 'ice cream', 'gaming']

# Removing the last element
last_item = favorites.pop()
print("Removed:", last_item)  # Removed: gaming
print(favorites)

# Finding the index of an element
index = favorites.index("ice cream")
print("Index of 'ice cream':", index)

# Counting occurrences
favorites.append("pizza")
count = favorites.count("pizza")
print("Pizza count:", count)  # 2

# Sorting the list alphabetically
favorites.sort()
print("Sorted favorites:", favorites)

# Reversing the list
favorites.reverse()
print("Reversed favorites:", favorites)

# Clearing the list
favorites.clear()
print("After clear:", favorites)  # []

