import csv
 
def time_data_processing():
    with open('data.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['TimeKey','Hour24','Hour24ShortString','Hour24MinString','Hour2424FullString','Hour12','Hour12ShortString','Hour12MinString','Hour12FullString','AmPmString','MinuteCode','MinuteShortString','MinuteFullString24','MinuteFullString12','HalfHour','HalfHourShortString','HalfHourFullString24','HalfHourFullString12','SecondShortString','FullTimeString24','FullTimeString12','DayTimeBucketGroupKey','DayTimeBucket'])
        for hour in range(0,24,1):
            for min in range(0,60,1):
                for sec in range(0,60,1):
                    TimeKey=hour*1000+min*100+sec
                    Hour24=hour
                    Hour24ShortString=str(hour)
                    Hour24MinString = str(hour)+":00"
                    Hour2424FullString = str(hour)+":00:00"
 
                    Hour12=hour%12
                    Hour12ShortString=str(Hour12)
                    Hour12MinString =  str(Hour12)+":00"
                    Hour12FullString =  str(Hour12)+":00:00"
 
                    AmPmCode=hour/12
                    AmPmString=""
                    if hour<12:
                        AmPmString+="AM"
                    else:
                        AmPmString+="PM"
 
                    Minute = min
                    MinuteCode=hour*100+Minute
                    MinuteShortString=str(min)
                    MinuteFullString24=str(hour)+":"+"0"+str(min)+":00"
                    MinuteFullString12=str(hour%12)+":"+"0"+str(min)+":00"
 
                    HalfHour=min/30
                    HalfHourCode=hour*100+(min/30)*30
                    HalfHourShortString=str((min/30)*30)
                    HalfHourFullString24=str(hour)+":"+"0"+str((min/30)*30)+":00"
                    HalfHourFullString12=str(hour%12)+":"+"0"+str((min/30)*30)+":00"
 
                    Second=sec
                    SecondShortString=str(sec)
                    FullTimeString24=str(hour)+":"+"0"+str(min)+":"+"0"+str(sec)
                    FullTimeString12=str(hour%12)+":"+"0"+str(min)+":"+"0"+str(sec)
 
                    FullTime=str(hour)+":"+"0"+str(min)+":"+"0"+str(sec)
 
                   # print(TimeKey,Hour24,Hour24ShortString,Hour24MinString)
                    #have to write codes to write all the values into csv file here
 
 
                    DayTimeBucketGroupKey = 0
                    if TimeKey >=00000 and TimeKey<=25959:
                        DayTimeBucketGroupKey=0
                    elif TimeKey >=30000  and TimeKey<=65959:
                        DayTimeBucketGroupKey=1
                    elif TimeKey >=70000  and TimeKey<=85959:
                        DayTimeBucketGroupKey=2
                    elif TimeKey >=90000  and TimeKey<=115959:
                        DayTimeBucketGroupKey=3
                    elif TimeKey >=120000  and TimeKey<=135959:
                        DayTimeBucketGroupKey=4
                    elif TimeKey >=140000  and TimeKey<=155959:
                        DayTimeBucketGroupKey=5
                    elif TimeKey >=50000  and TimeKey<=175959:
                        DayTimeBucketGroupKey=6
                    elif TimeKey >=180000  and TimeKey<=235959:
                        DayTimeBucketGroupKey=7
                    else:
                        DayTimeBucketGroupKey=8
 
 
                    DayTimeBucket  = ""
                    if TimeKey >=00000 and TimeKey<=25959:
                        DayTimeBucket+="Late Night (00:00 AM To 02:59 AM)"
                    elif TimeKey >=30000  and TimeKey<=65959:
                        DayTimeBucket+="Early Morning(03:00 AM To 6:59 AM)"
                    elif TimeKey >=70000  and TimeKey<=85959:
                        DayTimeBucket+="AM Peak (7:00 AM To 8:59 AM)"
                    elif TimeKey >=90000  and TimeKey<=115959:
                        DayTimeBucket+="Mid Morning (9:00 AM To 11:59 AM)"
                    elif TimeKey >=120000  and TimeKey<=135959:
                        DayTimeBucket+="Lunch (12:00 PM To 13:59 PM)"
                    elif TimeKey >=140000  and TimeKey<=155959:
                        DayTimeBucket+="Mid Afternoon (14:00 PM To 15:59 PM)"
                    elif TimeKey >=50000  and TimeKey<=175959:
                        DayTimeBucket+="PM Peak (16:00 PM To 17:59 PM)"
                    elif TimeKey >=180000  and TimeKey<=235959:
                        DayTimeBucket+="Evening (18:00 PM To 23:59 PM)"
                    else:
                        DayTimeBucket="Previous Day Late Night _(24:00 PM to 00:00 PM )"
 
                    thewriter.writerow([TimeKey,Hour24,Hour24ShortString,Hour24MinString,Hour2424FullString,Hour12,Hour12ShortString,Hour12MinString,Hour12FullString,AmPmString,MinuteCode,MinuteShortString,MinuteFullString24,MinuteFullString12,HalfHour,HalfHourShortString,HalfHourFullString24,HalfHourFullString12,SecondShortString,FullTimeString24,FullTimeString12,DayTimeBucketGroupKey,DayTimeBucket])
 
 
time_data_processing()
