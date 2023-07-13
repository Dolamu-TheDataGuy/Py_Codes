from twilio.rest import Client
import cred

TWILIO_SID = cred.TWILIO_SID
TWILIO_AUTH_TOKEN = cred.TWILIO_AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER = cred.TWILIO_VIRTUAL_NUMBER
TWILIO_VERIFIED_NUMBER = cred.TWILIO_VERIFIED_NUMBER

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_notification(self, message):
        message = self.client.message.create(
            body = message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        #print if successfully sent
        print(message.sid)
    