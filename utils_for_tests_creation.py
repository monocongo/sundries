import logging
import numpy as np

#-----------------------------------------------------------------------------------------------------------------------
# set up a basic, global _logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d  %H:%M:%S')
_logger = logging.getLogger(__name__)

#-----------------------------------------------------------------------------------------------------------------------
def reshape_to_2d(values,
                  second_axis_length):
    '''
    :param values: an 1-D numpy.ndarray of values
    :param second_axis_length: 
    :return: the original values reshaped to 2-D, with shape (int(original length / second axis length), second axis length)
    :rtype: 2-D numpy.ndarray of floats
    '''
    
    # if we've been passed a 2-D array with valid shape then let it pass through
    shape = values.shape
    if len(shape) == 2:
        if shape[1] == second_axis_length:
            # data is already in the shape we want, return it unaltered
            return values
        else:
            message = 'Values array has an invalid shape (2-D but second dimension not 12): {}'.format(shape)
            _logger.error(message)
            raise ValueError(message)
    
    # otherwise make sure that we've been passed in a flat (1-D) array of values    
    elif len(shape) != 1:
        message = 'Values array has an invalid shape (not 1-D or 2-D): {0}'.format(shape)
        _logger.error(message)
        raise ValueError(message)

    # pad the end of the original array in order to have an ordinal increment, if necessary
    final_year_months = shape[0] % second_axis_length
    if final_year_months > 0:
        pad_months = second_axis_length - final_year_months
        pad_values = np.full((pad_months,), np.NaN)
        values = np.append(values, pad_values)
        
    # we should have an ordinal number of years now (ordinally divisible by second_axis_length)
    increments = int(values.shape[0] / second_axis_length)
    
    # reshape from (months) to (years, 12) in order to have one year of months per row
    return np.reshape(values, (increments, second_axis_length))
            
#-----------------------------------------------------------------------------------------------------------------------
def print_years_months(values):
    """
    Takes an input array of value and prints it as if it were a 2-D array with (years, month) as dimensions, 
    with one year written per line and missing years listed as NaNs. Designed to accept an array of monthly values,
    with the initial value corresponding to January of the initial year.
    
    Useful for printing a timeseries of values when constructing a test fixture from running code that has results 
    we'd like to match in an unit test, etc.
    
    :param values: 
    """

    # reshape the array, go over the two dimensions and print
    values = reshape_to_2d(values, 12)
    for i in range(values.shape[0]):
        year_line = ''.join("%6.3f, " % (v) for v in values[i])
        print('        ' + year_line + ' \\')

#-----------------------------------------------------------------------------------------------------------------------
def print_years_days(values):
    """
    Takes an input array of value and prints it as if it were a 2-D array with (years, month) as dimensions, 
    with one year written per line and missing years listed as NaNs. Designed to accept an array of monthly values,
    with the initial value corresponding to January of the initial year.
    
    Useful for printing a timeseries of values when constructing a test fixture from running code that has results 
    we'd like to match in an unit test, etc.
    
    :param values: 
    """

    # reshape the array, go over the two dimensions and print
    values = reshape_to_2d(values, 366)
    print('[ ')
    for i in range(values.shape[0]):
        print('  [ ')
        # print 10 values per line
        for j in range(0, values.shape[1], 10):
            year_line = ''.join("%6.3f, " % (v) for v in values[i, j:j+10])
            print('        ' + year_line + ' \\')
        print(' ], \\')
    print(']')
