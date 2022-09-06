# read and print content of files data2A.txt and data2B.txt

f = open('folder1A/folder2A/data2A.txt', 'r')
print(f.read())
f.close()

f = open('folder1A/folder2B/data2B.txt', 'r')
print(f.read())
f.close()