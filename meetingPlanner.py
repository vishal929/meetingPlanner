import datetime

#Defining a user class for easy object oriented design and coordination with the graph
class User:
    def _init_(named):
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
    def _init_(self,beginningDate,endingDate):
        self.begDate=beginningDate
        self.endDate=endingDate


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
    begDate=datetime.datetime(begDate[6,9],begDate[0,1],begDate[3,4])
    #asking user to enter people attending and their availability
    usersDatesDictionary={}
    print("Please enter the name of a user, then enter their availability in the form ALL ABSENT, NOT ABSENT, ALL ABSENT EXCEPT mm/dd/yyyy,mm/dd/yyyy...,NOT ABSENT EXCEPT mm/dd/yyyy,mm/dd/yyyy..., or just enter dates seperated by a comma. Enter as many users as you wish, when you are finished enter a -.\n")
    while True
        user=input("please enter the person's name. Enter - if you want to stop.")
        user.strip()
        if (user=="-"):
            break
        else :
            toAdd = User(user)
            usersDatesDictionary[toAdd]=[]
        while True
            dates=input("Please enter either ALL ABSENT, ALL PRESENT, a date range of the form mm/dd/yyyy:mm/dd/yyyy, or an individual date of the form mm/dd/yyyy and hit enter. When you wish to stop please enter - .")
            dates.replace(" ","")
            dates.lower()
            if (dates==allabsent):
                #we have to check off all absent
                toAdd.setAllUnavailable()
                do stuff
            elif (dates==allpresent):
                #we have to check off all present
                toAdd.setAllAvailable()
                do stuff
            elif (dates[10]==":"):
                #we have a date range
                do stuff
            else :
                #then we have an individual date

            
 




    
