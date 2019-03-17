import os
import json
from bs4 import BeautifulSoup

def html_to_json(content):
    soup = BeautifulSoup(content, 'html')
    rows = soup.find_all('tr')
    
    headers = {}
    thead = soup.find('thead')
    if thead:
        thead = thead.find_all('th')
        for i in range(len(thead)):
            headers[i] = thead[i].text.strip().lower()
    headers[0] = 'Select'
    headers[1] = 'CRN'
    headers[2] = 'Subj'
    headers[3] = 'Crse'
    headers[4] = 'Sec'
    headers[5] = 'Cmp'
    headers[6] = 'Cred'
    headers[7] = 'Title'
    headers[8] = 'Days'
    headers[9] = 'Time'
    headers[10] = 'Cap'
    headers[11] = 'Act'
    headers[12] = 'Rem'
    headers[13] = 'WL Cap'
    headers[14] = 'WL Act'
    headers[15] = 'WL Rem'
    headers[16] = 'XL Cap'
    headers[17] = 'XL Act'
    headers[18] = 'XL Rem'
    headers[19] = 'Instructor'
    headers[20] = 'Date'
    headers[21] = 'Location'
    headers[22] = 'Attribute'
    data = []
    for row in rows:
        cells = row.find_all('td')
        items = {}
        for index in headers:
            if(index < len(cells)):
                items[headers[index]] = cells[index].text
        data.append(items)
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    files = os.listdir('./SIS Data')
    for page in files:
        with open('SIS Data/' + page, 'r') as f:
            content = f.read()
        with open('SIS Data/' + page.replace('html', 'json'), 'w') as r:
            r.write(html_to_json(content))
