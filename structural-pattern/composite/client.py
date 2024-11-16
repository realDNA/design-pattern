from leaf import File
from composite import Directory

file1 = File("file1.txt", 1000)
file2 = File("file2.txt", 2000)
file3 = File("file3.txt", 3000)
file4 = File("file4.txt", 4000)

dir1 = Directory("dir1")
dir2 = Directory("dir2")

dir1.add(file1)
dir1.add(file2)
dir2.add(file3)
dir2.add(file4)

root = Directory("root")
root.add(dir1)
root.add(dir2)
root.display()

print(f"Total Size: {root.getSize()} bytes")
