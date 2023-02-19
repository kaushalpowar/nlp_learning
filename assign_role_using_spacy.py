'''
Assigning roles using spaCy's parser
In this exercise you'll use spaCy's powerful syntax parser to assign roles
to the entities in your users' messages. To do this, you'll define two
functions, find_parent_item() and assign_colors(). In doing so, you'll use
a parse tree to assign roles, similar to how Alan did in the video.

Recall that you can access the ancestors of a word using its .ancestors
attribute.

'''

# Create the document
doc = nlp("let's see that jacket in red and some blue jeans")

# Iterate over parents in parse tree until an item entity is found
def find_parent_item(word):
    # Iterate over the word's ancestors
    for parent in word.ancestors:
        # Check for an "item" entity
        if entity_type(parent) == "item":
            return parent.text
    return None

# For all color entities, find their parent item
def assign_colors(doc):
    # Iterate over the document
    for word in doc:
        # Check for "color" entities
        if entity_type(word) == "color":
            # Find the parent
            item =  find_parent_item(word)
            print("item: {0} has color : {1}".format(item, word))

# Assign the colors
assign_colors(doc)

#OUTPUT
'''

item: jacket has color : red
item: jeans has color : blue
'''
