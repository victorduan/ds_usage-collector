ds_usage-collector
==================

A Python script to collect DataSift account usage into a database (MySQL)

Requirements
------------

* Python 2.7.2 or similar
* MySQL 5.5.24 and above
* [mysql-connector-python](http://dev.mysql.com/downloads/connector/python/) : MySQL Connector/Python standardized database driver
* [datasift-python](https://github.com/datasift/datasift-python) : Python client to interface with DataSift

Usage
-----

* Update config.py with your MySQL database credentials
* Create a table with the provided script: `mysql db_name -u user -p < table_creation.sql`
* Run the collector.py script: `python collector.py datasift_username datasift_api_key`

Changelog
---------

* v.0.2.0 - Performance enhancements; Reduced the time for multiple inserts into MySQL (2013-05-28)
* v.0.1.0 - Initial version (2013-05-20)

