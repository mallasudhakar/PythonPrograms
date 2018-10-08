# Usage of finally in Exception handling in Python.
#create a file with name hello in write mode
try:
    f=open("hello.txt","w")
    #here file is created and generated ZeroDivisionError
    x=1/0
except FileNotFoundError:
    print("First create the file")
finally:
    #This block is always executed.
    f.close()
    
