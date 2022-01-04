Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:
<pre> $ python exercise2.py 
   Please enter an IP address: 80.98.100.240

       Octet1         Octet2         Octet3         Octet4     
   ------------------------------------------------------------
         80             98             100            240      
      0b1010000      0b1100010      0b1100100     0b11110000   
        0x50           0x62           0x64           0xf0      
   ------------------------------------------------------------
</pre>

Four columns, fifteen characters wide, a header column, data centered in the column.
