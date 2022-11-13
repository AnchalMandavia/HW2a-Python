import operator

def sort_dictionary(inputDict):
    for i in sorted(inputDict.values(), key = operator.itemgetter(1),  reverse = True):
        #print(i[0], end=" ")
        #print(f"('{inputDict.keys[i]}', {i[0]})")
        print(f"('{inputDict.keys}'), {i[0]})", end = " ")
    print()