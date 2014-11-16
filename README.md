rota.py
=======
Python based rota generator.

This is in development by a computer science first year, so don't expect perfection.

Installation & Configuration
----------------------------
Ensure you have installed python, and then download the script.

In the smae directory as rota.py, create a tasks.txt with each task on a new line, and a names.txt with each name on a new line:

names.txt
<pre>
Steve
Matt
Suzie
</pre>

tasks.txt
<pre>
Kitchen
Bathroom
Halls
Rubbish
</pre>

Usage
-----
Create the two input files. From the command line, run with command line arguments: start date(dd/mm/yy), end date(dd/mm/yy), output format(csv,tex)

`python rota.py 15/11/14 12/12/14 csv`

The program will generate a rota.csv file in the current directory. The first row of the file is the rota table header, with the given task names. The remaining rows start with the week's start date(a Monday) followed by names allocated to tasks:

<pre>
Week Beginning,Kitchen,Bathroom,Halls,Rubbish
10/11/14,Steve,Matt,Suzie,Steve
17/11/14,Matt,Suzie,Steve,Matt
...
</pre>

If tex is chosen, along with the csv the following rota.tex is written:

<pre>
\documentclass{article} 
\usepackage{csvsimple} 
\begin{document} 
\csvautotabular{rota.csv} 
\end{document})
</pre>

This can then be converted to pdf using a tool like pdflatex(not included).