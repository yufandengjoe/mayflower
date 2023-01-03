import numpy as np
import os
import pandas as pd
import xlwings as xw


class xlwings_read:

    def __init__(self,
                 path: str,
                 book_name: str,
                 sheet_name: str,
                 cell_range: str):
        self.path = path
        self.book_name = book_name
        self.sheet_name = sheet_name
        self.cell_range = cell_range

    def read_excel(self):
        '''
        Function to open a table provided the spreadsheet name, worksheet name and cell range
        '''
        self.table = xw.Book(os.path.join(self.path, self.book_name)).sheets(
            self.sheet_name).range(self.cell_range).options(
                pd.DataFrame, chunksize=10000).value
        self.table = self.table.replace(
            '', np.nan, regex=True).dropna(axis=0, how='all')

        return self.table
