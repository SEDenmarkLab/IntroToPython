For all the following exercises, you should be considering as many boundary cases as possible, adding type hints, and adding full documentation, preferrably with `numpy` style docstrings.

## Exercise 5.1

* Create a class for a 3D point (i.e. xyz)
  * Raise a `TypeError` if a non-numeric string/object is passed in initalization
  * Define a custom subtraction operator which returns Euclidean distance between the points
  * Define a custom equals operator that returns "True" if the distance between the two points is less than 1e-6
  * Define a custom representation function that has some fancy printout (i.e. Point3D(x=0.134, y=14.230, z=231.145))

## Exercise 5.2

* Create similar classes as **Exercise 5.1** using different syntax
  * Do this `namedtuple`
    * You do not need to define custom operators/representations, solely instantiate an xyz with a similar name
  * Do this with `dataclass`
  * Do with this `attrs`
  * Understand the difference between your 3D point class, `namedtuple`, `dataclass`, and `attrs`.

## Exercise 5.3

* Create a class method that is used to show the difference between a class and an instance
  * This should actually demonstrate the difference with the methods.

## Exercise 5.4

* Design a class that inherits from the 3D point class but adds a mass attribute to the "child class"
  * Make the mass property protected
  * Write a `@property`getter that reads the mass and a `setter`method to change the mass
    * Raise a `ValueError` in the setter if the user attempts to set a negative mass.
