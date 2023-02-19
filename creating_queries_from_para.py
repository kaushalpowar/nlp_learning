'''
Creating queries from parameters
Now you're going to implement a more powerful function for querying the hotels
database. The goal is for that function to take arguments that can later be
specified by other parts of your code.


More specifically, your job is to define a find_hotels() function which takes
a single argument - a dictionary of column names and values - and returns a
list of matching hotels from the database.
'''

# Define find_hotels()
def find_hotels(params):
    # Create the base query
    query = 'SELECT * FROM hotels'
    # Add filter clauses for each of the parameters
    if len(params) > 0:
        filters = ["{}=?".format(k) for k in params]
        query += " WHERE " + " and ".join(filters)
    # Create the tuple of values
    t = tuple(params.values())
    
    # Open connection to DB
    conn = sqlite3.connect("hotels.db")
    # Create a cursor
    c = conn.cursor()
    # Execute the query
    c.execute(query, t)
    # Return the results
    return c.fetchall()

#params = {"area":"south","price":"lo"}

