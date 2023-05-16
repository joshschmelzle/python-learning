# PE1 - Module 2

## Introduction

Data types, variables, basic input-output operations, basic operators.

This module is about writing and running simple Python programs, what Python literals, operators, and expressions are, what variables are, and how to perform basci input and output operations.

The first thing we did was play with the print function.

```python
>>> print
<built-in function print>
>>> print()

>>> print("Hello world!")
Hello world!
```

The first "program" consists of:

- the word print;
- an opening parenthesis;
- a quotation mark;
- a line of text: Hello, World!;
- another quotation mark;
- a closing parenthesis.

In this case print is the **function name**. The meaning comes from the context in which the word is used.

A function in this context is a separate part of computer cost able to:

- **cause some effect** like sending text to a terminal. drawing an image. playing a sound.
- **evaluate a value** and **return it as the functions result**.

Python functions may come from Python itself. These would be referred to as built-in functions.

Python functions may come from add-ons named **modules**. Some modules come with Python and others may require separate installation. 

Python functions may be ones that you write yourself. Placing as many functions as you want and need inside your program to make it simpler, clearer, and more elegant.

The name of a function should be **significant**. For example, the name of the print function is self-evident. You should consider carefully the choice of names for functions you write.

A function may have an **effect** and a **result**, but there is a third part of functions. The **argument**(s).

Some Python functions don't need arguments. For syntax, Python functions strongly demand the presence of **a pair of parentheses**. Opening and closing ones.

If you want to add one or more arguments to a function, you would place them **inside the parentheses**.

## The `print()` function

The only argument delivered to the `print()` function in this example is a **string**:

```python
print("Hello, World!")
```

The function name (**print** in this case) along with the parentheses and argument(s), forms the **function invocation**. 

What happens when Python encounters an invocation like this one?

```python
function_name(argument)
```

First, Python checks to see if the name specified is **legal**. Which means Python browses the internal data in order to find an existing function of the name; if the search fails, Python aborts the code.

Second, Python checks if the function's requirements for the number of arguments **allows you to invoke** the function this way. Like if a specific function demands exactly two arguments any invocation delivering only one argument will be considered erroneous, and will abort the code's execution.

Third, Python **leaves your code for a moment** and jumps into the function you want to invokve.

Fourth, the function **executes its code**, causes the desired effect (if any), evaluates the desired result(s) (if any) and finishes its task.

Finally, Python **returns to your code** to the place just after the invocation) and resumes its execution.

