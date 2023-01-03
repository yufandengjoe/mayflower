import re


class regular_expression:

    def __init__(self, raw_text: str, search_text: str):
        self.raw_text = raw_text
        self.search_text = search_text

    def find_first(self, start_with=None, end_with=None):
        '''
        Find the first occurance and location of query text
            - span method: return the starting and ending position of first matching text
            - string method: return the string that meets the criteria
            - start_with and end_with only search the beginning and ending nodes of text
        '''

        start_sign = '^' if start_with else ''
        end_sign = '$' if end_with else ''
        txt = re.search(start_sign + self.search_text +
                        end_sign, self.raw_text)
        print("(Beginning, Ending) Location: {}".format(txt.span()))
        print("The string matches search is: " + txt.string)

        return None

    def find_all(self, start_with=None, end_with=None):
        '''
        Find all occurances and locations of query text
            - span method: return the starting and ending position of first matching text
            - string method: return the string that meets the criteria
            - start_with and end_with only search the beginning and ending nodes of text
        '''

        start_sign = '^' if start_with else ''
        end_sign = '$' if end_with else ''
        txt = re.finditer(start_sign + self.search_text +
                          end_sign, self.raw_text)

        for instance in txt:
            print("(Beginning, Ending) Location: {}".format(instance.span()))
            print("The string matches search is: " + instance.string)

        return None

    def find_all_subtext(self, substring=False):
        '''
        Find all strings of query text
            - substring controls for substring query
        '''
        self.string_lst = re.findall(r'\B' + self.search_text + r'\B', self.raw_text) if not substring else re.findall(
            r'[a-zA-Z]*' + self.search_text + r'[a-zA-Z]*', self.raw_text
        )
        return self.string_lst

    def frequent_use_case(self):
        '''
        Find common data types in raw data
        '''
        self.numeric = re.findall(
            r'^-?\d+(,\d+)*(\.\d+(e\d+)?)?$', self.raw_text)
        self.phone = re.findall(
            r'1?[\s-]?\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}', self.raw_text)
        self.email = re.findall(
            r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
        self.html = re.findall(r'<[^>]*>', self.raw_text)
        self.pic = re.findall(r'(\w+)\.(jpg|png|gif)$', self.raw_text)

        return None

    def check_file_format(self, format: str):
        '''
        return True if file ends with desired format, e.g. 'pdf'
        '''
        return re.search(r'(\w+)\.(' + format + ')$', self.search_text)

    def remove_substring(self):
        '''
        remove all substring from text
        '''
        self.reduced_text = re.sub(self.search_text,
                                   "",
                                   self.raw_text,
                                   count=0,
                                   flag=0)
        return self.reduced_text
