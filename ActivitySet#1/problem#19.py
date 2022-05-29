#lists 2
count=0
fname=input("enter the file name:")
fhand = open(fname)
for line in fhand:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
           count=count+1
           lst=line.split()
           print(lst[1])
print("There were", count, "lines in the file with From as the first word")

#split used for printing second word
#print second word in line i.e line[1]
#count used at the end 