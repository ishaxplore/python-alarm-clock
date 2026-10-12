import time

alarm_time = input("Enter alarm time (HH:MM:SS): ")

while True:
    current_time = time.strftime("%H:%M:%S")
    print(current_time, end="\r")

    if current_time == alarm_time:
        print("\nWake Up! Alarm Ringing...")
        break

    time.sleep(1)