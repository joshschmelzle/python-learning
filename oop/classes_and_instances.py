"""
A class can be thought of a blueprint, protoype, or model.

An instance is a specimen, occurence, or occasion.

A blueprint for a car and an instance would be the actual car.

A class would be the mammal canis familiaris and the instance would be your dog spike.

A class would be the concept of a point in two-dimensional space and the instance would be the center of a canvas.

A class is like a blueprint.

An instance is like something made from the blueprint.

Analogies are limited! None of these analogies fully encapsulate the concept of a class and instance.
"""

class Point:
    """
    >>> Point
    <class '__main__.Point'>
    
    The brackets "()" instantiates the class. 
    >>> Point()
    <__main__.Point object at 0x00000213C520AF90>
    >>> Point()
    <__main__.Point object at 0x00000213C520AE50>
    
    The two point objects have different memory addresses.
    
    They are two different instances of the Point class.
    """
    pass


"""
>>> class Cat:
...     pass
...
>>> Cat
<class '__main__.Cat'>
>>>
>>> Cat() 
<__main__.Cat object at 0x00000213C520AF10>
>>> Cat()
<__main__.Cat object at 0x00000213C520B050>
>>> Cat()
<__main__.Cat object at 0x00000213C520AF10>
>>> Cat()
<__main__.Cat object at 0x00000213C520B050>


You can create many instances of a class.

They will be unique as they live at separate places in memory.

Empty classes can be useful as naming a thing, but you want to add attributes and methods.
"""

