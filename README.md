rota.py
=======
Python based rota generator.

This is in development by a computer science first year, so don't expect perfection.

Usage
-----
Create a tasks.txt with each task on a new line, and a names.txt with each name on a new line.

From the command line, run with the start and end dates as command line arguments in dd/mm/yy format:

`python rota.py 15/11/14 12/12/14`

The program will generate a csv file. The first row of the file is the rota table header, with the given task names. The remaining rows start with the week's start date(a Monday) followed by names allocated to tasks:

<pre>
Week Beginning,Kitchen,Bathroom,Halls,Rubbish
10/11/14,Steve,Matt,Suzie,Steve
...
</pre>

Installation & Configuration
----------------------------
Ensure you are running python, and then download the script.