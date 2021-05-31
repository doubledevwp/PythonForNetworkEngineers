# Week 5 Email

In this email of Learning Python we are going to cover the following:
- Functions (Part1) <br>
Video link https://vimeo.com/247570174 <br>
Length is 8 minute <br>
     
- Functions (Part2) <br>
Video link https://vimeo.com/247581011 <br>
Length is 11 minutes <br>
     
- Misc Topics (Part1) <br>
Video link https://vimeo.com/247582360 <br>
Length is 10 minutes <br>
     
- Misc Topics (Part2) <br>
Video link https://vimeo.com/247655574 <br>
Length is 8 minutes <br>
     
- Python Debugger (pdb) <br>
Video link https://vimeo.com/247724017 <br>
Length is 10 minutes <br>

## Additional Content:

[A Byte of Python, Functions](https://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiNDI1NDQ5NyIsImRlbGl2ZXJ5X2lkIjoiczVtMnN2aGc2MmliZGIwMDRvaDMiLCJ1cmwiOiJodHRwczovL3B5dGhvbi5zd2Fyb29wY2guY29tL2Z1bmN0aW9ucy5odG1sP19fcz1sa3hhMzhobDB2cHN3cXQzOGlkNiJ9)

[How to use the Python Debugger](https://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiNDI1NDQ5NyIsImRlbGl2ZXJ5X2lkIjoiczVtMnN2aGc2MmliZGIwMDRvaDMiLCJ1cmwiOiJodHRwczovL3d3dy5kaWdpdGFsb2NlYW4uY29tL2NvbW11bml0eS90dXRvcmlhbHMvaG93LXRvLXVzZS10aGUtcHl0aG9uLWRlYnVnZ2VyP19fcz1sa3hhMzhobDB2cHN3cXQzOGlkNiJ9)

## Exercises

Reference code for these exercises is posted on GitHub at:
    https://github.com/ktbyers/pynet/tree/master/learning_python/lesson5


1. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. The function should print out each of these three variables and clearly indicate which variable it is printing out.

   Call this ssh_conn function using entirely positional arguments.

   Call this ssh_conn function using entirely named arguments.

   Call this ssh_conn function using a mix of positional and named arguments.

2. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default value of 'cisco_ios'. Print all four of the function variables out as part of the function's execution.

   Call the 'ssh_conn2' function both with and without specifying the device_type

   Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique.

3.  Create a function that randomly generates an IP address for a network. The default base network should be '10.10.10.'. For simplicity the network will always be a /24.

    You should be able to pass a different base network into your function as an argument.

    Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

    You can use the following to randomly generate the last octet:

    import random <br>
    random.randint(1, 254)

    Call your function using no arguments. <br>
    Call your function using a positional argument. <br>
    Call your function using a named argument. <br>

    For each function call print the returned IP address to the screen.

4. Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:

   01:23:45:67:89:AB

   This function should handle the lower-case to upper-case conversion.

   It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.

   The function should have one parameter, the mac_address. It should return the normalized MAC address

   Single digit bytes should be zero-padded to two digits. In other words, this:

   a:b:c:d:e:f

   should be converted to:

   0A:0B:0C:0D:0E:0F

   Write several test cases for your function and verify it is working properly.

5. Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement outside of your function (i.e. where you have your function calls).

   Inside of pdb, experiment with:

   Listing your code. <br>
   Using 'next' and 'step' to walk through your code. Make sure you understand the difference between next and step. <br>
   Experiment with 'up' and 'down' to move up and down the code stack. <br>
   Use p <variable> to inspect a variable. <br>
   Set a breakpoint and run your code to the breakpoint. <br>
   Use '!command' to change a variable (for example !new_mac = []) <br>

## CLASS OUTLINE


1. Functions (Part1) (VIDEO1)
   - How to define   [0:04]
   - How to call   [0:35]
   - Return values   [1:41]
   - Adding positional arguments   [3:21]
   - Adding named arguments   [4:54]
   - Default values   [7:13]

2. Functions (Part2) (VIDEO2)
   - Calling with *args   [1:57]
   - Calling with **kwargs   [3:45]
   - Passing mutables as function arguments   [4:49]
   - Variables are local to the function   [7:59]

3. Misc Topics (Part1) (VIDEO3)
   - Classes   [0:23]
      - Why you might want to use classes   [0:43]
      - Syntax for creating a class   [2:16]
   - Modules   [5:15]
      - What is a module   [5:38]
      - Importing a module you have created   [5:54]
      - Calling your imported function   [6:05]
      - How Python finds something using sys.path   [6:40]
      - Two ways to perform imports   [7:10]

4. Misc Topics (Part2) (VIDEO4)
   - Packages   [0:41]
   - List comprehensions   [1:55]
   - Lambda functions   [4:47]

5. Python’s Debugger (PDB) (VIDEO5)
   - The (Pdb) shell   [0:08]
   - Listing lines using 'list'   [0:52]
   - Using 'step (s)' to step through a program   [1:27]
   - 'args' to look at arguments of a function   [1:56]
   - 'p' to print variables   [2:01]
   - 'pp' to pretty print   [2:10]
   - 'up' to move up the stack   [2:27]
   - 'down' to move down the stack   [2:56]
   - execute until the return statement   [3:15]
   - Executing using 'python -m pdb'   [4:10]
   - Using 'next (n)'   [5:11]
   - Difference between step and next   [5:56]
   - Setting a breakpoint   [6:13]
   - 'continue' to execute until the breakpoint   [6:24]
   - Use '!<command>' to execute python code   [6:48]
   - Debugging principles   [7:54]
      - Get information out of your program   [8:08]
      - Quick feedback loop   [8:15]
