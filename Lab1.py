alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
change = int(input('Шаг замещения: '))
text = input("Tekct для шифровки: ").upper()    
result = ''   
for i in text:
    place = alphabet.find(i)
    next_place = place + change
for i in text:
    place = alphabet.find(i)
    next_place = place + change
if i in alphabet:
    result += alphabet[next_place] 
else:
    result += i
print (result)
