
def CopyFile(Source,Destination):
     fsrc=open(Source,"r")
     fdst=open(Destination,"w")
     Data=fsrc.read()
     fdst.write(Data)
     fsrc.close()
     fdst.close()




def main():
     src =input("Enter existing file name: ")
     dst =input("Enter new file name")
     CopyFile(src,dst)





if __name__=="__main__":
     main()