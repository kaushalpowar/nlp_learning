'''
Intent classification with regex I
You'll begin by implementing a very simple technique to recognize intents -
looking for the presence of keywords.

A dictionary, keywords, has already been defined. It has the
intents "greet", "goodbye", and "thankyou" as keys, and lists
of keywords as the corresponding values. For example, keywords["greet"]
is set to "["hello","hi","hey"].

Also defined is a second dictionary, responses, indicating how the bot
should respond to each of these intents. It also has a default response
with the key "default".

The function send_message(), along with the bot and user templates, have
also already been defined. Your job in this exercise is to create a dictionary
with the intents as keys and regex objects as values.
'''

#responses
'''
{'default': 'default message',
 'goodbye': 'goodbye for now',
 'greet': 'Hello you! :)',
 'thankyou': 'you are very welcome'}
'''
#keywords
'''

{'goodbye': ['bye', 'farewell'],
 'greet': ['hello', 'hi', 'hey'],
 'thankyou': ['thank', 'thx']}
'''
# Define a dictionary of patterns
patterns = {}

# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))

# Print the patterns
print(patterns)
