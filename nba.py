import requests
import sqlite3
import os
import json
import csv
from bs4 import BeautifulSoup


class NBA():
    def __init__(self):
        self.session = requests.session()
        self.base_url = 'https://www.basketball-reference.com/'
        self.sub_url = 'players/'
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    def getPlayers(self, i) -> list:

        """
        Scrapes all the data from the website whose last names start from the parameter provided to the function

        :param str i: The first letter of the players' laster
        :return: A list of dictionary of all the players
        :rtype: list
        """
        players=[]
        url = self.base_url+self.sub_url+i
        resp = self.session.get(url=url)
        soup = BeautifulSoup(resp.text, 'lxml')
        players = soup.find_all('th', {'data-append-csv':True})
        for p in players:
            tr = p.parent
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
            bas_url='https://www.basketball-reference.com'
            if college == '':
                college = 'None'
            player_dict= {'url':bas_url+p_url, 'name':name, 'start_year':start, 'end_year':end, 'position':pos, 'height':height, 'weight':weight, 'dob':dob, 'college':college}
            players.append(player_dict)
        return players
    
    def getAll(self) -> dict:
        """
        Scrapes all the data from the website of all the players

        :return: A dictionary of all the players keyed to their first letter of their last name
        :rtype: dict
        """
        players={}
        for i in self.letters:
            players[i]=self.getPlayers(i)
        return players