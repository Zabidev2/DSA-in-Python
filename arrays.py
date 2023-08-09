expences = {'January': 2000, 'February': 2350, 'March': 2600, 'April': 2130, 'May': 2190}

# 1. In Feb, how many dollars you spent extra compare to January?
print(f"In Feb I spent ${expences['February'] - expences['January']} extra as compared to Jan!")

# 2. Find out your total expense in first quarter (first three months) of the year.
print(f"The total expence in first quarter of the year is $"
      f"{expences['January'] + expences['February'] + expences['March']}")

# 3. Find out if you spent exactly 2000 dollars in any month
print(f"Did I spend $2000 in any month? {2000 in expences.values()} ") 

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expences['June'] = 1980
print(expences)

#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your
# monthly expense list based on this
expences['April'] = expences['April'] - 200
print(expences)


#Exercise 2
odd_numbers = []
number = input("Please input a number:")
print(number)
for num in range(int(number) + 1):
    if num%2 == 0:
        odd_numbers.append(num)


print(odd_numbers)




    