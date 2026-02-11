print("Hello Monu\"s World")
strr='vishnuuu'
#use \ or "" '' accordingly
#for multi line string use  ''' '''
print('''
      hey
      Mona''')
#to print length
print(len('Monaa hahah'))
#to print particular char
print(strr[1]) #0based indexing
#to print a slice 
print(strr[0:3]) #lower inclusive upper excluded
print(strr.upper()) #similarly lower()
print(strr.count('u')) #count of particular char/str
print(strr.find('nu')) #prints the index where that substr starts

strr=strr.replace('u','a') #doesnot change inplace--have to return it and store another value
print(strr)

#concatenation

print('hello '+ strr)

#fstrings using placeholders
print(f'hello {strr}!! cutieee')

print(dir(strr)) #shows all attributes/methods associated to this
print(help(strr.lower))