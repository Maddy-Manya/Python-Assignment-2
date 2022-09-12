def recursiveReverse(str1: str, pos: int):
    if pos < -len(str1): #base case
        return

    print(str1[pos],end = "") #processing
    recursiveReverse(str1,pos-1) #recurive step

str1 = input("Enter any string: ")
print("Reversed string: ")
recursiveReverse(str1,-1)


