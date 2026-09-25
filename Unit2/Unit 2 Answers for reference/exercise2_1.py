from math import floor
def round(number, decimal):
    """rounding a number to a certain decimal

    Parameters
    ----------
    number : float
        takes in a float to be rounded
    decimal : int
        takes in a decimal places

    Returns
    -------
    float
        return the rounded number in float
    """
    factor = 10 ** decimal
    shifted = floor(number * factor + 0.5) 
    #I use floor() instead of int() because floor works better when the input number is negative
    output = shifted / factor
    print("my rounding method") 
    #just want to make sure that it is using my rounding method instead of the round() method in Python
    return output


print(round(-3.14159, 4))
#for testing 