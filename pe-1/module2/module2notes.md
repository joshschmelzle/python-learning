# Module 2

## Integers

Let's say numbers are handled by modern computers are of two types.

- __integers__ which is numbers that are devoid of the efractional part
- and __floating-point__ number (or __floats__) that contain or are able to contain the fractional part.

```python
>>> type(1)
<class 'int'>
>>> type(1.1)
<class 'float'>
```

We can write numbers like `11111111` or `11_111_111`.

```python
>>> 11111111 == 11_111_111
True
```

What about negative numbers?

```python
>>> -11_111_111 == -11111111
True
```

What about positive numbers? We can precede them with a plus sign but we don't need to. 

```python
>>> +11_111_111 == 11111111
True
```

## Octal and hexadecimal numbers

Two additional conventions found in Python.

### 1. Octal

If an integer is preceded by an `0O` or `0o` prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the `[0..7]` range only.

For example `0o123` is an __octal__ number with a decimal value of `83`.

```python
>>> type(0o123)
<class 'int'>
>>> 0o123 == 83
True
>>> print(0o123)
83
```

### 2. Hexadecimal

Hexadecimal numbers are preceded with the `0x` or `0X` (zero-x) prefix.

`0x123` is a __hexadecimal__ number with a decimal value equal to 291. 

```python
>>> 0x123
291
>>> type(0x123)
<class 'int'>
>>> print(0x123)
291
```

## Floats

Floats are designed to represent and store numbers that have a __non-empty decimal fraction__.

```python
>>> 2.5
2.5
>>> -0.4
-0.4
>>> type(2.5)
<class 'float'>
>>> type(-0.4)
<class 'float'>
>>> .4 == 0.4
True
>>> 4. == 4
True
>>> 4.
4.0
>>> .4
0.4
>>> type(4.)
<class 'float'>
>>> type(4)
<class 'int'>
```

## Ints versus floats

Decimal points are important in recognizing floating-point numbers in Python.

`4` is an integer.

```python
>>> type(4)
<class 'int'>
```

`4.0` is a floating-point.

```python
>>> type(4.0)
<class 'float'>
```

The point is what makes a float.

There is also other ways to make a float. You can use the letter `e` to make a float.

```python
>>> 300000000
300000000
>>> 3e8
300000000.0
>>> 300000000 == 3e8
True
```

Python automatically chooses the more economical form of the number's presentation. Take this into consideration when creating literals.

```python
>>> 0.0000000000000000000001
1e-22
>>> 6.62607E-34
6.62607e-34
```

## Strings

Strings are used when you need to process text. Strings need quotes like the way floats need points.

```python
>>> "I am a string"
'I am a string'
>>> type("I am a string")
<class 'str'>
```

Don't forget about escape characters when working with strings. Remember that these are backslashes. The backslash can also escape quotes!

```python
>>> "I like \"Monty Python\""
'I like "Monty Python"'
```

Python can also use an apostrophe instead of a quote. Either of these may delimit strings, but you must be consistent. 

If you open a string with a quote, you have to close it with a quote. If you start a string with an apostrophe, you have to end it with an apostrophe. 

```python
>>> "I like \"Monty Python\""
'I like "Monty Python"'
>>> 'I like "Monty Python"'
'I like "Monty Python"'
```

## Boolean values

Booleans are used to represent an abstract value - __truthfulness__.

Each time you ask Python if one number is greater than another, the question results in the creation of some specific data... a __boolean__ value.

The name comes from George Boole (1815-1864) who defined __boolean algebra__ which makes use of only two distinct values. `True` and `False`, denoted as `1` and `0`.

```python
>>> True > False
True
>>> True < False
False
```

## Operators

```python
>>> 3
3
>>> 3+3
6
>>> 3-3
0
>>> 3*3
9
>>> 3/3
1.0
>>> 3//3
1
>>> 3%3
0
>>> 3**3
27
```

### Exponentation

A `**` (double asterisk) is a sign of exponentiation (power) operator.

Classical mathematics prefers notation with superscripts. Pure text editors don't accept that, so Python uses `**` instead.

```python
>>> 2**3
8
>>> 2**3.
8.0
>>> 2.**3
8.0
>>> 2.**3.
8.0
```

### Multiplication

An `*` (asterisk) sign is a __multiplcation__ operator. 

```python
>>> 2*3
6
>>> 2*3.
6.0
>>> 2.*3
6.0
>>> 2.*3.
6.0
```

