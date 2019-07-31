#given a classrom of N students, whose friendships can be represented in an adjacency list. for example the following describes a situation where 
#0 is friends with 1,2,3 and 6 
data_driver = {0:[1,2],1:[0,5],2:[0],3:[6],4:[],5:[1],6:[3],7:[]}
print(len(data_driver))
for i in range(len(data_driver)):
    print(data_driver[i])
    
