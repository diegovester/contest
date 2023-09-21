# Question 2: FunFunFunctions — 3 points


# the following code outputs: ee ll ll oe
# How to modify the code such that it outputs: He eH lo ll ol 

def recursive(s,i):
    if i<len(s):
        print(s[i]+s[-i])
        recursive(s,i+1)
    return

def main():
    s="Hello"
    i=1
    recursive(s,i)
    return
main()

