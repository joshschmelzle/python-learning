"""
.__init__() is a special method that is called when an object is created.

The dunder.

d for Double and under for underscore.

Thus the .__init__() can just be called the dunder init constructor in speaking.

Functions part of classes are called methods.

So, .__init__() is a method.

Attributes are where information lives in classes.

The self parameter is used to refer to the instance of the class.
"""

class Point:
    def __init__(self, x, y):
        """ The first parameter is always self. 
        You can actually call it something else, but by convention. Use self.
        """
        
        # We're defining a point. So, use x and y.
        
        # To assign x, y to the instance of the object. We use self and the attribute.
        self.x = x
        self.y = y

class Cat:
    def __init__(self, name, age):
        """
        What is "self"?
        
        self refers to the instance of the class.
        
        On "its self"
        
        A name commonly given to the first argument passed to the constructor
        
        A convention to call it self and you can call it something else
        
        Don't call it something else
        """
        self.name = name
        self.age = age
        
        
        
"""
>>> class Cat:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...
>>> Cat
<class '__main__.Cat'>
>>> Cat()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Cat.__init__() missing 2 required positional arguments: 'name' and 'age'
>>> cat = Cat("Dougie", 10)
>>> cat
<__main__.Cat object at 0x00000213C520B550>
>>> cat.age
10
>>> cat.name
'Dougie'
"""