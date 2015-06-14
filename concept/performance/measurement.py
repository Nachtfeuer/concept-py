import time

def track_duration_of(function, *args, **kwargs):
    """
    Tracks execution time of a single function.

    :param function: function to measure
    :param args: single value arguments
    :param wkargs: key/value arguments
    :returns: duration in seconds (float)
    """
    start = time.time()
    function(*args)
    return time.time() - start
