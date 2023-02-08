"""
Understanding class and instance attributes

- an instance attribute's value is specific to a particular instance.
- a class attribute is available from the class itself, and all instances derived from that class.
"""

class Doggo:
    species = "Canis familiaris"  # Class attribute
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        
"""
>>> class Doggo:
...     species = "Canis familiaris"
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...
>>> Doggo.species
'Canis familiaris'
>>> Doggo
<class '__main__.Doggo'>
>>> Doggo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Doggo.__init__() missing 2 required positional arguments: 'name' and 'age'
"""

class Point:
    dimensions = 2
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
"""
>>> class Point:
...     dimensions = 2
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...       
>>> Point.dimensions
2
>>> Point
<class '__main__.Point'>
"""