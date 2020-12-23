#DateTime 
#Working with dates, times, deltas and formats

#Imports
from datetime import datetime, timedelta
from time import strftime

def main():
    #Now 
    #If the host machine is in the UTC timezone then there will be no difference
    now = datetime.now()
    utc = datetime.utcnow()     
    print(f'Now: {now}')
    print(f'UTC: {utc}')
    print(f'Offset: {now.utcoffset}')

    #Time
    print(f'Hour: {now.hour}')
    print(f'Minute: {now.minute}')
    print(f'Second: {now.second}')
    print(f'Micro: {now.microsecond}')

    #Date
    print(f'Year: {now.year}')
    print(f'Month: {now.month}')
    print(f'Day: {now.day}')

    #Timedelta
    print(f'Next month: {now + timedelta(days=30)}') 

    #ISO Strings
    d = datetime.fromisoformat('2020-12-16')
    print(d)

    try:
        m = datetime.fromisoformat('20:26-06:00')
    except Exception as ex: 
        print(ex.args)

    print(f'ISO: {now.isoformat()}')

    #Formatting
    # http://www.w3schools.com/python/python_date_time.asp
    print(now.strftime('%y')) 
    print(now.strftime('%Y')) 
    print(now.strftime('%d')) 
    print(now.strftime('%D')) 
    print(now.strftime('%b')) 

    print(now.strftime('Today is %B, %d'))






if __name__ == "__main__":
    main()