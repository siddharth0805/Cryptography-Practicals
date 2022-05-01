word=input("Enter a word : ")
key=int(input("Enter the key : "))
nwword=""
ascii=nwa=0
for i in word:
    if  i.isupper():
        ascii=ord(i)
        nwa=(ascii-key-65)%26+65
    elif i.islower():
        ascii=ord(i)
        nwa=(ascii-key-97)%26+97
    else:
        nwa=ord(i)
    nwword+=chr(nwa)     
print(nwword)