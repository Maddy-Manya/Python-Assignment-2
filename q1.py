def countOccurence(str1: str, str2: str) -> int:
    str1 = str1.lower()
    str2 = str2.lower()
    count = 0

    for i in str1:
        count += str2.count(i)

    
    return count

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
print("Count :", countOccurence(str1,str2))