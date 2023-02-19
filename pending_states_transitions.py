'''
Pending state transitions

You'll often need to briefly deviate from the flow of a conversation, for
example to authenticate a user, before returning to the topic of discussion.

In these cases, it's often simpler - and easier to debug - if you save some
actions/states as pending rather than adding ever more complicated rules.

Here, you're going to define a policy_rules dictionary, where the keys are
tuples of the current state and the received intent, and the values are tuples
of the next state, the bot's response, and a state for which to set a pending
transition.
'''
# Define the states
INIT=0
AUTHED=1
CHOOSE_COFFEE=2
ORDERED=3

# Define the policy rules
policy_rules = {
    (INIT, "order"): (INIT, "you'll have to log in first, what's your phone number?", AUTHED),
    (INIT, "number"): (AUTHED, "perfect, welcome back!", None),
    (AUTHED, "order"): (CHOOSE_COFFEE, "would you like Colombian or Kenyan?", None),    
    (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "perfect, the beans are on their way!", None)
}

# Define send_messages()
def send_messages(messages):
    state = INIT
    pending = None
    for msg in messages:
        state, pending = send_message(state, pending, msg)

# Send the messages
send_messages([
    "I'd like to order some coffee",
    "555-1234",
    "kenyan"
])

'''
USER : I'd like to order some coffee
BOT : you'll have to log in first, what's your phone number?
USER : 555-1234
BOT : perfect, welcome back!
BOT : would you like Colombian or Kenyan?
USER : kenyan
BOT : perfect, the beans are on their way!
BOT : would you like Colombian or Kenyan?
'''
