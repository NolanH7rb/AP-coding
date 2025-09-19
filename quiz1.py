# 1. In your own words, describe the differences between a linear search and a 
# binary search. Please write your response using complete sentences.
print('A binary search takes a list and repeadly splits it in half to find the median of the list' 
' while a linear search go through each string in a list one by one until the specific task assigned is answered.')

# 2. How many steps would it take to get to the desired number of 98 using linear search?
# Please write your response using complete sentences.
print('it would take 5 steps to reach 98 using linear search due to the 0 value being a starting number.')
listA = [10,24,34,35,67,98,101]

# 3. How many steps would it take to get to the desired number of 150 using a binary search?
# Please write your response using complete sentences.
print('Using binary search it should take 3 steps of breaking the list in half until 150 is the remaining number in the list.')
listB = [1,40, 44, 55, 70, 93, 99, 134, 145, 150, 200, 244]

# 4. In your own words describe what an algorithm is. 
# Please write your response using complete sentences.
print("An algorithm the the strucutre where a set of instructrions are written.")

# 5. A person and their family is visiting a medical building. the medical building has
# 10 floors. The patient that the person and their family is visiting is on the 7th floor 
# of the building. The family also knows what room they need to go to to visit the
# patient on the 7th floor. which big-O time complexity would best describe the steps it
# would for them to get to the desired room and why? 
# Please write your response using complete sentences.
print('O(1) would be the would best descirbe because their only 10 floors and already know the room number.')

# 6. You and your friends are headed out to a party, as you're preparing to walk out the door to meet with
# your pals, your realize you forgot your phone. you you can't remember exactly where you misplaced it 
# but you know it is in one of your pairs of pants. You have 10 pairs of paints. which big-O time complexity
# would best describe the steps it would take to find your phone?
# Please write your response using complete sentences.
print('O(nlogn) would best fit this scenario becuase it is the most efficent and the quicksort attributes helps also')

# 7. Create a class that will represent and create game console objects. 
# Your class should have 4 attributes and 3 methods. 
# Once you've created your class, create 2 unique video game consoles.
class weSellanyConsole:
    def __init__(self, name, color, GB, release, model ,):
        self.name = name
        self.color = color
        self.GB = GB
        self.release = release
        self.model = model


    def printInfo(self):
        print('heres your future Console!')
        print('Name:   '+ self.name)
        print('Color:   '+ str(self.color))
        print('Giggabytes:  '+ str(self.GB))
        print('Release:  '+ str(self.release))
        print('Model:  '+ str(self.model))


Console1 = weSellanyConsole('Playstation 5','White','825GB','November 10th, 2020','slim')
Console2 = weSellanyConsole('Xbox series Y','Black','802GB','November 12th, 2020','wide')
print(Console1)
Console1.printInfo


# 8. Create a class that will represent a video game for your console.
# Your class should have 4 attributes and 3 methods objects.
# ONCE You've created your class, create 2 unique video games objects.. 
