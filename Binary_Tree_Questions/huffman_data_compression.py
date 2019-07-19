#given a string find the Huffman compression of said string using the huffman algorithm. aka data compression binary tree. 

#Code start 
print("Huffman Compression Program")
print("*"*8)
input_string = input("Enter a string you wish to compress:")
len_of_str = len(input_string)
print("Your Message is: " , (input_string))
print("Your data is " , len_of_str*7 , "bits long")
#Gathers user input and saves them to arguments. also informs user of how the data looks. uncompressed.
print("#"*30)

################################################################################################################################

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

################################################################################################################################
#after generating this data we can now start to build out our tree with nodes. 

nodes = []
while len(letters) > 0:
    nodes.append(letters[0:2])
    letters = letters[2:]
nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)
#this generates the base level of nodes for the tree, frequency and letter.

################################################################################################################################

#now we have to combine the Base nodes to the Huffman tree and allocate either a 0- or  1 to each pair.
#later we will use this to create the binary code for each letter.

def combine(nodes):
    #pos == position. 
    pos = 0
    newnode = []
    #grab the lowest nodes.
    if len(nodes) > 1:
        nodes.sort()
        #then we have to add the 0,1 for later use.
        nodes[pos].append("0")
        nodes[pos+1].append("1")
        #this starts the poccess of ordering the nodes in order of size. 
        #then combines them together in binary pathways.
        combined_node1 = (nodes[pos][0]+nodes[pos+1][0])
        combined_node2 = (nodes[pos][1]+nodes[pos+1][1])
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes = []
        newnodes.append(newnode)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes
        #continues until there is only one node left. 
        huffman_tree.append(nodes)
        combine(nodes)
    return huffman_tree

newnodes = combine(nodes)

################################################################################################################################
#tree should be inverted to give a aprox visualization of what you might do. 
huffman_tree.sort(reverse=True)
print("here is the Huffman Tree, showing mergerd nodes and pathways.")
#remove the duplicate items in the huffman tree and creates an array checklist with just the nodes and the correct levels. 
checklist = []
for level in huffman_tree:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else:
            level.remove(node)
count = 0
for level in huffman_tree:
    print("Level ",count," : ",level)
    count +=1
print()
print("#"*30)
################################################################################################################################
#build the binary codes for each character - easy cop out is there is only one type of character in the string.
letter_binary = []
if len(only_letters)==1:
    letter_code = [only_letters[0],"0"]
    letter_binary.append(letter_code * len(input_string))
else:
    for letter in only_letters:
        lettercode = ""
        for node in checklist:
            if len(node)>2 and letter in node[1]:
                lettercode = lettercode + node[2]
        letter_code = [letter,lettercode]
        letter_binary.append(letter_code)
#ouputs the letters with binary code.
print("Your binary code is: ")
#something here is causing it to print everything in the list, It should only print the final node. 
for letter in letter_binary:
    print(letter[0], letter[1])
################################################################################################################################
#create bistring of the original message using new codes. 
bitstring = ""
for character in input_string:
    for item in letter_binary:
        if character in item:
            bitstring = bitstring +item[1]


# I got to this point and realized there are much easier ways to implement this huffman tree in python. using built in dics
