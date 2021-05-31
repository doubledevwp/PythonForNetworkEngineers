**Note:** There is a table of contents for each video at the bottom of this email including timestamps to where various content is located. 
This should be helpful in navigating the videos.

---

**Note2:** You should be fundamentally focused on Python3 at this point in time and should be actively migrating any legacy Python2 code to Python3. 
Python2 support ended (from the Python core developers) on January 1, 2020.

---

# Video References From Kirk Byers
 
- Introduction<br>
Video https://vimeo.com/243034300<br>
Length is 7 minutes<br>

- Why Learn Programing?<br>
Video https://vimeo.com/243905715<br>
Length is 1 minute<br>

- Why Python?<br>
Video https://vimeo.com/243909371<br>
Length is 3 minutes<br>

- Python2 versus Python3<br>
Video https://vimeo.com/243912631<br>
Length is 2 minutes<br>

- Characteristics of Python<br>
Video https://vimeo.com/243918300<br>
Length is 5 minutes<br>

- The Python Interpreter Shell<br>
Video https://vimeo.com/242411259<br>
Length is 9 minutes<br>

- IPython<br>
Video https://vimeo.com/242460561<br>
Length is 4 minutes<br>

- Printing to stdout and Reading from stdin<br>
Video https://vimeo.com/243028886<br>
Length is 6 minutes<br>

- Dir, Help, and Variables​<br>
Video https://vimeo.com/243480156<br>
Length is 10 minutes<br>

- Python Strings (Part 1)<br>
Video https://vimeo.com/243481392<br>
Length is 6 minutes<br>

- Python Strings (Part 2)<br>
Video https://vimeo.com/243482081<br>
Length is 8 minutes<br>

- Python Strings (Part 3)<br>
Video https://vimeo.com/243482871<br>
Length is 10 minutes<br>

- Python String Formatting (Part 1)<br>
Video https://vimeo.com/243936489<br>
Length is 12 minutes<br>

- Python String Formatting (Part 2)<br>
Video https://vimeo.com/243956669<br>
Length is 4 minutes <br>

---

# Additional Content:

