'''
Refining your search
Now you'll write a bot that allows users to add filters incrementally,
just in case they don't specify all of their preferences in one message.

To do this, initialize an empty dictionary params outside of your respond()
function (as opposed to inside the function, like in the previous exercise).
Your respond() function will take in this dictionary as an argument.

'''
# Define a respond function, taking the message and existing params as input
def respond(message, params):
    # Extract the entities
    entities = interpreter.parse(message)["entities"]
    # Fill the dictionary with entities
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])

    # Find the hotels
    results = find_hotels(params)
    names = [r[0] for r in results]
    n = min(len(results), 3)
    # Return the appropriate response
    return responses[n].format(*names), params

# Initialize params dictionary
params = {}

# Pass the messages to the bot
for message in ["I want an expensive hotel", "in the north of town"]:
    print("USER: {}".format(message))
    response, params = respond(message, params)
    print("BOT: {}".format(response))


'''
USER: I want an expensive hotel
BOT: Grand Hotel is one option, but I know others too :)
USER: in the north of town
BOT: Ben's BnB is a great hotel!
'''
