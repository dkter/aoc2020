# Advent of Code 2020

This repository contains my solutions to [Advent of Code 2020](https://adventofcode.com/2020/), largely written in Python.

### Notable solutions

* [Day 13](https://adventofcode.com/2020/day/13) (part 2), in which I didn't know the math so I used Selenium to scrape Wolfram Alpha for the answer: [day13_pt2.py](https://github.com/dkter/aoc2020/blob/main/day13_pt2.py)
* [Day 14](https://adventofcode.com/2020/day/14), where I literally import the input file as a Python module:
```py
import day14_input
print(day14_input.mem)
```
[day14_stupid_edition.py](https://github.com/dkter/aoc2020/blob/main/day14_stupid_edition.py)
* [Day 18](https://adventofcode.com/2020/day/18) (part 1), which I just used Smalltalk for because Smalltalk has the exact operator precedence the problem was looking for: [day18_pt1.st](https://github.com/dkter/aoc2020/blob/main/day18_pt1.st)
* [Day 18](https://adventofcode.com/2020/day/18) (part 2), where I substitute operators in a string, compile it into a Python AST, and then replace the operators back in the AST and evaluate it: [day18_pt2.py](https://github.com/dkter/aoc/blob/main/day18_pt2.py)
