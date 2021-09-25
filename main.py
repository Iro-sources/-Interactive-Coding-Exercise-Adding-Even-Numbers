#Write your code below this row 👇
#This program calculates the sum of all the even numbers from 1 to 100.
sum_numbers =0
for number in range(1, 101):
    if number % 2 == 0:
        sum_numbers += number
print(sum_numbers)

sum_numbers =0
for number in range(2, 101, 2):
  sum_numbers += number
print(sum_numbers)