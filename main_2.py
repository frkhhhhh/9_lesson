import requests
import threading
import time
from bs4 import BeautifulSoup

start = time.perf_counter()
tables=[
    
'http://www.example.com/timetable',
'http://www.example.com/schedule',
'http://www.example.com/events/timetable',
'http://www.example.com/calendar',
'http://www.example.com/classes/schedule'


]


def table(tabel):
    try:
        tr= requests.get(tabel)
        soup = BeautifulSoup(tr.content, 'html.parser') 
        text_content = soup.get_text()  
        file_name = f"{tabel.split('/')[-1]}.csv"
        with open(file_name, "w", encoding="utf-8") as text_file:
            text_file.write(text_content)
            print(f"{file_name} downloaded")
    except Exception as e:
        print(f"Error {table}: {e}")

threads = []
tables
for tabel in tables:
    thread = threading.Thread(target=table, args=[tabel])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f"{end - start} seconds elapsed")