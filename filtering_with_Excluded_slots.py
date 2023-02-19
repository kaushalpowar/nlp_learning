'''
Filtering with excluded slots
Now you're going to put together some of the ideas from previous exercises in
order to allow users to tell your bot about what they do and do not want,
split across multiple messages.

The negated_ents() function has already been defined for you. Additionally,
a slightly tweaked version of the find_hotels() function, which accepts a
neg_params dictionary in addition to a params dictionary, has been defined.

'''
# Define the respond function
def respond(message, params, neg_params):
    # Extract the entities
    entities = interpreter.parse(message)["entities"]
    ent_vals = [e["value"] for e in entities]
    # Look for negated entities
    negated = negated_ents(message, ent_vals)
    for ent in entities:
        if ent["value"] in negated and negated[ent["value"]]:
            neg_params[ent["entity"]] = str(ent["value"])
        else:
            params[ent["entity"]] = str(ent["value"])
    # Find the hotels
    results = find_hotels(params, neg_params)
    names = [r[0] for r in results]
    n = min(len(results),3)
    # Return the correct response
    return responses[n].format(*names), params, neg_params

# Initialize params and neg_params
params = {}
neg_params = {}

# Pass the messages to the bot
for message in ["I want a cheap hotel", "but not in the north of town"]:
    print("USER: {}".format(message))
    response, params, neg_params = respond(message, params, neg_params)
    print("BOT: {}".format(response))
