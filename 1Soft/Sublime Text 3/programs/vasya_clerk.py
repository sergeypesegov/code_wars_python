'''The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bill'''

def tickets(people):
    counter_25 = 0
    counter_50 = 0
    
    for ticket in people:
        if ticket == 25:
            counter_25 += 1
            
        elif ticket == 50 and counter_25 >= 1:
            counter_25 -= 1
            counter_50 += 1
            
        elif ticket == 100 and (counter_25 >=3 or (counter_25 >= 1 and counter_50 >= 1)):
            if counter_50 >= 1:
                counter_50 -= 1
                counter_25 -= 1
            else:
                counter_25 -= 3
            
        else:
            return 'NO'
    return 'YES'