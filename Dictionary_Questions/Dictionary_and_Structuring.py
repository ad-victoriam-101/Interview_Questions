#Getting the data out right. 
#Dictionary data type, is a collection of many values. Usually stored in key value pairs. mycat = {'size':'FAT','Colour':'Gray','disposition':'loud'}
import pprint
my_cat = {'size':'FAT','Colour':'Gray','disposition':'loud'}
print(my_cat['size'])

message ='it was a bright cold day in april, and the clocks were strickign thirteen.'
count = {}
for char in message:
    count.setdefault(char,0)
    count[char] = count[char]+1
pprint.pprint (count)