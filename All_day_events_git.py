import csv


with open("List_of_events.csv", "r") as f:  
    rows = f.readlines()

#delete header
rows.pop(0)


for i in rows:
    #split data
    data = i.split(";")

    name = data[0]
    surname = data[1]
    event_type = data[2]
    date = data[3]

    data_separately = date.split(".")

    day = data_separately[0]
    next_day = int(day) + 1
    month = data_separately[1]
    year = data_separately[2]

    start_date = "2022"+month+day
    end_day = "2022"+month+str(next_day)

    name_of_person = name + " " + surname + " - " + event_type
    description_of_person = name + " " + surname + " - " + event_type + " - " + date

    #adding text to file
    text_of_file = "\
BEGIN:VCALENDAR\n\
VERSION:2.0\n\
PRODID:-//Apple Inc.//macOS 12.2.1//EN\n\
CALSCALE:GREGORIAN\n\
BEGIN:VEVENT\n\
TRANSP:TRANSPARENT\n\
DTEND;VALUE=DATE:"+end_day+"\n\
DTSTART;VALUE=DATE:"+start_date+"\n\
UID:2F378A4A-0EBB-4106-82E5-AF38020CA110\n\
DTSTAMP:20220323T164128Z\n\
DESCRIPTION:" + description_of_person + "\n\
SEQUENCE:1\n\
X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC\n\
SUMMARY:" + name_of_person + "\n\
LAST-MODIFIED:20220323T164123Z\n\
CREATED:20220323T163945Z\n\
RRULE:FREQ=YEARLY;INTERVAL=1\n\
BEGIN:VALARM\n\
X-WR-ALARMUID:C03A726D-6B68-4D44-8389-0082DCA3E36B\n\
UID:C03A726D-6B68-4D44-8389-0082DCA3E36B\n\
TRIGGER;VALUE=DATE-TIME:19760401T005545Z\n\
ACTION:NONE\n\
END:VALARM\n\
BEGIN:VALARM\n\
X-WR-ALARMUID:1F4249D7-FFDB-4185-9724-0798F24DD1B2\n\
UID:1F4249D7-FFDB-4185-9724-0798F24DD1B2\n\
TRIGGER:PT9H\n\
ATTACH;VALUE=URI:Chord\n\
ACTION:AUDIO\n\
END:VALARM\n\
END:VEVENT\n\
END:VCALENDAR\
"

    file_name = name + "_" + surname + "_" + event_type
    #otwarcie pliku ics
    f = open('./Output/'+file_name+'.ics', 'w')
    f.write(text_of_file)
    f.close()

