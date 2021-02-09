def stutter(mystring):
    return mystring[:2]+".. "+mystring[:2]+".. "+mystring+"?"

if __name__=="__main__":
    mystring=input("Enter string to stutter")
    s=stutter(mystring)
    print(s)
