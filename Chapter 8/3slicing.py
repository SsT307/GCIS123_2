list = [4,7,8,2,5,8,4,8,9,2]
l1 = list[1:4] # from index 1 to 3, not including 4
l2 = list[3:] # from index 3 till the end
l3 = list[:6] # from the beginning till index 5, not including 6
l4 = list[:100] # will just print the whole list
l5 = list[3:9:2] # from 3-8, with step 2
l6 = list[::2] # from the beginning till the end with step 2
l7 = list [7:2:-1] # going backwards 

#print(l1)

# ------------------------------ sorted acending ----------------------------- #
list.sort() # In-place, DESTROYING ORIGINAL FUNC
#print(list)

# ----------------------------- sorted decending ----------------------------- #
l_sorted = sorted(list, reverse=True) # Out of place, NOT DESTRUCTIVE
#print(l_sorted)


# ------------------- creating function with its own order ------------------- #
list_num2 = ['Hello', 'Professor', 'please', 'send', 'HELP!']
list_num2.sort(key=len) # sorting based on the LENGTH OF THE WORD
print(list_num2)

list_num2.sort(key=str.upper) # sorting based off of alphabetical order
print(list_num2)