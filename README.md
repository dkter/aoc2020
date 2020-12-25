# Advent of Code 2020

This repository contains my solutions to [Advent of Code 2020](https://adventofcode.com/2020/), largely written in Python.

### My ranks/times

          --------Part 1--------   --------Part 2--------
    Day       Time   Rank  Score       Time   Rank  Score
     25   00:32:59   2390      0   00:33:06   1979      0
     24   00:15:55    714      0   00:37:13    892      0
     23   00:48:50   2030      0   12:54:44   6788      0
     22   00:10:45   1245      0   01:56:16   3086      0
     21   00:23:08    678      0   00:34:31    840      0
     20   12:25:24   8878      0   21:47:17   6432      0
     19   01:01:08   1830      0   01:49:12   1507      0
     18   00:15:39    410      0   00:50:05   1469      0
     17   13:39:38  14425      0   13:50:07  13582      0
     16   00:17:23   1575      0   00:31:50    425      0
     15   00:07:07    192      0   00:20:08    865      0
     14   00:17:20   1128      0   00:49:07   1712      0
     13   00:10:18   1840      0   01:51:33   2998      0
     12   00:13:46   1566      0   01:14:09   4691      0
     11   00:17:20    786      0   00:31:44    980      0
     10   00:12:47   3460      0   13:14:09  22595      0
      9   00:09:24   1912      0   00:16:00   1483      0
      8   00:10:12   2345      0   00:27:37   2767      0
      7   00:22:08   1400      0   00:42:06   1932      0
      6   00:07:53   2660      0   00:11:49   1614      0
      5   00:10:22   1298      0   00:12:38    883      0
      4   00:17:13   3351      0   00:30:51   1353      0
      3   00:28:59   6241      0   00:37:26   5696      0
      2   12:29:20  50382      0   12:32:02  47684      0
      1       >24h  85503      0       >24h  79906      0

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
