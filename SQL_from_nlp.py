'''
Creating SQL from natural language
Now you'll write a respond() function that can handle messages like
"I want an expensive hotel in the south of town" and respond appropriately
according to the number of matching results in a database. This is an
important functionality for any database-backed chatbot.

Your find_hotels() function from the previous exercises has already been
defined for you, along with a Rasa NLU interpreter object, which can handle
hotel queries, and a list of responses, which you can explore in the Shell.
'''
# Define respond()
def respond(message):
    # Extract the entities
    entities = interpreter.parse(message)["entities"]
    # Initialize an empty params dictionary
    params = {}
    # Fill the dictionary with entities
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])

    # Find hotels that match the dictionary
    results = find_hotels(params)
    # Get the names of the hotels and index of the response
    names = [r[0] for r in results]
    n = min(len(results),3)
    # Select the nth element of the responses array
    return responses[n].format(*names)

# Test the respond() function
print(respond("I want an expensive hotel in the south of town"))

#Output
#Grand Hotel is a great hotel!
