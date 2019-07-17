#given a string find the Huffman compression of said string using the huffman algorithm. aka data compression binary tree. 

#Code start 
print("Huffman Compression Program")
print("*"*8)
input_string = input("Enter a string you wish to compress:")
len_of_str = len(input_string)
print("Your Message is: " , (input_string))
print("Your data is " , len_of_str*8 , "bits long")
#Gathers user input and saves them to arguments. also informs user of how the data looks. uncompressed.

#Create a list of characters and their frequency 
letters = []
only_letters = []
for letter in input_string:
    if letter not in letters:
        freq = input_string.count(letter)
        letters.append(freq)
        letters.append(letter)
        only_letters.append(letter)
#print(letters)
#print(only_letters)
# from this we have the frequency of each letter used we also remove duplicate letters to make it easier to read later. 

#after generating this data we can now start to build out our tree with nodes. 

nodes = []
while len(letters) > 0:
    nodes.append(letters[0:2])
    letters = letters[2:]
nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)
