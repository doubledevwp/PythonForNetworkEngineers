
**Note:** There is a table of contents for each video at the bottom of this email including timestamps to where various content is located. This should be helpful in navigating the videos.

---

# Video References From Kirk Byers

- Numbers<br>
Video https://vimeo.com/244128549<br>
Length is 9 minutes<br>

- Files<br>
Video https://vimeo.com/244127459<br>
Length is 10 minutes<br>

- Lists<br>
Video https://vimeo.com/244257596<br>
Length is 6 minutes<br>

- List Slices<br>
Video https://vimeo.com/244259492<br>
Length is 4 minutes  <br>

- Lists are Mutable<br>
Video https://vimeo.com/244287000<br>
Length is 5 minutes<br>

- Tuples<br>
Video https://vimeo.com/244153105<br>
Length is 3 minutes<br>

- Using .join()<br>
​Video https://vimeo.com/245464488<br>
Length is 3 minutes<br>

- sys.argv<br>
Video https://vimeo.com/245464766<br>
Length is 2 minutes<br>

- Linters<br>
Video https://vimeo.com/245102246<br>
Length is 6 minutes<br>

---

# Additional Content:

- [Automate the Boring Stuff with Python (Chapter 4 on Strings)](https://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiNDI1NDQ5NyIsImRlbGl2ZXJ5X2lkIjoiMzh0dzhnZXhxdTF2dW5sdnp2bWkiLCJ1cmwiOiJodHRwczovL2F1dG9tYXRldGhlYm9yaW5nc3R1ZmYuY29tL2NoYXB0ZXI0Lz9fX3M9bGt4YTM4aGwwdnBzd3F0MzhpZDYifQ)
<br>Up through the section named "Removing Values from Lists with del Statements"

- [Dive Into Python, Lists](https://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiNDI1NDQ5NyIsImRlbGl2ZXJ5X2lkIjoiMzh0dzhnZXhxdTF2dW5sdnp2bWkiLCJ1cmwiOiJodHRwczovL3d3dy5kaXZlaW50by5vcmcvcHl0aG9uMy9uYXRpdmUtZGF0YXR5cGVzLmh0bWw_X19zPWxreGEzOGhsMHZwc3dxdDM4aWQ2I2xpc3RzIn0)

---

# GitHub.com: Kirk Byers
Reference code for these exercises is posted on GitHub at:

https://github.com/ktbyers/pynet/tree/master/learning_python/lesson2

---

# Video Outline

- Numbers (VIDEO1)
   - Creating an integer type  [0:10]
   - Arithmetic Operators [0:23]
      - Modulo Operator [0:59]
      - Raise to the power [1:19]
      - Division behavior and Python2 [1:31]
         - from __future__ import division [2:44]
      - Whitespace in Python [3:32]
   - Type float [4:00]
   - Type casting an integer to a float [4:50]
   - Strange math behavior of .1 + .2 [5:53]
   - Increment by one [8:00]
 
- Files (VIDEO2)
   - Open a file for reading [0:26]
      - f.read() [0:58]
      - f.seek(0) [1:43]
      - f.close() [2:22]
   - f.readline() [3:23]
   - f.readlines() [3:56]
   - Context manager [5:04]
      - Automatic close [5:56]
   - Writing a file [6:30]
      - f.flush() [7:30]
      - Destructive operation [7:43]
   - Append a file [8:12]
 
- Lists (VIDEO3)
   - Data that is inherently sequential [0:06]
   - Examples [0:19]
   - Creating a list [0:56]
      - Creating a list with existing values [1:16]
      - Lists can store different types of data [1:39]
      - Accessing element 0, 1, 2, 3 [1:56]
      - Changing the value of an element [2:23]
   - List methods [2:53]
      - append() [2:57]
      - list concatenation [3:13]
      - list.extend() [3:48]
      - removing elements [4:14]
         - my_list.pop() [4:22]
         - my_list.pop(0) [4:37]
         - del my_list[0] [4:58]
 
- List slices (VIDEO4)
   - Read from show_version.txt [0:12]
   - Creating new lists from an existing list [0:47]
   - First index is included [1:07]
   - Last index is excluded [1:14]
   - First number is excluded (go to beginning) [1:39]
   - Last number is excluded (go to end) [2:02]
   - Can use negative indices [3:21]
 
- Lists are Mutable (VIDEO5)
   - What does mutable mean [0:14]
   - Mutable data types (lists, dictionaries) [2:13]
   - Immutable data types (strings, numbers) [3:03]
   - Be careful with copying lists [4:48]
- Tuples (VIDEO6)
   - Use parenthesis and not brackets [0:19]
   - Why use tuples? [0:34]
   - Behaves like a list, but can't modify it [0:48]
   - Tuples use less memory [2:07]
   - Type cast as a list [2:21]
- Using .join() (VIDEO7)
   - Review of using .split()   [0:11]
      - Split returns a list   [0:34]
   - .join() reunites the parts   [0:59]
      - String separator, pass in a list   [1:06]
      - Separator between each element   [1:30] 
      - .join() is a string method   [1:35]
   - Example using an IP address   [2:26]
- sys.argv (VIDEO8)
   - Behavior of sys.argv   [0:25]
      - Returns a list, element1 is the program name   [0:31]
      - Additional args are remaining elements   [0:54]
- Linters (VIDEO9)
   - Advantages of using linters [0:04]
      - Improve readability [0:23]
      - Flag obvious errors and save debugging time [0:40]
      - Flag potential problems [0:50]
   - Two most common linters: pylint and pycodestyle [1:01]
      - Installing pylint and pycodestyle linters [1:20]
      - Example using pylint and pycodestyle [1:35]
      - Example using pylint and pycodestyle [2:08]
   - Using pylama and a setup.cfg file [3:35]
   - You decide what characteristics matters [4:07]
   - Zero errors [5:03]
   - Integrate with CI [5:16]
