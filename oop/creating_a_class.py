"""
Naming Convention
 - CapitalizedWords
 - CamelCase
 - PascalCase
 
Class convention is to start off the class with 
a capital letter and no underscore or space between words.
"""

class Point:
    """ The class name is Point and it is a class object.
    
    >>> Point
    <class '__main__.Point'>
    """
    pass  # pass is a placeholder for code that is not yet written.


class Dog:
    pass

class Cat:
    pass


"""
We need classes when want to do object oriented programming.

How to store data?
Where to write code?
If your code operates on data, where do you place it? Same file? 
How to operate on data?
How do you determine one dictionary has a certain type of data?
Where to put the code that operates on data?

These are all things that classes can help with.

Classes are to make our lives easier as a developer.

Many situations where classes make your code easier to understand, write, and maintain.
"""

kirk = ["James T. Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

"""
Where do we put the extra fields?

How do we reference?

kirk[1]  # 34
spock[1]  # 35
mccoy[1]  # "Chief Medical Officer"

mccoy[1] doesn't make sense. We need to know what the data is.

If we were using classes.

kirk.age  # 34
spock.age  # 35
mccoy.age  # AttributeError
"""

x1 = 1
y1 = 2
point = (1, 2)

point[0] = 1  # x
point[1] = 2  # y

# Is point a list of points? 
# This can be confusing.
# It is common for programmers to write something and forget it when they come back later.

point.x = 1 
point.y = 2

# Less ambiguious automatically.

"""
A convenient structure to:
 - store and operate on data
 - encapsulate code

Classes to make your life as a developer easier.

You can over do classes. Classes aren't for every situation.

In Python you can use OOP or other types of programming.

If the class doesn't make sense, experiment without using them.

The key is to use them if you want to and understand what they can bring to your code.
"""

