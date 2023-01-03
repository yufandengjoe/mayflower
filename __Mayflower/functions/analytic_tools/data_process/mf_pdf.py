import tabula
from functions.analytic_tools.data_process import mf_re


def check_pdf(file_name):
    '''
    Return True if the file format is pdf
    '''
    check_object = mf_re.regular_expression(raw_text="",
                                            search_text=file_name)
    return check_object.check_file_format('pdf')


class pdf_process:

    def __init__(self, file_name):
        self.file_name = file_name

    def parse_table(self):
        self.table = tabula.read_pdf(
            self.file_name,
            pages='all',
            multiple_tables=True,
            stream=True,
            guess=False
        )
        return self.table

    def filter_table(self, keyword: str):
        '''
        Filter the table based on keyword, only keep the tables contains the keyword
        '''
        self.page = []
        self.data = ""
        self.parse_table()
        for page_num in range(len(self.table)):

            # Break down in pure text structure
            data_slice = tables[page_num]

            # Detect desired word in each page
            txt = mf_re.regular_expression(
                raw_text=data_slice, search_text=keyword)
            try:
                txt.find_first()
            except:
                pass
            else:
                self.page.append(page_num)
                self.data += data_slice

        return self.page, self.data
