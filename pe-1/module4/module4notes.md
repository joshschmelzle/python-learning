# PE-1 Module 4

## Functions

### Why do we need functions?

We've already made use of some __methods__, which are also functions, but declared in a very specific way.

We're going to talk about writing our own functions and how to use them. 

Functions are useful for particular pieces of codes that is repeated many times in our programs. Maybe there are only a few minor modifications. Maybe we're cloning the same code. 

If a particular fragment of code begins to appear in more than one place, consider the possibility of isolating it in the form of a function. And invoke that function from points where needed.

This simplifies the work of the program because pieces of code can be encoded separately and tested separately. This is often called decomposition. 

If a piece of code becomes so large that reading and understanding it may cause a problem, consider dividing the code into separate, smaller problems, and implementing each of them in the form of a separate function. 

This decomposition continues until you get a set of short functions, easy to understand and test.

### Decomposition

Sometimes problems are so large and complex that they cannot be assigned to a single developer, and a __team of developers__ have to work on it. 

It's not only about __sharing the work__, but also about __sharing the responsibility__ among many developers. 

Each developer writes a clearly defined and described set of functions, which when __combined into the module__ will give the final product.

If we're going to divide work among multiple programmers, __decompose the problem to allow the product to be implemented as a set of separately written functions packed together in different modules.__

### Where do functions come from?

- From Python itself (like `print()`) where numerous functions are an __integral part of Python__. These are functions that we call __built-in functions__.
- From Python's __preinstalled modules__. 
- __directly from your code__ - you can write your own functions, and place them inside your code, and use them freely. 

This means functions come from: python, modules, and code. 

### Defining a functions

How do we make a function? We have to define it. 

Simplest function definition looks like:

```python
def function_name():
    function_body
```

Rules:

- Functions always start with the __keyword__ `def` (for _define_)
- Next after `def` goes the __name of the function__ (naming rules are similar to variables)
- After the function name there is a place for a pair of __parentheses__.
- The line must be ended with a __colon__.
- The line after the `def` begins the __function body__ with at least one __nested instruction

We must insert the __function's invocation__ in order to use the function. Like this:

```python
function_name()
```

A __function__ is a block of code that performs a specific task when a function is called/invoked. Functions are used to make code reusable, better oganized, and more readable. Functions can have parameters and return values. 
