file = open('Codingal.txt', 'r')
Counter = 0

Content = file.read()
Colist = Content.split("\n")
print(Colist)
Counter=len(Colist)

print("This is the number of lines in the file")
print(Counter)