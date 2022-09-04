# **NBA Player Database Webscraper**

## **INFO:**
* ### Scrapes from a [NBA Player database](https://www.basketball-reference.com/players) website
* ### Webscraping using beautiful soup
* ### Exports in JSON, CSV and SQL
* ### Fetches content over multiple pages
* ### Uses multiple optimizations to reduce runtime and 
* ### Reduced bandwidth resources
* ### Makes use of only one connection with the server per scrape

## **MODULES:**

* ### Requests
* ### Beautifulsoap
* ### lxml

## **BRIEF:**

### This web scraper uses bs4 along side with lxml (which is faster by 5x than the default html.parser), also makes uses a connection session (`requests.session()`) to prevent multiple connections and do multiple `GET` requests through that connection. This webscraper also exports in multiple file formats such as CSV, SQL, JSON allowing for a flexible usecases for the script


### This was made as a proof of skill in the libraries mentioned, the code is meant to be light weight and efficient while showcasing its flexibilty in export. A portfolio project on webscraping using BeautifulSoup for Upwork

## **By yours truely,**
## ***-Amogha.Y.A***