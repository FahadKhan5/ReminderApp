import time
from plyer import notification

def hourly_reminder():
    while True:
        time.sleep(10) #this time is in seconds show notification after 1 minute

        notification_title = "Reminder"
        notification_message = "One minute has passed"

        notification.notify (
            title = notification_title,
            message = notification_message,
            app_name = "The Reminder App",
            timeout = 5 #notification will be shown for 5 sec only
        )

if __name__ == "__main__":
    print("App has been started")
    print("ctrl + c to stop")
    try:
        hourly_reminder()
    except KeyboardInterrupt: #press ctrl+c to stop the terminal
        print("The app has been stoped")
