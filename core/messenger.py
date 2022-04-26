import time
from fbchat import Client as MessengerClient
from fbchat.models import ThreadType, Message

from core.models import MessengerBelayer

# client = MessengerClient('daniel.rodas.bautista@gmail.com', 'password')
# thread_id = 630504458
# thread_type = ThreadType.USER
# message_id = client.send(Message(text="Hello I'm a bot"), thread_id=thread_id, thread_type=thread_type)

"""
User(
uid='630504458', 
type=ThreadType.USER, 
photo='https://scontent-atl3-2.xx.fbcdn.net/v/t39.30808-1/272765516_10160213631044459_6876269269143858076_n.jpg?stp=c592.294.1111.1111a_cp0_dst-jpg_s32x32&_nc_cat=106&ccb=1-5&_nc_sid=0081f9&_nc_ohc=mi6pWbVg6KEAX9wqlOG&_nc_oc=AQnTefFsUF2aZq7naAIol2C_lZ3yFImO4k4tJzvfVWptaiJzfWJSn8efAOKYd6Im5Q0&_nc_ht=scontent-atl3-2.xx&oh=00_AT_APi5bL1YQyyOxFQL750tHEoXVjqHXQtNnSJglCmLuHQ&oe=626B4F4B', 
name='Louis-thomas Schreiber', 
last_message_timestamp=None, 
message_count=None, 
plan=None, 
url='https://www.facebook.com/louisthomas.schreiber', 
first_name='Louis-thomas', 
last_name=None, 
is_friend=True, 
gender='male_singular', 
affinity=None, 
nickname=None, 
own_nickname=None, 
color=None, 
emoji=None)
"""


class Messenger:

    def __init__(self, user, session):
        self.contacts = []
        self.user = user
        self.client = MessengerClient(email=user.email, password='badpassword', session_cookies=session)

    def get_contacts(self):
        messenger_users = self.client.fetchAllUsers()

        for messenger_user in messenger_users:
            messenger_user.is_belayer = False
            messenger_user_belayer = MessengerBelayer.objects.filter(
                messenger_id=messenger_user.uid,
                user=self.user).first()
            if messenger_user_belayer:
                messenger_user.is_belayer = True
                messenger_user.id = messenger_user_belayer.id

        self.contacts = messenger_users
        return self.contacts

    def send_message(self, message):
        contacts = MessengerBelayer.objects.filter(user=self.user)
        for contact in contacts:
            print(f'sending it: "{message}" to "{contact.name}"')
            self.client.send(Message(text=message), thread_id=contact.messenger_id, thread_type=ThreadType.USER)
            time.sleep(2)


