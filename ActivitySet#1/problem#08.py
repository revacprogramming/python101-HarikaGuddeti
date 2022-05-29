# Files

fname = "dataset/mbox-short.txt"

count = 0
average = 0
average=float(average)
fname = input("Enter file name:")
fh =open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        a=float(line[20:])
        average=average+a
        count=count+1
print("Average spam confidence:",average/count)
