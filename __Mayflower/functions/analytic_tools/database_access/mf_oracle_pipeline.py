import cx_Oracle
import getpass
import os
import pandas as pd
import sqlalchemy
from functions.core import mf_user_info


class oracle_connect:

    def __init__(self,
                 data_base: str,
                 table_name: str,
                 SQL_query=None,
                 data_frame=None,
                 application="oracle",
                 module="cx_oracle"
                 ):
        self.database = data_base
        self.table_name = table_name.lower()
        self.SQL_query = SQL_query
        self.data_frame = data_frame
        self.application = application
        self.module = module

        return None

    def load_user_info(self):
        info_loader = mf_user_info.user_info()
        try:
            self.__username, self.__password, self.__hostname, self.__servicename = info_loader.extract_user_info(
                self.application + self.database)
        except:
            self.__username, self.__password, self.__hostname, self.__servicename = info_loader.input_user_info(
                self.application + self.database)
        return None
