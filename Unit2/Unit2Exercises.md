## Exercise 2.1

* Create a function that takes a float and outputs a float to a specific number of integers (i.e. creating a rounding function).

  * This should have two inputs, the number, and the number of decimals
  * You are not allowed to use the `round` function; however, you are allowed to go to Wikipedia to look up the math behind rounding
  * This must round >=5 up, and <=4 down.

## Exercise 2.2

* Create a function that takes a string and places them where all numbers are valid, and there are 2 types. One is a comma, and the other is a semi-colon
* The function should take a string and print comma numbers vertically, and semi-colons horizontally. For example, the string "1.2,413.345;2,0.31" could look something like this:

1.2                 2

413.345       0.31

## Exercise 2.3

* Create a function that returns a postition based on a label on a grid of arbitrary size (*m* width X *n* height).
* The function should be made up of 4 inputs: label (string such as "B3"), direction (string such as "h" or "v"), width (integer such as 5 or 10), and height (integer such as 5 or 10)
* The output should let me know how many grid squares I would need to traverse to reach the associated point on the grid.
  * For example, let's say I had a grid of 5 rows by 7 columns (35 squares), where the rows are "A,B,C,D,E" and the columns are "1,2,3,4,5,6,7". If I wanted to locate position "B2". It would take 9 squares to traverse horizontally (i.e. A1, A2, A3, A4, A5, A6, A7, B1, B2), but it would only take 7 squares to go vertically (i.e. A1, B1, C1, D1, E1, A2, B2).
