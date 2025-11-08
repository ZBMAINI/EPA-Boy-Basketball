import pandas as pd
from ics import Calendar, Event
from datetime import datetime
import pytz

# 读取CSV文件
df = pd.read_csv('schedule.csv')

calendar = Calendar()
tz = pytz.timezone("America/New_York")

for _, row in df.iterrows():
    event = Event()
    event.name = row['opponent']
    start = tz.localize(datetime.strptime(row['date'], "%Y-%m-%d %H:%M"))
    event.begin = start
    event.location = row.get('location', '')
    event.description = f"Erie Prep Boys Basketball vs {row['opponent']}"
    calendar.events.add(event)

# 输出ICS文件
with open('EriePrep_Boys_Basketball.ics', 'w', encoding='utf-8') as f:
    f.writelines(calendar)

