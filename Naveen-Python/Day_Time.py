import datetime
import pytz

Day_Time=datetime.datetime(2019, 6,24,12,35,42, tzinfo=pytz.UTC)
print(Day_Time)

Dt_Now=datetime.datetime.now(tz=pytz.UTC)
print(Dt_Now)

Dt_UTCnow=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(Dt_UTCnow)

#prefer datetime.now becaue easy to write

Dt_NowUtc=datetime.datetime.now(tz=pytz.UTC)
print(Dt_NowUtc)

Dt_Mntn=Dt_NowUtc.astimezone(pytz.timezone('Canada/Yukon'))
print(Dt_Mntn)

for tz in pytz.all_timezones:
    print(tz)#prints all timezones

Now_Dt=datetime.datetime.now()
print(Now_Dt)


Now_Dt=datetime.datetime.now()
Dt_Mntn=pytz.timezone('US/Mountain')
Now_Dt=Dt_Mntn.localize(Now_Dt)
print(Now_Dt)


Date=datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(Date.strftime("%B %d,%Y"))

#convert string into datetime

Date="March 05,2020"
Conv_Dt=datetime.datetime.strptime(Date, "%B %d,%Y")
print(Conv_Dt)

