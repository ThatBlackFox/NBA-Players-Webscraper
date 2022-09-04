import requests
import sqlite3
import os
import json
import csv
from bs4 import BeautifulSoup

try:
    os.remove('temp.db')
    os.remove('temp.json')
except:
    pass

csv_file = open('temp.csv', 'w', encoding='utf-8')
fieldnames = ['url', 'name', 'start_year', 'end_year', 'position', 'height', 'weight', 'dob', 'college']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()

#using this without a context manager because I dont wish to open and close multiple times during the loop

conn = sqlite3.connect('temp.db')
cor = conn.cursor()

temp_dict = {}

def main():
    base_url = 'https://www.basketball-reference.com/'
    ses = requests.Session()

    #preparing to collect names and respective profile urls
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sub_url = 'players/'

    #itering over the letter to scrap the indices
    for i in letters:
        table = f""" CREATE TABLE {i} (
            url CHAR(255),
            name CHAR(255),
            start_year INT,
            end_year INT,
            pos char(10),
            height CHAR(10),
            weight CHAR(10),
            dob CHAR(25),
            college CHAR(40)
        ); """
 
        cor.execute(table)
        conn.commit()
        print(f'Collecting data of NBA players with last names starting from {i.capitalize()}')
        temp_dict[i]=[]
        url = base_url+sub_url+i
        resp = ses.get(url=url)
        soup = BeautifulSoup(resp.text, 'lxml')
        players = soup.find_all('th', {'data-append-csv':True})
        for p in players:
            tr = p.parent

            #getting name and url

            for tag in p.children:
                if tag.name=='a':
                    p_url = tag['href']
                    name = tag.text
                elif tag.name == 'strong':
                    tag = tag.a
                    p_url = tag['href']
                    name = tag.text
            start = tr.contents[1].text
            end = tr.contents[2].text
            pos = tr.contents[3].text
            height = tr.contents[4].text
            weight = tr.contents[5].text
            dob = tr.contents[6].text
            college = tr.contents[7].text
            if college == '':
                college = 'None'
            bas_url='https://www.basketball-reference.com'
            cor.execute(f"INSERT INTO {i} (url, name, start_year, end_year, pos, height, weight, dob, college) VALUES (?,?,?,?,?,?,?,?,?)", (bas_url+p_url,name,start,end,pos,height,weight,dob,college))
            conn.commit()
            player_dict= {'url':bas_url+p_url, 'name':name, 'start_year':start, 'end_year':end, 'position':pos, 'height':height, 'weight':weight, 'dob':dob, 'college':college}
            temp_dict[i].append(player_dict)
            writer.writerow(player_dict)

if __name__ == "__main__":
    main()

with open('temp.json', 'w') as f:
    json.dump(temp_dict, f)

csv_file.close()
exit("Thanks for using Amogh's mini webscraper!")