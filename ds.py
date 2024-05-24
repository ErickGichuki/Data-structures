# the input function accept the list elements in the form of a string
my_input = input("Enter the elements of your list: ")

# break an input string into a list using split() method
my_list = my_input .split()
print("string list: ", my_list)

# access list elements using a for loop and range
for i in range(len(my_list)):
    # convert each item into int type
    my_list[i] = int(my_list[i])
    print("My list: ", my_list)

# calculating the sum of my list elements
print("sum = ", sum(my_list))

my_tupple = ("River and the source", "The river between", "Kidagaa kimemwozea", "The caucasian chalk circle", "Betrayal in the City")
for m in (my_tupple):
    pass

my_dict = {
    "name": "",
    "age": "",
    "favoritecolor":""
}
print(my_dict["age"])