For all the following exercises, you should be considering as many boundary cases as possible, adding type hints, and adding full documentation, preferrably with `numpy` style docstrings.

## Exercise 4.1

* Use a lambda function to sort a list of strings with a custom sorting rule
  * For example, you could do something like organize a list alphabetically based on the 2nd letter of their name.
  * This function should be able to handle a list like this:
    * ['Matthew', 'Tatsuto', 'Dongchen', 'Tony', 'Blake', 'Elena', 'Shangheng', "Margherita', 'Matt', 'Jim', 'Nick', 'Jacob', 'Roberto', 'Felix', 'Michela', 'Yuki', 'Behrad', 'Sateesh']
  

## Exercise 4.2

* Create a function that converts SI units of distances as a string argument into one of the decimal prefix numbers (i.e. convert it to SI with scientific notation)
  * This should be able to handle a list such as this:
    * ['1.4 A', '134 nm', '254 um', '530 mm', '765 cm', '812 m', '299 km']

## Exercise 4.3

* Create a sum function that handles an undefined number of inputs
  * This should be able to handle `int`, `float`, and complex numbers.

## Exercise 4.4

* Create a type-annotated function that computes the distances between two 3D points
  * All arguments should have type annotations, and you should be able to handle "Euclidean" and "Spherical" coordinates

## Exercise 4.5

* Create a function thyat takes a mandatory first and last name, but also an undefined number of keyword arguments (i.e. age, occupation, and location), and returns a dictionary
  * This should raise errors when unexpected types appear in the dictionary (i.e. `occupation` should not be 2)
