import time
import datetime

def countdown_timer(time_in_seconds):
    """Countdown the timer in the terminal."""
    end_time = datetime.datetime.now() + datetime.timedelta(seconds=time_in_seconds)
    while end_time >= datetime.datetime.now():
        time_left = end_time - datetime.datetime.now()
        print(f"Time left: {time_left}", end='\r')
        time.sleep(1)
    print("Time's up!")

time_in_seconds = int(input("Enter the duration of the timer (in seconds): "))

countdown_timer(time_in_seconds)
