""" program to generate a CSV rota between a date range
given on the command line """

import datetime
import sys
from itertools import cycle
import csv
from random import randrange

#task and name arrays
names=["Connor","Sivert","Tom","Alex","Vlad"]
nameCycle=cycle(names)
tasks=["Kitchen","Bathroom","Bins","Hoover"]

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
  wr = csv.writer(open("rota.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
  for row in table:
    wr.writerow(row)

makeCSV(rotaTable)