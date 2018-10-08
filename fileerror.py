try:
    f=open("hello.txt","w")
    x=1/0
except FileNotFoundError:
    print("First create the file")
finally:
    f.close()
    
