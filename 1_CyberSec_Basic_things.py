import string;
import random;

passwordList=list()
functionIterator=list()
functionCount=0

def generatePassword(length: int=16):
    alphabet=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(alphabet)for i in range(length))
    passwordList.append(password)
    global functionCount
    functionIterator.append(functionCount)
    functionCount+=1

    return password

password=generatePassword()
print(f"Password generated: {password}")
password=generatePassword()
print(f"Password generated: {password}")
password=generatePassword()
print(f"Password generated: {password}")
print(f"\n Number of function calls: {functionCount}")
print(passwordList)
print(functionIterator)

passwordDict={}
for i in functionIterator:
    passwordDict[i]=passwordList[i]    

print("Password Dictionary:")
print(passwordDict)
print("Password with the iterator 1: " + passwordDict.get(1))
