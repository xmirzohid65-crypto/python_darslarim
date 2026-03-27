# Converts the first character to upper case
text1 = "hello world"
print(text1.capitalize())

# Converts string into lower case
text2 = "HELLO"
print(text2.casefold())

# Returns a centered string
text3 = "Hello"
print(text3.center(20, "*"))

# Returns the number of times a specified value occurs in a string
text4 = "banana"
print(text4.count("a"))

# Returns an encoded version of the string
text5 = "Hello"
print(text5.encode())

# Returns true if the string ends with the specified value
text6 = "hello.py"
print(text6.endswith(".py"))

# Sets the tab size of the string
text7 = "H\te\tl\tl\to"
print(text7.expandtabs(4))

# Searches the string for a specified value and returns the position of where it was found
text8 = "Hello world"
print(text8.find("world"))

# Formats specified values in a string
name = "Ali"
age = 20
print("My name is {} and I am {}".format(name, age))

# Formats specified values in a string
data = {"name": "Ali", "age": 20}
print("Name: {name}, Age: {age}".format_map(data))

# Searches the string for a specified value and returns the position of where it was found
text9 = "Hello world"
print(text9.index("world"))

# Returns True if all characters in the string are alphanumeric
text10 = "Hello123"
print(text10.isalnum())

# Returns True if all characters in the string are in the alphabet
text11 = "Hello"
print(text11.isalpha())

# Returns True if all characters in the string are ascii characters
text12 = "Hello"
print(text12.isascii())

# Returns True if all characters in the string are decimals
text13 = "123"
print(text13.isdecimal())

# Returns True if all characters in the string are digits
text14 = "123"
print(text14.isdigit())

# Returns True if the string is an identifier
text15 = "my_var"
print(text15.isidentifier())

# Returns True if all characters in the string are lower case
text15 = "hello"
print(text15.islower())

# Returns True if all characters in the string are numeric
text16 = "123"
print(text16.isnumeric())

# Returns True if all characters in the string are printable
text17 = "Hello"
print(text17.isprintable())

# Returns True if all characters in the string are whitespaces
text18 = "   "
print(text18.isspace())

# Returns True if the string follows the rules of a title
text19 = "Hello World"
print(text19.istitle())

# Returns True if all characters in the string are upper case
text20 = "HELLO"
print(text20.isupper())

# Joins the elements of an iterable to the end of the string
words21 = ["Hello", "World"]
print(" ".join(words21))

# Returns a left justified version of the string
text22 = "Hello"
print(text22.ljust(10, "-"))

# Converts a string into lower case
text23 = "HELLO"
print(text23.lower())

# Returns a left trim version of the string
text24 = "   Hello"
print(text24.lstrip())

# Returns a translation table to be used in translations
table = str.maketrans("H", "J")
text25 = "Hello"
print(text25.translate(table))

# Returns a tuple where the string is parted into three parts
text26 = "Hello World"
print(text26.partition(" "))

# Returns a string where a specified value is replaced with a specified value
text27 = "Hello world"
print(text27.replace("world", "Python"))

# Searches the string for a specified value and returns the last position of where it was found
text28 = "Hello hello"
print(text28.rfind("hello"))

# Searches the string for a specified value and returns the last position of where it was found
text29 = "Hello hello"
print(text29.rindex("hello"))

# Returns a right justified version of the string
text30 = "Hello"
print(text30.rjust(10, "-"))

# Returns a tuple where the string is parted into three parts
text31 = "Hello World"
print(text31.rpartition(" "))

# Splits the string at the specified separator, and returns a list
text32 = "a-b-c-d"
print(text32.rsplit("-", 2))

# Returns a right trim version of the string
text33 = "Hello   "
print(text33.rstrip())

# Splits the string at the specified separator, and returns a list
text34 = "apple,banana,orange"
print(text34.split(","))

# Splits the string at line breaks and returns a list
text35 = "Hello\nWorld"
print(text35.splitlines())

# Returns true if the string starts with the specified value
text36 = "Hello world"
print(text36.startswith("Hello"))

# Returns a trimmed version of the string
text37 = "  Hello  "
print(text37.strip())

# Swaps cases, lower case becomes upper case and vice versa
text38 = "Hello World"
print(text38.swapcase())

# Converts the first character of each word to upper case
text = "hello world"
print(text.title())

# Returns a translated string
table = str.maketrans("ae", "12")
text = "apple"
print(text.translate(table))

# Converts a string into upper case
text = "hello"
print(text.upper())

# Fills the string with a specified number of 0 values at the beginning
text = "42"
print(text.zfill(5))