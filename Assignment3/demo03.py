#Define a procedure histogram() that takes a list of 
#integers and prints a histogram to the screen. For example,
# histogram([4, 9, 7]) should print the following:

#   ```
#   4: ****
#   9: *********
#   7: *******
#   ```

def histogram(n):
    for item in n:
        result="*" * item
        print(result)
histogram([4,9,7])        