# Use the file name mbox-short.txt as the name
fname = input("Enter file name: ")
fh = open(fname)
ff = fh.read()
mino = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count+1
    lino = line.find(':')
    kino = float(line[lino+1:])
    mino = kino + mino
print('Average spam confidence:',mino/count)
