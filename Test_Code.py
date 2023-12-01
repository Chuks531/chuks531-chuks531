Input_Output def:

n1 = input('First number is: ')
n2 = input('Second number is: ')
user_sum = float(n1) + float(n2)
print("The sum of " + str(n1) + " and " + str(n2) + " is " + str(user_sum))


Args_Python.py:
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
        return sum
    
print(sum_of(4, 5, 6))


a  =  5
b  =  6
sum1 = a + b

c  = 6
d  = 9
sum2 = c + d
total_sum = (sum1 + sum2)
print(total_sum)

def sum(a, b):
    return a + b
    print(sum(5, 10))
    print(sum(4, 11))


# Algorithm for a Palindrome

def ispalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True


print(ispalindrome('racecar'))


coffees = ['Espresso', 'Latte', 'Cappuccino', 'Macchiato', 'Americano', 'Decaf']
def reverse(str):
    return str[::-1]
    reversed_coffees = map(reverse, coffees)
    for x in reversed_coffees:
        print(x)



Recursion_Code:

# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')




# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')


class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house


class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house

house = House()
print(house.num_rooms)
print(House.num_rooms)

house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)


class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost



house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)



Exercise: Instantiate a custom Object
This is your first experience creating classes and objects in Python. You will be following a sequential process where you will create a class, define its state by creating variables and functions to define its attributes and behavior, and then instantiate it using some variable. Finally, you will use the class members to get the desired output.

Follow the steps to build and run your program in the environment provided at the bottom of the reading.


Step 1
1.1 Define a class called MyFirstClass.

1.2 Add a print statement inside it such as “Who wrote this?”.

Step 2
Create a string variable named index and initialize it with a string “Author-Book”.

Step 3
3.1 Define a function called hand_list() with the help of def keyword. 

3.2 Pass the parameter  self to it. And then pass two parameters, philosopher and book to it.

Step 4
4.1 Write a print statement using the print() function and pass the class variable by accessing it. 

Hint: Class variables are accessed directly by calling it over the class name using dot notation.

4.2 Write a print statement that will give output such as: “Plato wrote the book: Republic” where “Plato” is the philosopher and “Republic” is the book. 

Hint: You can make use of the built-in (+) concatenation operator to join these strings. 

Step 5
5.1 Create and instantiate an object of that class, called whodunnit

5.2 Call method hand_list() over this object “whodunnit” and pass two values to it namely “Sun Tzu” and “The Art of War”.

Rough test work for the above:
# Define class MyFirstClass

    # Define string variable called index
    
    # Define function hand_list()
    
        # variable + “ wrote the book: ” + variable
        

# Call function handlist()


Solution to above:

# Sample Solution code
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")