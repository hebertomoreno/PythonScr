# Domain Knowledge: What does a user expect this bot to understand?
# Personality: What tone or vocabulary does the bot employ?

GREETING_KEYWORDS = ("hello", "hi","greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey","*nods*","hey you get my snap?"]

def check_for_greeting(sentence):
	"""If any of the words in the user's input was a 
	greeting, regurn a greeting response"""
	for word in sentence.words:
		if word.lower() in GREETING_KEYWORDS:
			return random.choice(GREETING_RESPONSES)

check_for_greeting("hello")