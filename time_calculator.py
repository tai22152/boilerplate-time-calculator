def add_time(start, duration, day=""):

    week_arr = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"];

    time_arr = start.split(":");
    hour_res = int(time_arr[0]);
    minutes_res = int(time_arr[1].split(" ")[0]);
    zone_res = time_arr[1].split(" ")[1];

    h_duration = int(duration.split(":")[0]);
    m_duration = int(duration.split(":")[1]);

    m_remaining = m_duration + minutes_res;
    h_remaining = 0;

    new_time_minutes = 0;
    new_time_hour = 0;
    new_time_zone = "";
    new_time_days = 0;


    if ((m_remaining // 60) > 0):
        h_remaining += 1;
        new_time_minutes = m_remaining % 60;
    else:
        new_time_minutes = m_remaining;

    if (zone_res == "PM"):
        h_remaining += 12 + hour_res + h_duration;
    else:
        h_remaining += hour_res + h_duration;

    new_time_days = h_remaining // 24;

    if ((h_remaining % 24) >= 12):
        new_time_hour = (h_remaining % 24) - 12;
        new_time_zone = "PM";
    else:
        new_time_hour = (h_remaining % 24);
        new_time_zone = "AM";
    if(new_time_hour==0):
        new_time_hour=12;
    if(new_time_minutes<10):
        new_time_minutes="0"+str(new_time_minutes);
    
    

    minutes_res = m_remaining % 60;


    new_time = "";
    if (day == ""):
        if(new_time_days <= 1):
            if (new_time_days == 0):
                new_time = f"{new_time_hour}:{new_time_minutes} {new_time_zone}"
            else:
                new_time = f"{new_time_hour}:{new_time_minutes} {new_time_zone} (next day)"
        else:
            new_time = f"{new_time_hour}:{new_time_minutes} {new_time_zone} ({new_time_days} days later)";
    else:
        index = week_arr.index(day.upper());
        if ((index+new_time_days)%7 == 0):
            day_to_show = week_arr[0].capitalize();
        else:
            day_to_show = week_arr[(index+new_time_days)%7].capitalize();
        if(new_time_days <= 1):
            if (new_time_days == 0):
                new_time = f"{new_time_hour}:{new_time_minutes} {new_time_zone}, {day_to_show}"
            else:
                new_time = f"{new_time_hour}:{new_time_minutes} {new_time_zone}, {day_to_show} (next day)"
        else:
            new_time = f"{new_time_hour}:{new_time_minutes} {new_time_zone}, {day_to_show} ({new_time_days} days later)";

    return new_time

print(add_time("8:16 PM","466:02", "tuesday"));