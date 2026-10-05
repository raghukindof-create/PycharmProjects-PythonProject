# raghulist = ["ball", "bat", "stumps", "players", "umpires", "mat"]
#
# # print(raghulist*2)
# print(raghulist.pop(1))
# print(raghulist)
# print(raghulist)
# print(raghulist[0])
# print(raghulist[1])
#
# print(raghulist[2:4])     #starting index will start from zero and last index should consider as n-1 or starts from 1
#
# # raghulist[1] = "sapota"
# # print(raghulist)
#
#
# # loop
# #
# # for i in  raghulist:
# #     print(i)
#
# if "sapota" in raghulist:
#     pass
# from collections.abc import list_reverseiterator
from os import remove

# word=["collection","collection","apple", "banana"]
# print(len(word))           #length
# print(word.count("collection"))      #count
# word.sort()
# print(word)           #sort desc
# word.sort(reverse=True)                  #when we have sorted order then only we can reverse
# print(word) #asc


#append: insert the values at end
# word.append("235")             #append
# print(word)
# word.insert(2,"mango")
# print(word)
# word.remove("banana")
# print(word)
# word.pop(1)    #seconf method to remove


# third approach to del & Del is keyword not a method
# del word[1]
# print(word)
# del word
# print(word)
#
# word=["collection","collection","apple", "banana"]
#
# word2=word.copy()   #copy approach 1
# print(word)
# print(word2)
#
# word3=list(word2)   #copy approach 2
# print(word3)
#
# word4=word2+word3   #Joining
# print(word4)

# list1 = ['3', '8','4']
# list2 = ['a', 'b','c']
# list3=list()   #empty list
#
# # list2.append(k)   #approach 1
# list2.extend(list1)  #approach 2
#
# print(list2)


# tuple
# we cannot directly change values in tuple. first we have to convert the tuple into list and after changing the values, convert list to tuple again

# items = ("cherry", "nuts", "dal")
# converted_items = list(items)
# converted_items[1]="abc"
# print(converted_items)
# items = tuple(converted_items)
# print(items)
#
# print("nuts" in items)
#
# print(len(items))
#
#
# items2=items     #copying
# print(items.)



# set

# set1 = {1, 2, "banana", "apple"}
# set2 = {5,6, 1}
# print(set1)
#
# for i in set1:        #only way to read the data in same order for set
#     print(i)
#
# print("apple" in set1)
#
# print(len(set1))
# set1.add("mango")
# print(set1)
# set1.update(["anjur","badam", 9])
# print(set1)

# set1.remove("banana")
# set1.discard("abc")
# # set1.pop()
# print(set1)

# set1.clear()
# print(set1)
#
# del set1
# print(set1)

# set3 = set1 | set2
# print(set3)
#
# print(set1.intersection(set2))  #or for retrievnig the commom values
# set4= set1 & set2
# print(set4)


nums = [1, 2, 3] * 2
print(nums)


