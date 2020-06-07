import datetime

#Defining a user class for easy object oriented design and coordination with the graph
class User:
    def _init_(self,named):
        self.name=named
        self.allAvailable=False
        self.allUnavailable=True
    
    def setAllAvailable():
        self.allAvailable=True

    def setAllUnavailable():
        self.allUnavailable=True
#Defining a graph type class for my dates
#basically the user will enter people and the dates that they cannot make it
#then, we will create a graph with all the dates of absences
#if there are as many absences as dates in the range, then we will choose the dates with the least people absent
#otherwise we will choose the dates with nobody absent
class DateGraph:
    def _init_():
        self.dates={}
    
    #adding a specific node based on user-timedate key pair
    def addUser(user,timedate):
        if (timedate in self.dates):
            self.dates[timedate].append(user)
        else :
            self.dates[timedate]=[user]
    #counts the degree of a node
    def countDegree(timedate):
        #count the degree here

    def getBestDates():
        #goes through all the dates and gets a list of the best dates (based on least people missing)

#some functions to help with date stuff

#function to check if a date is in the range specified by the user
def isValidDate(enteredDate, begDate,endDate):
    if (enteredDate<=endDate and enteredDate>=begDate):
        return True
    else:
        return False


#function to take list of dates and get list of datetimes
def getListTimes(dateString):
    seperatedDates=dateString.split(",")
    for 



#when user is entering data about other users, they can optionally say ALL ABSENT Except ..., ALL ABSENT, NOT ABSENT, NOT ABSENT except..., in addition to just listing dates
#if a user is all absent, then they can just be excluded from the graph basically.
#likewise, if a user is not absent, they can also be excluded from the graph
def main():
    while True
    dateRange = input("Please enter a date range in the format mm/dd/yyyy:mm/dd/yyyy\n")
    #removing whitespace from the entire date, if any
    dateRange.replace(" ","")
    #splitting up ending date string and beginning date string
    dateRange=dateRange.split(":")
    begDate=dateRange[0]
    endDate=dateRange[1]
    #turning our date strings into actual date objects for future usefulness
    begDate=datetime.date(begDate[6,9],begDate[0,1],begDate[3,4])
    #asking user to enter people attending and their availability
    usersDatesDictionary={}
    #maps users names to another dictionary
    usersNamesDictionary={}
    #count for users
    userCount=0
    print("Please enter the name of a user, then enter their availability in the form ALL ABSENT, NOT ABSENT, ALL ABSENT EXCEPT mm/dd/yyyy,mm/dd/yyyy...,NOT ABSENT EXCEPT mm/dd/yyyy,mm/dd/yyyy..., or just enter dates seperated by a comma. Enter as many users as you wish, when you are finished enter a -.\n")
    while True
        user=input("please enter the person's name. Enter - if you want to stop.")
        user.strip()
        if (user=="-"):
            break
        else :
            toAdd = User(user)
        while True
            dates=input("Please enter either ALL ABSENT, ALL PRESENT, a date range of the form mm/dd/yyyy:mm/dd/yyyy, or an individual date of the form mm/dd/yyyy and hit enter. When you wish to stop please enter - .")
            dates.replace(" ","")
            dates.lower()
            if (dates==allabsent):
                #we have to check off all absent
                toAdd.setAllUnavailable()
                break
            elif (dates==allpresent):
                #we have to check off all present
                toAdd.setAllAvailable()
                break
            elif (dates[10]==":"):
                #we have a date range
                #we should check if start date is valid and end date is valid
                dates=dates.split(":")
                start = dates[0]
                end = dates[1]
                start = datetime.date(start[6,9],start[0,1],start[3,4])
                end=datetime.date(end[6,9],end[0,1],end[3,4])
                if (isValidDate(start,begDate,endDate) and isValidDate(end,begDate,endDate)):
                    #then i need to add all the dates in this range to the dictionary
            else :
                #then we have an individual date
                #we should check if this date is valid and then if valid, we add it, else not
                dates=datetime.date(dates[6,9],dates[0,1],dates[3,4])
                if (isValidDate(dates,begDate,endDate)):
                    #then we add this date to the dictionary
                    usersDatesDictionary[toAdd].append(dates)
        #now we set up the corresponding "nodes" in the graph
