import configparser
import os
import shutil


class folder_process:

    def __init__(self,
                 file_name: str,
                 file_path: str):
        self.file_name = file_name
        self.file_path = file_path
        self.full_path = os.path.join(file_path, file_name)
        self.current_working_directory = os.getcwd()
        self.config = configparser.ConfigParser()

    def check_path_existence(self):
        '''
        Check if a path exist
          - if not, create a new path
          - raise exception if fail to create
        '''

        directory = os.path.dirname(self.file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        assert os.path.exists(
            directory), "Failed to create directory >%s<" % self.file_name
        return None

    def check_file_existence(self):
        '''
        Check if a file exists
          - raise exception if not
        '''

        self.check_path_existence()
        assert os.path.exists(
            self.full_path), "File does not exist: >%s<" % self.file_name
        return None

    def parse_config(self):
        '''
        Read configuration from a file
        '''

        try:
            self.config.read(self.full_path)
        except:
            msg = "Cannot parse configuration file >%s<" % self.file_name
            raise KeyError(msg)

        return None

    def save_config(self, new_config_dict: dict):
        '''
        Create or overwrite configuration
        '''

        try:
            self.config.read(self.full_path)
            self.config.read_dict(new_config_dict)
        except:
            with open(self.full_path, "w") as config_file:
                self.config.write(config_file)
        return None

    def folder_search(self,
                      prefix=None,
                      format_filter=None,
                      remove_path=False,
                      remove_format=False
                      ):
        '''
        Return a list of file names from search query
            - prefix does not require full path, just starting letters of file name
            - format_filter specifies the file format, e.g. ".xlsx"
            - remove_path removes the path in the query result
            - remove_format removes the file format in query result
        '''

        self.file_lst = [[os.path.join(root, file) for file in files]
                         for root, dirs, files in os.walk(self.file_path)[0]]

        if prefix:
            self.file_lst = [file for file in self.file_lst if file.startswith(
                os.path.join(self.file_path, prefix))]

        if format_filter:
            self.file_lst = [
                file for file in self.file_lst if file.endswith(format_filter)]

        if remove_path:
            self.file_lst = [file.split("\\")[-1] for file in self.file_lst]

        if remove_format:
            self.file_lst = [file.split(".")[0] for file in self.file_lst]

        return self.file_lst

    def return_last_file(self,
                         by="order",
                         prefix=None,
                         format_filter=None,
                         remove_path=False,
                         remove_format=False):
        '''
        Return the file in the folder that is the last
            - by = "order" returns the alphabetical last file
            - by = "time" returns the latest modified file
        '''

        self.folder_search(prefix=prefix,
                           format_filter=format_filter,
                           remove_path=remove_path,
                           remove_format=remove_format)

        if by == "order":
            self.last_file = max(self.file_lst)
        elif by == "time":
            self.last_file = max(self.file_lst, key=os.path.getmtime)
        return self.last_file

    def copy_file(self, from_path, to_path):
        '''
        Copy a file from from_path to to_path
        '''
        shutil.copy2(from_path, to_path)
        return None
