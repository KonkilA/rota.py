""" program to generate a rota between a date range
given on the command line """

import datetime
import sys
from itertools import cycle
import csv
from random import randrange

names=open('names.txt').read().splitlines()
tasks=open('tasks.txt').read().splitlines()

nameCycle=cycle(names)

#randomise the start position in the name cycle
for i in range(randrange(len(names))):
  nameCycle.next()

#date boundries in dd/mm/y
startDate=datetime.datetime.strptime(sys.argv[1], "%d/%m/%y")
endDate=datetime.datetime.strptime(sys.argv[2], "%d/%m/%y")

def toMonday(date):
  if date.weekday()!=0:
    #inform user of date change
    print("Converting " + date.strftime("%d/%m/%y")
          + " to previous monday:")
    date=(date-datetime.timedelta(days=date.weekday()))
    print("New date: " + date.strftime("%d/%m/%y"))
  return date

#convert start day to the week's monday
startDate=toMonday(startDate)

#create an array for header, 0th element "week beginning",
#then subsequent elements task names
header=["Week Beginning"]
for task in tasks:
  header.append(task)
print(header)

rotaTable=[header]

#set current date and loop it from week of start to week of end
currDate=startDate
while ((endDate-currDate)>datetime.timedelta(hours=0)):
  row=[currDate.strftime("%d/%m/%y")]
  for task in tasks:
    row.append(nameCycle.next())
  print(row)
  rotaTable.append(row)
  currDate += datetime.timedelta(days=7)

#write the contents of a passed 2d rota array to rota.csv
def makeCSV(table):
  wr = csv.writer(open("rota.csv","w"), delimiter=',',quoting=csv.QUOTE_MINIMAL)
  for row in table:
    wr.writerow(row)

def makeTex(table):
  makeCSV(table)
  texFile=open("rota.tex","w")
  texFile.write("\documentclass{article} \n"
                +"\usepackage{csvsimple} \n"
                +"\\"+"begin{document} \n"
                +"\csvautotabular{rota.csv} \n"
                +"\end{document})")

if(sys.argv[3].lower()=="csv"):
  print("Generating csv from txt files")
  makeCSV(rotaTable)
elif(sys.argv[3].lower()=="tex"):
  print("Generating csv and tex from txt files")
  makeTex(rotaTable)
else:
  print("Defualting to generating csv from txt files")
  makeCSV(rotaTable)