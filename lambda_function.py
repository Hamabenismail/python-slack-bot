
import slack
import schedule
import os
from pathlib import Path
from dotenv import load_dotenv
import time

def main() :
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path = env_path)


    client = slack.WebClient(token= os.environ['SLACK_TOKEN'])

    client.chat_postMessage(channel="#test", text="hello people")

schedule.every(10).seconds.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
