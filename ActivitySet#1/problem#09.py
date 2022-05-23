# Lists

fname = "dataset/romeo.txt"


fname = input("Enter filename: ")
fhand = open(fname)
lst = list()
for line in fhand:
    l= line.split()
    for i in l:
        if i in lst:
            continue
        else:
            lst.append(i)
lst.sort()            
print(lst)

#for i in l:
#if i not in lst:
     #lst.append(i)