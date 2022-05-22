'''Instructions
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
'''
'''Examples
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
'''
'''Thoughts
1. Get a dictionary to add and subtract bills
2. if b is 5 d[5] plus 1
3. if b is 10 d[10] plus 1 and d[5] minus 1
4. check if d[5] is less 0 if it is return False
5. if b is 20 either subtract a 10 and a 5 or 3 fives.
6. Check if d[5] id less that 0 if it is return False
7. Return True
'''

def change(bills):
    d = {'20': 0, '10':0, '5':0}
    for b in bills:
        if b == 5:
            d['5'] += 1
        elif b == 10:
            d['10'] += 1
            d['5'] -= 1
            if d['5'] < 0:
                return False
        else:
            d['20'] += 1
            if d['10'] > 0:
                d['10'] -= 1
                d['5'] -= 1
            else:
                d['5'] -= 3
            if d['5'] < 0:
                return False
    return True