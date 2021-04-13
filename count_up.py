def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    list_to_max_stop = range(start, stop + 1)

    for num in list_to_max_stop:
        print(num)
    # if(start < stop):
        


count_up(5, 7)        
