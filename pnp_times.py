import timeit
 
#--------------------------------------------------------------------------------- 
# compute PNP time using previous version with loops
def previous_pnp():
    SETUP_CODE = '''
import climate_indices.indices as indices
import tests.fixtures as fixtures
precips = fixtures.FixturesTestCase.fixture_precips_mm_monthly.flatten()
data_year_start = fixtures.FixturesTestCase.fixture_data_year_start_monthly
calibration_year_start = fixtures.FixturesTestCase.fixture_calibration_year_start_monthly
calibration_year_end = fixtures.FixturesTestCase.fixture_calibration_year_end_monthly
'''
 
    TEST_CODE = '''
indices.previous_percentage_of_normal(precips, 
                                      6, 
                                      data_year_start, 
                                      calibration_year_start, 
                                      calibration_year_end, 
                                      'monthly')
'''
     
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 1000)
 
    # print the minimum execution time
    print('Previous PNP time: {}'.format(min(times)))        
 
#--------------------------------------------------------------------------------- 
# compute PNP time using new version with numpy broadcasting
def new_pnp():
    SETUP_CODE = '''
import climate_indices.indices as indices
import tests.fixtures as fixtures
precips = fixtures.FixturesTestCase.fixture_precips_mm_monthly.flatten()
data_year_start = fixtures.FixturesTestCase.fixture_data_year_start_monthly
calibration_year_start = fixtures.FixturesTestCase.fixture_calibration_year_start_monthly
calibration_year_end = fixtures.FixturesTestCase.fixture_calibration_year_end_monthly
'''
 
    TEST_CODE = '''
indices.percentage_of_normal(precips, 
                             6, 
                             data_year_start, 
                             calibration_year_start, 
                             calibration_year_end, 
                             'monthly')
'''
     
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 1000)
 
    # print the minimum execution time
    print('New PNP time: {}'.format(min(times)))        

#--------------------------------------------------------------------------------- 
if __name__ == "__main__":
    previous_pnp()
    new_pnp()
