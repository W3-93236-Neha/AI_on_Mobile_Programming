#Create a tuple to store information of a person. 
#Reverse the tuple (in a new tuple) and print it.

def Person():
    info=("Neha",30,"Software Engineer","Pune","9767654355")
    print("original tuple:",info)
    reverseInfo=info[::-1]
    print("Reverse tupple value is",reverseInfo)

Person()    