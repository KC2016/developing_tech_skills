# ELIZA I: asking questions
# Asking questions is a great way to create an engaging conversation. Here, you'll create the very first hint of ELIZA's famous personality, by responding to statements with a question and responding to questions with answers.

# A dictionary of responses with "question" and "statement" as keys and lists of appropriate responses as values has already been defined for you. Explore this in the Shell with responses.keys() and responses["question"].

# Instructions
# Define a respond() function which takes in message as an argument, and uses the string's .endswith() method to check if a message ends with a question mark.
# If the message does end with a question mark, choose a random "question" from the responses dictionary. Else, choose a random "statement" from the responses.
# Send the bot multiple messages with and without a question mark - these have been provided for you. If you want to experiment further in the Shell, be sure to first hit 'Run Code'.


import random
import time
import re

# # ' ' 'This bot responds based on whether user asked a question or made a statement ' ' '

# create a template
bot_template = "BOT : {0}"
user_template = "USER : {0}"

responses = {"question": ["you tell me!", "I don't know :("], 
             "statement": [":)", "oh wow!", "I find that extremely interesting", "why do you think that?"]}

# Write a function called respond() with a single parameter message which returns the bot's response. To do this, concatenate the strings "I can hear you! You said: " and message.
# Store the concatenated strings in bot_message, and return this result.



# create a fucntion to answer questions or make an statement
def respond(message):
    if message.endswith("?"):
        return random.choice(responses["question"])
    else:
        return random.choice(responses["statement"])


def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    # create an artifitial delay
    time.sleep(1.0)
    print(bot_template.format(response))



send_message("what's today's weather?")
time.sleep(1.0)
send_message("Do you need something?")
time.sleep(1.0)
send_message("I love building chatbots")
time.sleep(1.0)
send_message("I like Python!")

# ELIZA II: Extracting key phrases
# The really clever thing about ELIZA is the way the program appears to understand what you told it by occasionally including phrases uttered by the user in its responses.

# In this exercise, you will match messages against some common patterns and extract phrases using re.search(). A dictionary called rules has already been defined, which matches the following patterns:

# "do you think (.*)"
# "do you remember (.*)"
# "I want (.*)"
# "if (.*)"
# Inspect this dictionary in the Shell before starting the exercise.

# Instructions
# Iterate over the rules dictionary using its .items() method, with pattern and responses as your iterator variables.
# Use re.search() with the pattern and message to create a match object.
# If there is a match, use random.choice() to pick a response.
# If '{0}' is in that response, use the match object's .group() method with index 1 to retrieve a phrase.

rules = {'do you think (.*)': ['if {0}? Absolutely.', 'No chance'], 
         'do you remember (.*)': ['Did you think I would forget {0}', 
         "Why haven't you been able to forget {0}", 'What about {0}', 
         'Yes .. and?'], 
         'I want (.*)': ['What would it mean if you got {0}', 
         'Why do you want {0}', 
         "What's stopping you from getting {0}"], 
         'if (.*)': ["Do you really think it's likely that {0}", 
         'Do you wish that {0}', 'What do you think about {0}', 'Really--if {0}']}

# print(rules)

# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None
    
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase     # it was return response.format(phrase), 
    # I changed https://code.sololearn.com/chAYGq7gEQrS/?ref=app#py and https://www.sololearn.com/Discuss/2133553/python-help

# Test match_rule
print(match_rule(rules, "do you remember your last birthday"))

# ELIZA III: Pronouns
# To make responses grammatically coherent, you'll want to transform the extracted phrases from first 
# to second person and vice versa. 
# In English, conjugating verbs is easy, and simply swapping "me" and 'you', "my" and "your" works in most cases.

# In this exercise, you'll define a function called replace_pronouns() which uses re.sub() 
# to map "me" and "my" to "you" and "your" (and vice versa) in a string.

# Instructions
# If 'me' is in message, use re.sub() to replace it with 'you'.
# If 'my' is in message, replace it with 'your'.
# If 'your' is in message, replace it with 'my'.
# If 'you' is in message, replace it with 'me'.

# Define replace_pronouns()
def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my','your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you', 'me', message)

    return message

# ELIZA IV: Putting it all together
# Now you're going to put everything from the previous exercises together and experience the magic! The match_rule(), send_message(), and replace_pronouns() functions have already been defined, and the rules dictionary is available in your workspace.

# Your job here is to write a function called respond() with a single argument message which creates an appropriate response to be handled by send_message().

# Instructions
# Get a response and phrase by calling match_rule() with the rules dictionary and message.
# Check if the response is a template by seeing if it includes the string '{0}'. If it does:
# Use the replace_pronouns() function on phrase.
# Include the phrase by using .format() on response and overriding the value of response.
# Hit 'Submit Answer' to see how the bot responds to the provided messages!

# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

# Send the messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")