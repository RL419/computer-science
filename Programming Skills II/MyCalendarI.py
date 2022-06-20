'''Instructions
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
'''
'''Examples
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
'''
'''Thoughts
1. init creates a list of tuple for booked time
2. book loops through every booked time and check if the start and end overlaps with any starts and ends
3. If it does return false
4. Else add start and end into booked time and return true
'''

class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.booked:
            if s < end and start < e:
                return False
        self.booked.append((start,end))
        return True