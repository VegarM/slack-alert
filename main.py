import os
import time
import sys
from slackclient import SlackClient

AUDIO_FILE = os.path.join(
    'audio', 'Tri-Tachyon_-_04_-_Hundred_Years_in_Helheim.mp3')
ALERT_CHANNEL = 'CAYH1GKM4'
#ALERT_CHANNEL = 'D9H0NM0A1'

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)


def handle_msg(msg):
    print(msg)
    if (msg['type'] == 'message' and msg['channel'] == ALERT_CHANNEL and
            'firing' in str(msg).lower()):
        os.system('mpv --loop-file {}'.format(AUDIO_FILE))


def main():
    while True:
        try:
            if sc.rtm_connect():
                while sc.server.connected:
                    for msg in sc.rtm_read():
                        handle_msg(msg)
                    time.sleep(1)
            else:
                print("connection failed")
        except KeyboardInterrupt:
            print("\nctrl+c was pressed, quitting")
            sys.exit(0)
        except Exception as e:
            print(e)
            print("unexpectet error happened ^")
            pass


if __name__ == '__main__':
    main()
