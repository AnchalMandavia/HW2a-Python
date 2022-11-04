import operator

def sort_dictionary(inputDict):
    for i in sorted(inputDict.values(), key = operator.itemgetter(1),  reverse = True):
        #print(i[0], end=" ")
        #print(f"('{inputDict.keys[i]}', {i[0]})")
        print(f"('{inputDict.keys}'), {i[0]})", end = " ")
    print()

def main():
    A = {"Tom" : (5464512, 24) , "Sara" : (5446987, 32) , "Mary" : (1557896, 20)}
    sort_dictionary(A)
    print(A)

main()