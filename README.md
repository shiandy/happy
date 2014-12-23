happy
=====

Playing around with some stuff.

Code to calculate [happy numbers](https://en.wikipedia.org/wiki/Happy_number)

Approach
---------

Given a number n, we generate a sequence by taking the sum of the squares of its
digits to get n1. Then we do the same to n1 to get n2, and so on. The number n
is happy if this process eventually converges to 1. 

The approach we take is quite simple. We can show that this algorithm applied to
any number either converges to 1 or the "non-convergent" sequence 

4, 16, 37, 58, 89, 145, 42, 20, 4,...

Let a number n have d digits. The maximum possible sum of squares of digits is
9^2 times the number of digits, which is 81d. Then, with d `>=` 4, we have

n `>=` 10^(d-1) > 81d

So any number bigger than 999 gets smaller. The number from 1 to 999 with the
largest sum of squared digits is 999, whose sum of squared digits is 243. So all
numbers between 244 and 999 become less than 244. The number from 1 to 243 with
the largest sum of squared digits is 199, whose sum of squared digits is 163.
The number under 163 with largest sum of squared digits is 159, which becomes
107. Then, number with the largest sum of squared digits less than or equal to
107 is 107, which becomes 50. 

So all numbers greater than 99 become a number less than or equal to 99 in this
process. Then, the code in `happy_experiment.py` verifies that all of these
numbers from 1 to 99 either ends in 1 or the sequence described above. 

Performance
-----------

The basic way to compute whether or not a number is happy is to apply the
algorithm and at every step check if the number is 1 or 4. I found that by
checking if the number is any of the elements in the "non-convergent" sequence,
we could speed up the process a little. I tested a binary search approach, but
because the list of unique elements in the non-convergent sequence is short,
this had worse approach because function calls are expensive in Python. 

To quickly compute squares, I created a dictionary that mapped the string form
of a digit 0-9 to its square (as an int). 


Files
------

* `happy.py`: The main code that contains the function that checks whether or
  not a number is happy, as well as driver code to check which of the numbers
  from 1 to 10000 is happy. 

* `happy_experiment.py`: Verifies that all numbers between 1 and 99 inclusive
  end in the "non-convergent" sequence given above. 

* `test_happy.py`: Contains unit tests.


References
https://en.wikipedia.org/wiki/Happy_number

