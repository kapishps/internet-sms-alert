import os, platform, subprocess, time
from twilio.rest import TwilioRestClient
from secrets import Twilio_Secrets
#Comment the line below if not using Proxy else edit proxy.py file too
import proxy


def send_sms():
    twilio_secrets = Twilio_Secrets()
    ACCOUNT_SID = twilio_secrets.account_sid
    AUTH_TOKEN = twilio_secrets.auth_token
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to="+918417861995",
        from_="+15204339038",
        body="Hi, The Internet is working once again. Enjoy :)",
    )
    return


def display_notification(title, message):
    subprocess.Popen(['notify-send', title, message])
    return


def ping(host):
    ping_str = "-n 5" if  platform.system().lower()=="windows" else "-c 5"
    return os.system("ping " + ping_str + " " + host) == 0


display_notification("App Activated", "You will get the notification "
                                      "and sms once the Internet starts working")
while not ping("10.1.1.18"):	#you can change this to any url, 10.1.1.18 in my case is the address of my proxy server
    time.sleep(300)

display_notification("Internet is Working Once Again", "Enjoy !!")
send_sms()
