import getpass
import os


class user_info:

    def __init__(self) -> None:
        pass


    def extract_user_info(self, file_name):
        '''
        extract user info from local save
        '''
        txt = open(
            "C://Users//" + os.getlogin() + "//AppData//Roaming//user_access//" + file_name + ".txt", "r")
        self.__username = txt.readline().strip()
        self.__password = txt.readline().strip()
        self.__hostname = txt.readline().strip()
        self.__servicename = txt.readline().strip()

        return self.__username, self.__password, self.__hostname, self.__servicename

    
    def input_user_info(self, file_name):
        '''
        establish user info and save local temp at first time
        '''
        self.__username = input('Enter username here')
        self.__password = getpass.getpass('Enter password here')
        self.__hostname = input('Enter hostname here')
        self.__servicename = input('Enter servicename here')

        file = open(
            "C://Users//" + os.getlogin() + "//AppData//Roaming//user_access//" + file_name + ".txt", "x")
        file.write(self.__username + '\n' + self.__password + '\n' + self.__hostname + '\n' + self.__servicename) 
        file.close()

        print('User info saved to local temp file!')

        return self.__username, self.__password, self.__hostname, self.__servicename
        