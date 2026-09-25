def extract_numbers(string):
    """Extract the numbers separated by ";" or "," from a given string and categorize them into different orientation

    Parameters
    ----------
    string : string
        Take in a string with separated numbers

    Returns
    -------
    null
        no return, only print comma numbers vertically, and semi-colons horizontally
    """
    columns = string.split(";")
    grid = []
    for column in columns:
        num = column.split(",")
        grid.append(num)
        #the grid is now [['1.2', '413.345'], ['2', '0.31']]
    longest_column = []
    for column in grid:
        if len(column) > len(longest_column):
            longest_column = column
    height = len(longest_column)
    #I add this because I want to find the longest column to use that as the number of iteration
    #since the length of each column might not be the same
    #e.g 1.2;413.345,2,0.31 instead of 1.2,413.345;2,0.31
    for i in range(height):
        rows = []
        for column in grid:
            if i < len(column):
                rows.append(column[i])
            else:
                rows.append("  ")
                #if this column is short shorter than the longest column, I will replace the rest by spaces
        print(rows)

extract_numbers("1.2,413.345;2,0.31")
#for testing 