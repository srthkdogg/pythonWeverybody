fname = input("Enter file name: ")
fh = open(fname)
x = 0
y = 0
oneword = list()
emptylist = list()
newlist = list()
for line in fh:
    x = x + 1
    line = line.rstrip()
    splitline = line.split()
    for element in splitline:
        if element in emptylist : continue
        emptylist.append(element)
        emptylist = sorted(emptylist)
print(emptylist)

#newlist = sorted(n)




#sorts the new list in A B C order


#print("line.rstrip()", line.rstrip())
#print("lst", lst)
#print("lst[1:]", lst[1:])
    #splitlst = lst.split()
#print("splitlst", splitlst)


#print(lst.rstrip(lst))
#print(line)
#print(line.rstrip())