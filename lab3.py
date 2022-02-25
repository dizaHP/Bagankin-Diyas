alf= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key = int(input("vvedite klych:"))
text = (input('Text for crypt:'))
for i in range(0,len(alf):
               
    a = key.index[i+1]
    b = (a*7)%26
    print(b)
def unshift(key, ch):
   offset = ord(ch) - ASC_A
   return chr(((key[0] * (offset + key[1])) % WIDTH) + ASC_A)
