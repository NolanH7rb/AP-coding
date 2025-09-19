numbers = [1,5,10,20,39,48,83,89,72,92] #min/max

def minMax():
    x = min(numbers)
    y = max(numbers)
    
    print(x, y)

minMax()

#txt = "ydlab"[::-1]
#print(txt)

#Create a function that will reverse the character in a string.
def reverseString(word):
    text = word[::-1]
    print(text)

reverseString('ydlab')