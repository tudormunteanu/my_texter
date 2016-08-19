from twilio.rest import TwilioRestClient
import datetime
import random
import time
from key import account_sid, auth_token, twilio_number

#Instantiate class TwilioRestClient with your credentials
client = TwilioRestClient(account_sid, auth_token)

#set current date and time into variable
d = datetime.datetime.now() 

#List that holds the messages that are texted
text = ['Hello. This is your reminder to drink water. Thank you.',
		'Bernardo wants to know if you\'re drinking water. Hugs!',
		'*computer voice* Drink water please!',
		'May I recommend this site: http://greatist.com/health/health-benefits-water',
		'I\'m thirsty. Are you thirsty? Let\'s go grab a water!',
		'It\'s Water O\'Clock somewhere, am I right?',
		'Hey kid, wanna try some water? All the cool kids are drinking it.',
		'Gimme a H. Gimme a 2. Gimme an O. What\'s that spell? Water!',
		'Don\'t you love letting out a big \'Aaaahhh\' after a nice gulp of water?',
		'Kick back, put your feet up, grab a drink of water and enjoy this https://www.youtube.com/watch?v=oHg5SJYRHA0',
		'Waiter, what\'s the water de jour? It\'s the water of the day. Thank you, I\'ll have that.',
		'Listen...Do you hear that? It\'s the sound of you not drinking water.',
		'I heard the watercooler just got a fresh keg, let\'s go!',
		'I know you want a cocktail right now, but a drink of water is more important.',
		'I love the taste of water. Especially frozen into cubes and completely surrounded by vodka.',
		'Tell Janice from Accounting to relax. She\'ll get her numbers after your drink of water',
		'Dihydrogen monoxide is a colorless and odorless chemical compound that the government is purposely telling its citizens to ingest. We must stop this abuse!']

contacts = {
			}
			
def send_text():
    if d.isoweekday() in range(1, 6): #checks for Monday - Friday
    	if d.hour in range(10, 18): #checks for 10am - 5pm
    		for name, number in contacts.items(): #create tuple from contacts dictionary
    			message = client.messages.create( 
    	    		body=random.choice(text), #randomly select a message from the text list
    	    		to=number,   #loop through tuple phone numbers
    	    		from_= twilio_number) # Replace with your Twilio number
    			time.sleep(2)
    			print message.sid
    	else:
    		print 'Not in time range'
    else:
    	print 'Not weekday'
