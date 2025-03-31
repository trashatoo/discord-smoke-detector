import random
import requests
import time

WEBHOOK_URL = "put your webhook url here from the discord integrations tab in the server settings"

def send_webhook_message(message):
    data = {"content": message}
    requests.post(WEBHOOK_URL, json=data)

def main():
    beep_count = 0  # Start a count for beeps
    print("beep'd 0 times press ctrl c to exit")
    while True:
        if random.randint(1, 100) == 1:
            beep_count += 1  # Increment beep count
            send_webhook_message("Beep")
            print(f"beep'd {beep_count} times")  # Display the beep count
        time.sleep(5)  # Wait 5 second before checking again

if __name__ == "__main__":
    main()
