#!/usr/bin/python

import sys
import mysql.connector
import datasift

class Env(object):
    """
    Sets up and provides access to the environment for the Push examples.
    """
    _args = []
    _user = None
    
    def __init__(self, args):
        if len(args) < 2:
            sys.stderr.write("Please specify your DataSift username and API key as the first two command line arguments\n")
            sys.exit(1)
            
        self._user = datasift.User(args[1], args[2])
        
    def get_user(self):
        return self._user
    

class MySqlHelper(object):

    _username     = ""
    _password     = ""
    _host         = ""
    _database     = ""

    def __init__(self, username, password, host, database):
        self._username = username
        self._password = password
        self._host = host
        self._database = database

    def return_columns(self, table_name):
        # Open MySQL Connection
        cnx = mysql.connector.connect(user=self._username,  password=self._password, host=self._host, database=self._database)
        columns = []
        query = "show columns from {0}".format(table_name)
        cursor = cnx.cursor()
        cursor.execute(query)

        for (Field, Type, Null, Key, Default, Extra) in cursor:
            columns.append(Field)

        cnx.commit()
        cursor.close()
        cnx.close()

        return columns
    
    def connect(self):
        self._cnx = mysql.connector.connect(user=self._username,  password=self._password, host=self._host, database=self._database)
        return self._cnx

    def execute_query(self, query, data=''):
        self._cnx.autocommit = False
        
        self._cursor = self._cnx.cursor()
        self._cursor.execute(query, data)

    def commit(self):
        self._cnx.commit()
        self._cursor.close()
        self.close()   
        
    def close(self):
        self._cnx.close() 

