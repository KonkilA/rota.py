""" program to generate a rota between a date range
given on the command line """

import datetime
import sys
from itertools import cycle
import csv
from random import randrange
from random import shuffle

names=open('names.txt').read().splitlines()
tasks=open('tasks.txt').read().splitlines()

#basic validation of command line args (there should be four)
# - "filename startdate enddate outputformat"
if len(sys.argv) < 4:
  print("Input error. Arguments must be start datestart date(dd/mm/yy) end date(dd/mm/yy) output format(csv,tex)")
  #quit since it will throw a index out of bounds error
  sys.exit(0)

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

#get a randomised, fairly distibuted list of names equal to |tasks|*|weeks|
nameCycle=cycle(names)
currDate=startDate
namesDistribution=[nameCycle.next()]
namesDone=1
while ((endDate-currDate)>datetime.timedelta(hours=0)):
  for task in tasks:
    #add the next name to the distribution
    namesDistribution+=[nameCycle.next()]
    namesDone += 1
    #if all names have been mentioned, shuffle their order before retracing
    if namesDone == len(names):
      shuffle(names)
      nameCycle=cycle(names)
      namesDone=0
  currDate += datetime.timedelta(days=7)

namesDistributionCycle=cycle(namesDistribution)
#for each week, assign one name to one task, storing order by row in rotaTable[]
currDate=startDate
while ((endDate-currDate)>datetime.timedelta(hours=0)):
  row=[currDate.strftime("%d/%m/%y")]
  #loop through tasks, and assign name to task from distribution
  for task in tasks:
    row.append(namesDistributionCycle.next())
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

#generate output
if(sys.argv[3].lower()=="csv"):
  print("Generated csv from txt files")
  makeCSV(rotaTable)
elif(sys.argv[3].lower()=="tex"):
  print("Generated csv and tex from txt files")
  makeTex(rotaTable)
else:
  print("Defaulted to generating csv from txt files")
  makeCSV(rotaTable)