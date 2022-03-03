'''
Author: your name
Date: 2022-02-07 19:37:28
LastEditTime: 2022-02-10 19:57:51
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \sp21\17.py
'''
class Food:

    def __init__(self, name, type, calories):
        self.name = name
        self.type = type
        self.calories = calories

class Elephant:
    species_name = "African Savanna Elephant"
    scientific_name = "Loxodonta africana"
    calories_needed = 8000

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten  = 0
        self.happiness = 0

    def play(self, num_hours):
        self.happiness += (num_hours * 4)
        print("WHEEE PLAY TIME!")

    def eat(self, food):
        self.calories_eaten += food.calories
        print(f"Om nom nom yummy {food.name}")
        if self.calories_eaten > self.calories_needed:
            self.happiness -= 1
            print("Ugh so full")

    def interact_with(self, animal2):
        self.happiness += 1
        print(f"Yay happy fun time with {animal2.name}")


ranked_chocolates = ("Dark", "Milk", "White")
for chocolate in ranked_chocolates:
    print(chocolate)
print('================')
ranked_chocolates = ("Dark", "Milk", "White")
chocorator = iter(ranked_chocolates)
try:
    while True:
        print(next(chocorator))
except StopIteration:
    pass

def evens():
    num = 0
    while num < 2:
        yield num
        num += 2

gen = evens()

# next(gen)
# next(gen)

# def find_matches(filename, match):
#     matched = []
#     for line in open(filename):
#         if line.find(match) > -1:
#             matched.append(line)
#     return matched

# matched_lines = find_matches('frankenstein.txt', "!")
# matched_lines[0]
# matched_lines[1]

def a_then_b(a, b):
    for item in a:
        yield item
    for item in b:
        yield item

list(a_then_b(["Apples", "Aardvarks"], ["Bananas", "BEARS"]))



def a_then_b_alt(a, b):
    yield from a
    yield from b

list(a_then_b_alt(["Apples", "Aardvarks"], ["Bananas", "BEARS"]))


def factorial(n, accum):
    if n == 0:
        yield accum
    else:
        yield from factorial(n - 1, n * accum)

for num in factorial(3, 1):
    print(num)


def leaves(t):
    yield label(t)
    for c in branches(t):
        yield from leaves(c)

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

t = tree(20, [tree(12,
               [tree(9,
                  [tree(7), tree(2)]),
                tree(3)]),
              tree(8,
               [tree(4), tree(4)])])

leave_gen = leaves(t)
next(leave_gen)


