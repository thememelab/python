#data Structure

#list
starting_list = [3,5,7,9,12]

#list can be accessed by index
#fisrt index
starting_list[0]
#last index
starting_list[-1]

#list object menthods
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
len(stack)
stack.pop()


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort() # sorts in aphabeticval order

#function to sum values in alist
def sumValues(A):
    results = 0
    for x in A:
        results = results+x
    # always return somemthing for a fucntion
    print( results)
    #return results
#call function
sumValues(starting_list)


def findAverage(A):
    list_count = len(A)
    results = 0
    for x in A:
        results = results+x

    avg = results/list_count
    print(avg)
    return avg


findAverage(starting_list)
