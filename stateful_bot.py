'''
Form filling

You'll often want your bot to guide users through a series of steps,
such as when they're placing an order.

In this exercise, you'll begin building a bot that lets users order coffee.
They can choose between two types: Colombian and Kenyan. If the user provides
unexpected input, your bot will handle this differently depending on where they
are in the flow.

Your job here is to identify the appropriate state and next state based on the
intents and response messages provided. For example, if the intent is "order",
then the state changes from INIT to CHOOSE_COFFEE.

A function send_message(policy, state, message) has already been defined for
you. It takes the policy, the current state, and message as arguments, and
returns the new state as a result. Additionally, an interpret(message)
function, similar to the one Alan described in the video, has been pre-defined
for you.

'''
# Define the INIT state
INIT = 0

# Define the CHOOSE_COFFEE state
CHOOSE_COFFEE = 1

# Define the ORDERED state
ORDERED = 2

# Define the policy rules
policy = {
    (INIT, "order"): (CHOOSE_COFFEE, "ok, Colombian or Kenyan?"),
    (INIT, "none"): (INIT, "I'm sorry - I'm not sure how to help you"),
    (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "perfect, the beans are on their way!"),
    (CHOOSE_COFFEE, "none"): (CHOOSE_COFFEE, "I'm sorry - would you like Colombian or Kenyan?"),
}

# Create the list of messages
messages = [
    "I'd like to become a professional dancer",
    "well then I'd like to order some coffee",
    "my favourite animal is a zebra",
    "kenyan"
]

# Call send_message() for each message
state = INIT
for message in messages:    
    state = send_message(policy,state,message)

'''
USER : I'd like to become a professional dancer
BOT : I'm sorry - I'm not sure how to help you
USER : well then I'd like to order some coffee
BOT : ok, Colombian or Kenyan?
USER : my favourite animal is a zebra
BOT : I'm sorry - would you like Colombian or Kenyan?
USER : kenyan
BOT : perfect, the beans are on their way!
'''
