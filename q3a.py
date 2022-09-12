def iterativeReverse(str1: str):
    for i in range(len(str1)-1, -1, -1):
        print(str1[i], end="")
    print()


str1 = input("Enter any string: ")
print("Reversed string: ")
iterativeReverse(str1)
