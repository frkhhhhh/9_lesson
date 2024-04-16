import requests
import time
import threading
from bs4 import BeautifulSoup
start=time.perf_counter()
add=[
    'https://www.bbc.com/news',
    'https://www.nytimes.com/',
    'https://www.theguardian.com/us',
    'https://www.khanacademy.org/',
    'https://www.coursera.org/',
    'https://www.edx.org/'

]

def address_l(address):
    try:
        tr= requests.get(address)
        soup = BeautifulSoup(tr.content, 'html.parser') 
        text_content = soup.get_text() 
        file_name = f"{address.split('/')[-1]}.txt"
        with open(file_name,"w", encoding='UTF-8') as address:
         address.write(text_content)

        print(address)
    except Exception as e:
        print(f'ERROR {address} :{e}')    
    
        print(f"{soup} downloaded" )
threads=[]
for address in add:
    th=threading.Thread(target=address_l, args=[address])
    th.start()
    threads.append(th)

for i in threads:
    i.join()



end=time.perf_counter()

print(f"Finished {end - start} seconds")

