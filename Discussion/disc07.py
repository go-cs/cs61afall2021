'''
Author: your name
Date: 2022-02-13 13:58:45
LastEditTime: 2022-02-13 17:39:31
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Discussion\disc07.py
'''
class Student:

    max_slip_days = 3 # this is a class variable

    def __init__(self, name, staff):
        self.name = name # this is an instance variable
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_slip_days(self, student, days):
        student.max_slip_days = days
"""
    >>> callahan = Professor("Callahan")
    >>> elle = Student("Elle", callahan)
    Added Elle
    >>> elle.visit_office_hours(callahan)
    Thanks, Callahan
    >>> elle.understanding
    1   
    >>> [name for name in callahan.students]
    ['Elle']
    >>> x=Student("Vivian", Professor("Stromwell")).name
    Added Vivian
    >>> x
    'Vivian'
    >>> [name for name in callahan.studets]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'Professor' object has no attribute 'studets'
    >>> [name for name in callahan.students] 
    ['Elle']
    >>> elle.max_slip_days
    3
    >>> callahan.grant_more_slip_days(elle, 7)
    >>> elle.max_slip_days
    7
    >>> Student.max_slip_days
    3
    >>>
"""


class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        self.buttons = {}
        for x in args:
            self.buttons[x.pos] = x

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if info in self.buttons.keys():
            b = self.buttons[info]
            b.times_pressed += 1
            return b.key
        return ''

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        s = ''
        for pos in typing_input:
            #s = s + self.buttons[pos].key
            s = s + self.press(pos)#不调用方法press就不会调用实例变量times_pressed
        return s

class Pet:

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        #super().talk()
        print(self.name + " says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        "*** YOUR CODE HERE ***"
        # if self.is_alive == False:
        #     print("This cat has no more lives to lose.")
        # elif self.lives == 0:
        #     self.is_alive = False
        # else:
        #     self.lives -= 1

        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print("This cat has no more lives to lose.")


class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner, lives)

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        super().talk()
        print(self.name + " says meow!")





import random as random

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.lives = lives

    # Insert other previously defined methods here

    @classmethod
    def adopt_random_cat(cls, owner):
        """
        Returns a new instance of a Cat with the given owner,
        a randomly chosen name and a random number of lives.
        >>> randcat = Cat.adopt_random_cat("Ifeoma")
        >>> isinstance(randcat, Cat)
        True
        >>> randcat.owner
        'Ifeoma'
        """
        cat_name = random.choice(['Tom', 'Jack', 'Thomas'])
        cat_lives = random.randint(1, 9)
        #为什么用的不是cls.cat_name和cls.cat_lives
        return cls(cat_name, owner, cat_lives)

class A:
    """
    >>> A('one')
    one
    >>> print(A('one'))
    oneone
    >>> repr(A('two'))
    'two'
    >>> str(A('two')) 
    'twotwo'
    """
    def __init__(self, x):
        self.x = x

    def __repr__(self):
         return self.x

    def __str__(self):
         return self.x * 2

class B:
    """
    >>> b=B()
    boo!
    >>> b.add_a(A('a'))
    >>> b.add_a(A('b'))
    >>> b
    2
    aabb
    """
    def __init__(self):
         print('boo!')
         self.a = []

    def add_a(self, a):
         self.a.append(a)

    def __repr__(self):
         print(len(self.a))
         ret = ''
         for a in self.a:
             ret += str(a)
         return ret