### Division

A `/` (slash) sign is a __divisional__ operator.

```python
>>> 6/3
2.0
>>> 6/3.
2.0
>>> 6./3
2.0
>>> 6./3.
2.0
```

Division operator is always a float.

### Integer Division

A `//` (double slash) sign is an __integer divisional__ operator. 

```python
>>> 6//3
2
>>> 6//3.
2.0
>>> 6.//3
2.0
>>> 6.//3.
2.0
>>> 7/3
2.3333333333333335
>>> 7//3
2
>>> 6//4
1
>>> 6.//4
1.0
>>> 6/4
1.5
>>> 6./4
1.5
```

Important! __rounding always goes to the lesser integer__.

### Remainder (modulo)

The `%` (percent) sign is the remainder (modulo) operator.

The result of the operator is a __remainder left after the integer division__.

```python
>>> 14%4
2
>>> 14//4
3
>>> 3*4
12
>>> 14-12
2
>>> 12%4.5
3.0
```

As you probably know, __division by zero doesn't work__.

#### Addition

The __addition__ operator is the `+` (plus) sign.

```python
>>> -4 + 4
0
>>> -4. + 8
4.0
```

### Operators in their priorities

Often you will find more than one operator in one expression. 

Python precisely defines the priorities of all operators, and assumes that the operators of larger (higher) priority perform their operations before the operators of a lower priority.

Consider `2 + 3 * 5` as an expression.

So, if `*` has a higher priority than `+`, the computation of the final result should be obvious - `17`.

```python
>>> 2 + 3 * 5
17
```

### Operators and their bindings

The __binding__ of the operator determines the order of computations performed by some operators with equal priority, put side by side in one expression.

Most of Python's operators have left-sided binding, which means that the calculation of the expression is conducted from left to right.

```python
>>> 9 % 6 % 2
1
```

```
>>> 2**2
4
>>> 4**3
64
>>> 2**2**3
256
```

Exponentiation operator uses right-sided binding.

### List of priorities

1. `**`
2. `+`, `-` (unary)
3. `*`, `/`, `//`, `%`
4. `+`, `-` (binary)

```python
>>> 2*3%5
1
```

### Operators and parentheses

You can use __parentheses__ to change the natural order of calculation.

__Subexpressions in parentheses are always calculated first__.

```python
>>> (5 * ((25 % 13) + 100) / (2 * 13)) // 2
10.0
```

```python
>>> (2 ** 4), (2 * 4.), (2 * 4)
(16, 8.0, 8)
>>> (-2 / 4), (2 / 4), (2 // 4), (-2 // 4)
(-0.5, 0.5, 0, -1)
>>> (2 % -4), (2 % 4), (2 ** 3 ** 2)
(-2, 2, 512)
```

### Correct and incorrect variable names

Correct (but not always convenient).

`MyVariable`, `i`, `counter`, `days_to_christmas`.

Incorrect.

`10t` (does not begin with a letter), `Exchange Rate` (contains a space).

PEP 8 recommends:

- variable names should be lowercase, with words separated by underscores to improve readability. 
- function names follow the same convention as variable names
- use mixed case in contexts where there is already a prevailing style. 

### Keywords 

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

These are __keywords__ or __reserved keywords__. They are reserved because __you can't use them as names__. 

### Creating variables

A variable comes into existence as a result of assigning a value to it.

### Using variables

You can use as many variable declarations you need to achieve your goal.

You're __not allowed to use a variable which doesn't exist__ or in other words, a variable that was not assigned a value.

```python
>>> foo = 1
>>> print(bar)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bar' is not defined
```

We tried to use a variable (`bar`) which doesn't have any value.

### Assigning a new value to an already existing variable

The equal sign is used as an `assignment operator`. It assigns the value of its right argument to the left.

```python
>>> var = 1
>>> var
1
>>> var = var + 1
>>> var
2
>>> var = 100
>>> var = 200 + 300
>>> var
500
```

### Shortcut operators

There are some operators that make a developer's life easier.

Often we want to use one and the same variable both to the right and left sides of the `=` operator`. 

```python
x = x * 2
sheep = sheep + 1
```

We can shorten the way of writing the operators like this:

```python
x *= 2
sheep += 1
```

`variable = variable op expression`

`variable op= expression`

`i = i + 2 * j` == `i += 2 * j`