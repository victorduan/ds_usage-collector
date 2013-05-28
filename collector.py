#!/usr/bin/python

import sys
import logging
import config
import time
import calendar
from env import Env
from env import MySqlHelper

if config.logLevel == "info":
    logging.basicConfig(format='%(asctime)s | %(levelname)s | %(filename)s | %(message)s', level=logging.INFO, filename=config.logFile)
else:
    logging.basicConfig(format='%(asctime)s | %(levelname)s | %(filename)s | %(message)s', level=logging.DEBUG, filename=config.logFile)


if __name__ == "__main__":
   
    table_name = config.mysql_table

    # Create object for internal database methods (mySQL)
    mysql = MySqlHelper(config.mysql_username, config.mysql_password, config.mysql_host, config.mysql_database)

    retry = 3
    while retry:
        try:
            logging.info("Getting valid columns from MySQL database.")
            valid_sources = mysql.return_columns(table_name)
            valid_sources = [ col for col in valid_sources if col not in ('intID', 'username', 'start', 'end', 'stream_type', 'stream_hash', 'seconds') ]
            logging.debug("Columns found: {0}".format(valid_sources))
            retry = 0
        except Exception, err:
            logging.exception(err)
            retry -= 1
            logging.warning("Retries left: {0}".format(retry))
            time.sleep(2) # Sleep 2 seconds before retrying
    
    # Open a MySQL connection
    mysql.connect()
    
    # Set up the environment
    env = Env(sys.argv)
    
    username = sys.argv[1]

    retry = 3
    while retry:
        try:
            usage = env.get_user().get_usage(config.usage_interval)
            logging.info("Getting /usage for user: {0}".format(username))
            print "Getting /usage for user: {0}".format(username)
            retry = 0
        except Exception, err:
            logging.exception("Encountered getting /usage for user: {0}. Error message: {1}".format(username, err))
            retry -= 1
            logging.warning("Retries left: {0}".format(retry))
            time.sleep(5) # Sleep 5 seconds before retrying


    date_format = "%a, %d %b %Y %H:%M:%S +0000"
    start       = time.strptime(usage['start'], date_format)
    end         = time.strptime(usage['end'], date_format)

    unix_start  = calendar.timegm(start)
    unix_end    = calendar.timegm(end) 

    insert_string = ''
    
    for stream in usage['streams']:
        if len(stream) == 32:
            stream_type = "stream"
        else:
            stream_type = "historic"

        seconds = usage['streams'][stream]['seconds']

        data = {
            'username'       : username,
            'start'          : unix_start,
            'end'            : unix_end,
            'stream_type'    : stream_type,
            'stream_hash'    : str(stream),
            'seconds'        : seconds
        }

        licenses = usage['streams'][stream]['licenses']

        if len(licenses):
            for license_type, license_value in licenses.items():
                # Only add licenses for columns that exist in the database
                if any(str(license_type) in x for x in valid_sources):
                    data[str(license_type)] = license_value

            fields_string = ", ".join([ "`{0}`".format(k) for k in licenses.keys() ])
            values_string = ", ".join([ "%({0})s".format(k) for k in licenses.keys() ])

            insert_query = ("""
                            INSERT INTO {0} 
                            (`username`, `start`, `end`, `stream_type`, `stream_hash`, `seconds`, {1}) 
                            VALUES ('%(username)s', %(start)s, %(end)s, '%(stream_type)s', '%(stream_hash)s', %(seconds)s, {2});
                            """).format(table_name, fields_string, values_string)

        # Different MySQL Query if there is no license consumption
        else:
            insert_query = ("""
                            INSERT INTO {0} 
                            (`username`, `start`, `end`, `stream_type`, `stream_hash`, `seconds`) 
                            VALUES ('%(username)s', %(start)s, %(end)s, '%(stream_type)s', '%(stream_hash)s', %(seconds)s);
                            """).format(table_name)
        
        # Concatenate all the INSERT statements    
        insert_string += " ".join(insert_query.split()) % data
    
    try:
        insert_count= 0 
        cursor = mysql.execute_many(insert_string)
        for insert in cursor:
            insert_count += 1
            
        # Commit the inserts for the user (if there are results)
        if insert_count: mysql.commit()
        else:            mysql.close()
    except Exception, err:
        logging.exception(err)
        sys.exit()
        
    logging.info("Tasks completed.")

