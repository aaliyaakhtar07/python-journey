s1="Hello"
s2="World"
s3=s1+" "+s2  #String concatenation
s4=s1*3  #String repetition
s5=s1[0]  #Accessing first character
s6=s1[1:4]  #Slicing the string
print('H' in s1) #membership operaator
print("Concatenated String:", s3)
print("Repeated String:", s4)
print("First Character:", s5)
print("Sliced String:", s6)
s="   Hello World   "
print("String with leading/trailing whitespace:", s)    
print(s.strip())  #Removing leading/trailing whitespace
print(s.lstrip())  #Removing leading whitespace
print(s.rstrip())  #Removing trailing whitespace
print(s1.upper())  #Converting to uppercase
print(s1.lower())  #Converting to lowercase
t="Hello!$I$am$Aaliya"
print(t.split('$'))  #Splitting the string by '$'
print(t.rsplit('$'))  #Splitting the string from the right by '$'
l=['H','e','l','l','o']
print(''.join(l))  #Joining the list elements into a string
a="I love to eat mangoes"
print(a.replace(" ", "_"))  #Replacing spaces with underscores
