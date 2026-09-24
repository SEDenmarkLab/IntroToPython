def steps(label, direction, width, height):
    """_summary_

    Parameters
    ----------
    label : String
        Label that shows the location
    direction : String
        "v" or "h" that indicate the direaction(vertical or horizontal)
    width : int
        the width of the grid(how many rows)
    height : int
        the height of the grid(how many columns)

    Returns
    -------
    int
        return the steps in order to traverse to reach the associated point(location showed on the label)
    """
    rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    row_number = rows.index(label[0]) + 1
    # A is indexed 0 but it means to have 1 row
    column_number = int(label[1:])
    output = 0
    if direction == "h":
        complete_rows = row_number - 1
        #rows before the current row will be count completely
        output = (complete_rows * width) + column_number
    elif direction == "v":
        complete_columns = column_number - 1
        #columns before the current column will be count completely
        output = (complete_columns * height) + row_number
    return output

print(steps("B2", "v", 5, 7))
#for testing