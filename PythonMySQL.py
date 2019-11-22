import requests                         #allows to send and get info to or from an endpoint
import mysql.connector                  #allows you to connect to a mySQL db

def main():
	
    connection = mysql.connector.connect(host='hostname',   #establishes connection to mySQL db with credentials
                                        user='username',
                                        passwd='password',
                                        db='db_name')

    cursor = connection.cursor()                                            #creates a cursor to navigate db info
    query="SELECT columnName FROM dbName WHERE rowName='ExampleRowName'"    #constructs an SQL Query as a string; this can be formatted as any valid SQL query
    cursor.execute(query)                                                   #executes the SQL query
    result=cursor.fetchall()                                                #grabs info returned from query (returned as a list)
    
    print(result)               #any logic you'd like to do to the 'results' list can be done here
        
    connection.close()          #closes connection to db (not necessary in learning, but good practice and is necessary in the real world)
    

main()                          #calls main function