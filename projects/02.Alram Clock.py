from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time in the given format HH:MM:SS with the alarm period of am/pm\n")

alarm_hour = alarm_time[0:2]
# print(alarm_hour)
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

print('Setting up the alarm')
while True:
    now = datetime.now()
    current_hour = now.strftime('%H')
    current_minute = now.strftime('%M')
    current_second = now.strftime('%S')
    current_period = now.strftime('%p')
    if(alarm_period == current_period):
        if(alarm_hour == current_hour):
            if(alarm_minute == current_minute):
                if(alarm_second == alarm_second):
                    print('Wake up!')
                    playsound('02.Audio.mp3')
                    break

    # print(current_hour)
