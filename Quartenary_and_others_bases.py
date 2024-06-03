#Representação de um número pela base quartenária - Representation of a number in the quartenary base
b = 4 #base quartenária - quartenary base
I = int(26.625) #valor inteiro da parte decimal/fracionário - integer value of the fracionary value
d_int = [] 
while (I != 0): 
    d_int.insert(0, I % b) 
    I //= 4 
print('(',*d_int,')_4',sep='') #a parte inteira - inter part
F = 26.625 % 1
d_fra = []
while (F != 0):
     F *= b
     d_fra.append(int(F)) 
     F %= 1 
print('(0,',*d_fra,')_4',sep='') #a parte fracionário - fracionary part
print('(',*d_int,',',*d_fra,')_',b, sep='') #resultant part

#Representação de um número na base hexadecimal(16) - Representation of a  number in the hexadecimal base
b = 16  #base hexadecimal - hexadecimal base
digs = "0123456789ABCDEF" #digitos - digits
x = 3245.875  #numero - number
I = int(x)  #valor inteiro da parte fracionária - integer part of the fracionary part
di = [] 
while (I != 0): 
     di.insert(0, I % b) 
     I //= b 
  
F = x % 1 #parte fracionária - fracionary part
df = [] 
while (F != 0): 
     F *= b 
     df.append(int(F)) 
     F %= 1 
print('(',*[digs[d] for d in di], ',',*[digs[d] for d in df],f')_{b}',sep='')#resultant part

