﻿import MySQLConnector
import re

class User_Controller():

    def __init__(self):
        return

    def signin_handler(self,userName,password):
        
        print("Hello")
        psswdMatch = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$')
        ispswdMatch = psswdMatch.match(password)

        userMatch = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{6,15}$')
        isnameMatch = userMatch.match(userName)
        ##send to MySQLConnector
        if(ispswdMatch is not None and isnameMatch is not None ):
            params= (userName,password)
            mysqlptr = MySQLConnector.MySQL_Connector()
            row = mysqlptr.ExecuteSP_Params('sp_get_user',params)
            if(len(row) == 0):
                return 404#user not found
            else: 
                 return row#OK
        else:
            return 100 #wrong password/username format
       
    def signup_handler(self,uname,pswdf,email,fname,lname,number,address,city,zipCode,comments):
        #validation
        #reg exp
        #insertion
        params= (uname,pswdf,email,fname,lname,address,city,number,zipCode,comments,2)
        mysqlptr = MySQLConnector.MySQL_Connector()
        mysqlptr.ExecuteSP_Params('sp_insert_user',params)
        
            
