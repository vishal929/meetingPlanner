# Python Meeting Planner
This is some practice for myself with python. So far, I have really only delved deep into Java and C, so I wanted to get more practice with Python. This project is a simple meeting planner, where a user can enter a date range for an event, then the user can enter participants for the event and their availabilities and the program will return a list of best dates, which minimize the number of absences of the participants.

## What's needed to Run this?
Please install Python3 and run from command line as "python3 meetingPlanner.py"

## Program Intuition:
Basically, I am creating a graph where the nodes are possible dates for the event in question, given by the user. Then, for each dateNode, there is a list of users which are absent on that day, and an integer with the length of this list (This simulates a bipartite graph without actually making UserNodes). By going through all the possible dates and finding the nodes with the least degree, I can find the best dates for this event. Then, this is displayed to the user.

## Program I/O
The user is first asked to give a date range for the event in the form "mm/dd/yy:mm/dd/yy". Then, the user is asked to enter names of participants and their absence dates/date-ranges or "ALL PRESENT" (if the participant is never absent) or "ALL ABSENT" (if the participant is absent on every possible day). Then, the user is given a list of all best days to hold the event (best meaning that those days have the least number of absences compared to all other possible days to hold the event)
