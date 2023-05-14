# PE1 - Module 1 

## Introduction

In this module, you will learn about:

- the fundamentals of computer programming, i.e., how the computer works, how the program is executed, how the programming language is defined and constructed;
- the difference between compilation and interpretation;
- what Python is, how it is positioned among other programming languages, and what distinguishes the different versions of Python.

## How does a computer program work?

A program makes a computer "usable". Without a program, a computer is an object. Like, without a player, a piano is nothing more than a wooden box. 

Computers are capable of performing very complex tasks. A computer can compute all sorts of things. But it is neccessary to instruct the computer.

## Natural languages vs. programming languages

A language is a means (and a tool) for expressing and recording thoughts. There are lots of languages all around us. Computers have their own language too. Called machine language. A computer is devoid of intelligence. You could say it's like a well-trained dog. Responding only to a predetermined set of known commands. The commands it recognizes are very simple. Stuff like "take the number, divide by another, and save the result". 

A complete set of commands is called an *instruction list*, aka *IL*.

Machine languages are developed by humans.

Computers cannot yet create their own language. Just as people use different languages, so do machines. The difference is human language is developed naturally. New words are created. Old words are disappear. These languages are called natural languages. 

## What makes a language? 

We can say a langauge consists of the following elements:

- an **alphabet**: a set of symbols used to build words of a certain language
- a **lexis**: (aka a dictionary) a set of words the language offers its users 
- a **syntax**: a set of rules (formal or informal, written or felt intuitively) used to determine if a certain string of words forms a valid sentence
- **semantics**: a set of rules determining if a certain phrase makes sense (e.g.. "I ate a doughnut" makes sense, but "A doughnut ate me" doesn't)

The **IL** is, in fact, **the alphabet of a machine language**. This is the simplest and most primary set of symbols we can use to give commands to a computer. It's the computer's mother tongue.

Unfortunately, this mother tongue is a far cry from a human mother tongue. We both (computers and humans) need something else, a common language for computers and humans, or a bridge between the two different worlds.

We need a language in which humans can write their programs and a language that computers may use to execute the programs, one that is far more complex than machine language and yet far simpler than natural language.

Such languages are often called high-level programming languages. They are at least somewhat similar to natural ones in that they use symbols, words and conventions readable to humans. These languages enable humans to express commands to computers that are much more complex than those offered by ILs.

A program written in a high-level programming language is called a source code (in contrast to the machine code executed by computers). Similarly, the file containing the source code is called the source file.

## Compilation vs. interpretation

There are two different ways of transforming a program from a high-level programming language into machine language:

**COMPILATION** - the source program is translated once (however, this act must be repeated each time you modify the source code) by getting a file (e.g., an .exe file if the code is intended to be run under MS Windows) containing the machine code; now you can distribute the file worldwide; the program that performs this translation is called a compiler or translator;

**INTERPRETATION** - you (or any user of the code) can translate the source program each time it has to be run; the program performing this kind of transformation is called an interpreter, as it interprets the code every time it is intended to be executed; it also means that you cannot just distribute the source code as-is, because the end-user also needs the interpreter to execute it.

Due to some very fundamental reasons, a particular high-level programming language is designed to fall into one of these two categories.

There are very few languages that can be both compiled and interpreted. Usually, a programming language is projected with this factor in its constructors' minds - will it be compiled or interpreted?

## What does this all mean for you?

- Python is an interpreted language. This means that it inherits all the described advantages and disadvantages. Of course, it adds some of its unique features to both sets.
- If you want to program in Python, you'll need the Python interpreter. You won't be able to run your code without it. Fortunately, Python is free. This is one of its most important advantages.

Due to historical reasons, languages designed to be utilized in the interpretation manner are often called scripting languages, while the source programs encoded using them are called scripts.

## What is Python?

Python is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming.

And while you may know the python as a large snake, the name of the Python programming language comes from an old BBC television comedy sketch series called Monty Python's Flying Circus.

At the height of its success, the Monty Python team were performing their sketches to live audiences across the world, including at the Hollywood Bowl.

Since Monty Python is considered one of the two fundamental nutrients to a programmer (the other being pizza), Python's creator named the language in honor of the TV show.

## Who created Python?

One of the amazing features of Python is the fact that it is actually one person's work. Usually, new programming languages are developed and published by large companies employing lots of professionals, and due to copyright rules, it is very hard to name any of the people involved in the project. Python is an exception.

There are not many languages whose authors are known by name. Python was created by Guido van Rossum, born in 1956 in Haarlem, the Netherlands. Of course, Guido van Rossum did not develop and evolve all the Python components himself.

## Python goals

In 1999, Guido van Rossum defined his goals for Python:

- an easy and intuitive language just as powerful as those of the major competitors;
- open source, so anyone can contribute to its development;
- code that is as understandable as plain English;
- suitable for everyday tasks, allowing for short development times.

## What makes Python special?

Python is easy to learn, teach, use, understand, and obtain.

Drawbacks include it is not a speed demon and in some cases it may be resistant to simpler testing techniques.

## Python rivals?

Python has two direct competitors, with comparable properties and predispositions. These are:

- Perl – a scripting language originally authored by Larry Wall;
- Ruby – a scripting language originally authored by Yukihiro Matsumoto.

## Why not Python?

Despite Python's growing popularity, there are still some niches where Python is absent, or is rarely seen:

- low-level programming (sometimes called "close to metal" programming): if you want to implement an extremely effective driver or graphical engine, you wouldn't use Python;
- applications for mobile devices: although this territory is still waiting to be conquered by Python, it will most likely happen someday.

## There is more than one Python

Python 3 is the newer (or to be more precise, the current) version of the language. It's going through its own evolutionary path, creating its own standards and habits.

All the code samples you will find during the course have been tested against Python 3.4, Python 3.6, Python 3.7, and Python 3.8.

## Python aka CPython

In addition to Python 2 and Python 3, there is more than one version of each.

Guido van Rossum used the "C" programming language to implement the very first version of his language and this decision is still in force. All Pythons coming from the PSF are written in the "C" language. There are many reasons for this approach. One of them (probably the most important) is that thanks to it, Python may be easily ported and migrated to all platforms with the ability to compile and run "C" language programs (virtually all platforms have this feature, which opens up many expansion opportunities for Python).

This is why the PSF implementation is often referred to as CPython. This is the most influential Python among all the Pythons in the world.

## Cython

Another Python family member is Cython.

Cython is one of a possible number of solutions to the most painful of Python's traits – the lack of efficiency. Large and complex mathematical calculations may be easily coded in Python (much easier than in "C" or any other traditional language), but the resulting code execution may be extremely time-consuming.

How are these two contradictions reconciled? One solution is to write your mathematical ideas using Python, and when you're absolutely sure that your code is correct and produces valid results, you can translate it into "C". Certainly, "C" will run much faster than pure Python.

This is what Cython is intended to do – to automatically translate the Python code (clean and clear, but not too swift) into "C" code (complicated and talkative, but agile).

## Jython

Another version of Python is called Jython.

"J" is for "Java". Imagine a Python written in Java instead of C. This is useful, for example, if you develop large and complex systems written entirely in Java and want to add some Python flexibility to them. The traditional CPython may be difficult to integrate into such an environment, as C and Java live in completely different worlds and don't share many common ideas.

Jython can communicate with existing Java infrastructure more effectively. This is why some projects find it useful and necessary.

## PyPy and RPython

Take a look at the logo below. It's a rebus. Can you solve it?

It's a logo of the PyPy - a Python within a Python. In other words, it represents a Python environment written in Python-like language named RPython (Restricted Python). It is actually a subset of Python.

The source code of PyPy is not run in the interpretation manner, but is instead translated into the C programming language and then executed separately.

This is useful because if you want to test any new feature that may be (but doesn't have to be) introduced into mainstream Python implementation, it's easier to check it with PyPy than with CPython. This is why PyPy is rather a tool for people developing Python than for the rest of the users.

This doesn't make PyPy any less important or less serious than CPython, of course.

In addition, PyPy is compatible with the Python 3 language.

There are many more different Pythons in the world. You'll find them if you look, but this course will focus on CPython.

## How to get Python and how to use it

Linux users probably already have Python installed. If you type `python3` and press *Enter* you should see something like this:

```
 python-learning git:(main) python3
Python 3.11.3 (main, Apr  7 2023, 20:13:31) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```