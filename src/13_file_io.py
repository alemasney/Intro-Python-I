"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

f = open('foo.txt', 'r')

print(f.read())
print(f.close())
print(f.closed)
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

j = open('bar.txt', 'w')
    j.write('I love to learn new languages')
    # j.write('Soccer is awesome')
    # j.write('Spider-man')
    # j.read()
    # j.close()

print(j)