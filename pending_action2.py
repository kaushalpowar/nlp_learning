'''
Pending actions II

Having defined your policy() function, it's now time to write a send_message()
function which takes both a pending action and a message as its arguments and
leverages the policy() function to determine the bot's response.

Your policy(intent) function from the previous exercise has been pre-loaded.
'''
# Define send_message()
def send_message(pending, message):
    print("USER : {}".format(message))
    action, pending_action = policy(interpret(message))
    if action == "do_pending" and pending is not None:
        print("BOT : {}".format(pending))
    else:
        print("BOT : {}".format(action))
    return pending_action
    
# Define send_messages()
def send_messages(messages):
    pending = None
    for msg in messages:
        pending = send_message(pending, msg)

# Send the messages
send_messages([
    "I'd like to order some coffee",
    "ok yes please"
])

'''
USER : I'd like to order some coffee
BOT : Unfortunately, the Kenyan coffee is currently out of stock, would you like to order the Brazilian beans?
USER : ok yes please
BOT : Alright, I've ordered that for you!
'''
