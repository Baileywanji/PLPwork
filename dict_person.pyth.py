
#Accept use input of dictionary of person information
#person_infor = {'name': 'Caroline', 'age': 33, 'color': 'brown'}
#print(person_infor['name'])
#print(person_infor['age'])
#print(person_infor['color'])

# Accept user input for the first set of integers
#num_integerList1 = input("1 2 3 4 5")
#set1 = set(map(int, num_integerList1.split()))

# Accept user input for the second set of integers
#num_integerList2 = input("3 4 5 6 7")
#set2 = set(map(int, num_integerList2.split()))

# Create a new set containing only the elements common to both sets
common_elements = set1.intersection(set2)

# Print the common elements
#print("Common elements:", common_elements)

# List of words
word_list = ["apple", "banana", "orange", "kiwi", "pear", "grape"]

# New list containing words with an odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

# Print the new list
print("Words with an odd number of characters:", odd_length_words)
