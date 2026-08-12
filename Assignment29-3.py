import sys
source_file=sys.argv[1]
file1=open(source_file,"r")
data=file1.read()

file1.close()

file2=open("Demo.txt","w")
file2.write(data)
file2.close()

print("Contents copied successfully")