- [Google Python Course on Strings](https://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiNDI1NDQ5NyIsImRlbGl2ZXJ5X2lkIjoibHY1cXZoNjZoYjdxeWJoMjR4dGYiLCJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMuZ29vZ2xlLmNvbS9lZHUvcHl0aG9uL3N0cmluZ3M_X19zPWxreGEzOGhsMHZwc3dxdDM4aWQ2In0)

- [Automate the Boring Stuff with Python (Chapter 6 on Strings)](https://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiNDI1NDQ5NyIsImRlbGl2ZXJ5X2lkIjoibHY1cXZoNjZoYjdxeWJoMjR4dGYiLCJ1cmwiOiJodHRwczovL2F1dG9tYXRldGhlYm9yaW5nc3R1ZmYuY29tL2NoYXB0ZXI2Lz9fX3M9bGt4YTM4aGwwdnBzd3F0MzhpZDYifQ)

*Read up through the section on .join() and .split() string methods.

---

# Python Standards

- Python naming conventions:
  - a. For variable names, function names, object names, and module names use lower case separated by underscore, for example:

    - my_router
    - find_set_of_devices
    - convert_id_string_to_list

  - For class names, capitalize the first letter of each word.  Do not use any underscores.  For example:

    - ManyToManyField
    - ClientHistory
    - UserProfile

  - For constants, use all upper case; use underscores for word separation.

    - PI = 3.14
    - EMAIL_MODE
    - EMAIL_FROM_ADDRESS

---

# GitHub.com: Kirk Byers
Reference code for these exercises is posted on GitHub at:

https://github.com/ktbyers/pynet/tree/master/learning_python/lesson1

---

# Video Outline

- Introduction (VIDEO1)
   - Purpose of the course  [0:11]
   - Who is this video series for?  [0:33]
   - About me  [2:51]
   - Course logistics  [3:29]
   - Apply what you learn  [4:23]
   - Context for the exercises  [4:49]

- Why Learn Programming? (VIDEO2)
   - Programming as a power skill  [0:10]
   - Still need to retain core engineering skills  [0:20]
   - Automation is major trend in our industry  [0:30]
   - Range of potential programming skills  [0:54]

- Why Python? (VIDEO3)
   - Large, active community  [0:20]
      - Libraries                                               
      - Learning resources                                      
      - People you can ask questions to                         
   - High-level language  [1:29]
   - Widely available on systems  [1:53]
   - Readability  [2:05]
   - Supports beginners through advanced programmers  [2:33]

- Python2 versus Python3? (VIDEO4)
   - What should network engineers do (as of today)?  [1:20]

- Characteristics of Python (VIDEO5)
   - Blocks of code are indicated by indentation  [0:13]
   - Python conventions  [2:02]
      - Follow the Python conventions (PEP8)   [2:12]                   
   - What is Python like as a language?  [3:20]
   - High-level language  [3:58]
      - Dynamically typed variables  [4:12]

- The Python Interpreter Shell VIDEO6)
   - Launch the interpreter shell  [0:05]
   - Running python 3.6.2  [0:33]
   - Creating a variable  [1:00]
      - Variable naming conventions  [1:17]
   - Using type  [1:43]
   - Characters allowed in variable names  [2:08]
      - Upper case / lower case / numbers  [2:23]
      - Can’t start with a number  [2:36]
      - Can start with an underscore  [2:47]
   - Automatic evaluation of expressions  [3:42]
   - First Python program  [4:15]
   - Printing to standard output  [5:21]
   - Making the program executable at the system level  [6:22]
   - Editing and Editors (to create Python programs)  [8:30]
   - IDEs  [8:53]

- IPython (VIDEO7)
   - Launching IPython  [0:13]
      - Better formatting  [0:47]
      - History buffer / improved history  [1:13]
      - Command completion  [1:40]
   - Installing IPython  [2:30]
      - More on variable names  [3:00]
      - Comments  [3:28]

- Printing to stdout / Reading from stdin (VIDEO8)
   - print() in Python3  [0:14]
      - Differences in Python2  [1:00]
      - Writing PY2 and PY3 compatible code  [1:41]
   - Python3 reading from stdin (input)  [2:43]
      - Differences in Python2  [3:31]
      - Writing PY2 and PY3 compatible code  [4:18]
  
- Dir, Help, and Variables (VIDEO9)
   - Using dir()  [0:24]
   - Calling methods versus referring to methods  [0:55]
      - Examples calling various string methods  [2:16]
      - Chaining methods  [2:39]
   - Using help()  [3:34]
   - Assignment operator  [5:44]
   - Variables as references to objects  [6:10]
      - Using id()  [6:16]
      - Two names that refer to the same thing  [7:17]
      - Reassigning a name to a different object  [8:40]

- Strings (Part1) (VIDEO10)
    - Fundamental Difference between Python2 and Python3  [0:30]
    - String in Python2 is an ASCII string  [1:10]
    - String in Python3 is a Unicode string  [1:59]
    - How to write Unicode strings in Python2  [2:08]
    - How to write byte strings in Python3  [3:23]
    - Technique for making all string literals unicode  [3:46]

- Strings (Part2) (VIDEO11)
    - Comparison Operators  [0:30]
    - Substring in broader string  [2:16]
    - String indexes  [3:51]
    - len() function  [4:50]
    - String concatenation  [5:14]
    - Binary and hex representations of strings  [6:43]

- Strings (Part3) (VIDEO12)
    - Raw Strings  [1:04]
    - Assigning strings (single, double, triple quotes) [1:44]
    - repr() of a string  [3:32]
    - String methods  [4:21]
       - strip()  [4:34]
       - split()  [6:04]
       - splitlines()  [9:15]

- String Formatting (Part1) (VIDEO13)
    - Replicating a string  [1:12]
    - Format Method  [1:35]
       - Calling with positional arguments  [2:00]
       - Specifying field width  [2:59]
       - Right aligned, centered  [3:21]
       - Using named arguments   [6:20]
       - Using *args to pass in a list  [10:50]

- String Formatting (Part2) (VIDEO14)
    - Using the format operator (%)  [0:25]
    - F-strings  [1:41]
