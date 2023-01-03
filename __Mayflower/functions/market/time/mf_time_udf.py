from datetime import datetime
from functions.market.time import mf_date


class time_process:

    def __init__(self, time_object):
        self.time_object = time_object

    def yyyymmdd_to_date(self):
        '''
        Convert "yyyymmdd" string to datetime object
        '''
        self.date_object = datetime.strptime(self.time_object, '%Y%m%d')
        return self.date_object

    def oracle_date_converter(self):
        '''
        Convert a datetime object to oracle SQL query date format
        '''
        return '{}/{}/{}'.format(self.date_object.day,
                                 mf_date.Oracle_month(
                                     self.date_object.month).name,
                                 self.date_object.year)
