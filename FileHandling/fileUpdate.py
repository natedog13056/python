# a. write a sentence to 'data1A.txt': 'This is content in data1A file.'

f = open('folder1A/data1A.txt', 'w')
f.write('This is content in data1A file.')
f.close()

# b. write a sentence to 'data2A.txt': 'This is content in data2A file.'
f = open('folder1A/folder2A/data2A.txt', 'w')
f.write('This is content in data2A file.')
f.close()

''' c. write 3 sentences to 'data3A.txt': 
		'This is content in data3A file.'
		'My content is supposed to copy to another file'
		'Do you really know how to do it ?' '''
f = open('folder1A/folder2A/folder3A/data3A.txt', 'w')
f.write('This is content in data3A file.\n')
f.write('My content is supposed to copy to another file\n')
f.write('Do you really know how to do it ?')
f.close()

# c. copy all content from 'data3A.txt' to 'data2B.txt'
f1 = open('folder1A/folder2A/folder3A/data3A.txt', 'r')
f2 = open('folder1A/folder2B/data2B.txt', 'w')

for line in f1:
    f2.write(line)

f1.close()
f2.close()