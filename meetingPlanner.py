import datetime

#Defining a user class for easy object oriented design and coordination with the graph
class User:
    def _init_(self,named):
        self.name=named
        self.allAvailable=False
        self.allUnavailable=True
    
    def setAllAvailable(self):
        self.allAvailable=True

    def setAllUnavailable(self):
        self.allUnavailable=True
#Defining a graph type class for my dates
#basically the user will enter people and the dates that they cannot make it
#then, we will create a graph with all the dates of absences
#if there are as many absences as dates in the range, then we will choose the dates with the least people absent
#otherwise we will choose the dates with nobody absent
class DateGraph:
    def _init_(self):
        #this dictionary maps dates to users
        self.dates={}
        #this dictionary maps dates to their degree (we will increment this on every add)
        self.dateDegree={}
        #list of users that are all absent
        self.completelyAbsent=[]
        #list of users that are all present
        self.completelyPresent=[]
    
    #adding a specific node based on user-timedate key pair
    def addUserDate(self,user,timedate):
        if (timedate in self.dates):
            self.dates[timedate].append(user)
            self.dateDegree[timedate]++
        else :
            self.dates[timedate]=[user]
            self.dateDegree[timedate]=0

    #adding a user that is completely absent
    def addAbsentUser(self,user):
        self.completelyAbsent.append(user)

    #adding a user that is completely present
    def addPresentUser(self,user):
        self.completelyPresent.append(user)
    
    #getting all the users that are absent on a specific date
    def getAbsentUsers(self,timedate):
        absentees=[]
        for x in self.dates:
            absentees.append(x)
        for x in self.completelyAbsent:
            absentees.append(x)
        return absentees

    #counts the degree of a node
    def countDegree(self,timedate):
        #count the degree here
        #we just count the number of users associated to this date
        count=0
        for person in self.dates[timedate]:
            count++
        return count

    #method to get the best dates in the graph
    def getBestDates(self):
        #goes through all the dates and gets a list of the best dates (based on least people missing)
        #i do one pass to find the date with the least people absent (least degree)
        #then i do another pass to add other dates with the same degree and add them to the list
        bestDate=None
        bestDates=[]
        for x in self.dateDegree:
            if (bestDate==None):
                bestDate=x
            else :
                if (self.dateDegree[bestDate]>x):
                    #then x has the least people absent
                    bestDate=x
        
        #second pass to add all the dates with this least associativity
        for x in self.dateDegree:
            if (self.dateDegree[bestDate]==self.dateDegree[x]):
                bestDates.append(x)
        #returning the list of best dates, ready to be printed out to the user
        return bestDates

    #function to print out the list of best dates and the users attending
    def printBestDates(self,listDates):
            if (len(listDates)>1):
                print("Best Dates and Absentees:\n")
                print("------------------------------------------------------\n")
            else :
                print("Best Date and Absentees:\n")
                print("------------------------------------------------------\n")
            
            #now iterating through the dates given and printing out the date and the absentees
            for x in listDates:
                x.strftime("%b/%d/%Y\n")
                print("Absent:")
                for y in self.dates[x]:
                    print(" "+y)
                print("\n")
                print("------------------------------------------------------\n")
        
#some functions to help with date stuff

#gets all the dates in the given range (returns a list of datetimes)
def getDateRange(begDate,endDate):
    testDate=begDate
    dates=[]
    while(testDate <=endDate):
       dates.append(testDate)
       testDate=testDate+datetime.timedelta(day=1)
    return dates



#function to check if a date is in the range specified by the user
def isValidDate(enteredDate, begDate,endDate):
    if (enteredDate<=endDate and enteredDate>=begDate):
        return True
    else:
        return False


#function to turn a string in form of "mm/dd/yy" into a datetime
def getDateTime(enteredDate):
    date=datetime.date(enteredDate[6,9],enteredDate[0,1],enteredDate[3,4])
    return date


#when user is entering data about other users, they can optionally say ALL ABSENT Except ..., ALL ABSENT, NOT ABSENT, NOT ABSENT except..., in addition to just listing dates
#if a user is all absent, then they can just be excluded from the graph basically.
#likewise, if a user is not absent, they can also be excluded from the graph
def main():
    #creating a graph to use
    graph = DateGraph()
    dateRange = input("Please enter a date range for the event in the format mm/dd/yyyy:mm/dd/yyyy\n")
    #removing whitespace from the entire date, if any
    dateRange.replace(" ","")
    #splitting up ending date string and beginning date string
    dateRange=dateRange.split(":")
    begDate=dateRange[0]
    endDate=dateRange[1]
    #turning our date strings into actual date objects for future usefulness
    begDate=getDateTime(begDate)
    endDate=getDateTime(endDate)
    #list of all usernames entered in this operation
    users=[]
    print("Now you will be prompted to enter information for each user associated with this event: \n")
    while True:
        user=input("please enter the person's name. Enter - if you want to stop.")
        user.replace(" ","")
        if (user=="-"):
            break
        else :
            users.append(user)
        while True:
            dates=input("Please enter either ALL ABSENT, ALL PRESENT, a date range of the form mm/dd/yyyy:mm/dd/yyyy in which the individual WOULD BE ABSENT, or an individual date of the form mm/dd/yyyy in which the individual WOULD BE ABSENT and hit enter. When you wish to stop please enter - .")
            dates.replace(" ","")
            dates.lower()
            if (dates=="allabsent"):
                #we have to check off all absent
                graph.addAbsentUser(user)
                break
            elif (dates="-"):
                #then we stop
                break
            elif (dates=="allpresent"):
                #we have to check off all present
                #in other words, do nothing, because all present doesnt really matter
                break
            elif (dates[10]==":"):
                #we have a date range
                #we should check if start date is valid and end date is valid
                dates=dates.split(":")
                start = dates[0]
                end = dates[1]
                start = getDateTime(start)
                end=getDateTime(end)
                if (isValidDate(start,begDate,endDate) and isValidDate(end,begDate,endDate)):
                    #then i need to add all the dates in this range to the dictionary
                    datesList = getDateRange(begDate,endDate)
                    for x in datesList:
                        #I need to add the date user pair to the graph
                        graph.addUserDate(user,x)
            elif(dates[2]=="/" and dates[5]=="/"):
                #then we have an individual date
                #we should check if this date is valid and then if valid, we add it, else not
                dates=datetime.date(dates[6,9],dates[0,1],dates[3,4])
                if (isValidDate(dates,begDate,endDate)):
                    #then we add this date to the graph dictionary
                    graph.addUserDate(user,dates)
            else:
                #then we have some invalid input
                print("I am sorry, it seems there was an invalid input! Please try again: \n")
    #now we find the list of the best dates and print them
    bestDates = graph.getBestDates()
    #we first print the list of all the users
    print("Users associated with this event: \n")
    for x in users:
        print(x+"\n")
    #now i print the output of the best dates
    graph.printBestDates(bestDates)

