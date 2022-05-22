'''Instructions
Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
'''
'''Examples
Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
'''
'''Thoughts
1. Generate a list of all the seats in reverse order
2. For reserve return and pop the last value
3. If length of seats is zero or seatnumber is less than the last element append it to the list
4. Else loop through seats from the last element and if seatnumber is greater that the elemetn in seats add it the correct index and exit the loop
'''

class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1, n+1)][::-1]

    def reserve(self) -> int:
        return self.seats.pop()

    def unreserve(self, seatNumber: int) -> None:
        if len(self.seats) == 0 or seatNumber < self.seats[-1]:
            self.seats.append(seatNumber)
        else:
            for i in range(len(self.seats) - 2, -1,-1):
                if seatNumber < self.seats[i]:
                    self.seats.insert(i+1, seatNumber)
                    break