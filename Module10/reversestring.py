string = input("Enter a string value: ")
if isinstance(string, str):
    reverseString = string[::-1]
    print("Reverse String:", reverseString)
else:
    print("Please enter a valid string.")
