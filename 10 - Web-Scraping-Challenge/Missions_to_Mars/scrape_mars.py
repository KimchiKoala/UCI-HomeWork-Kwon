# Import dependencies
import os
import requests
import time
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager


# Find the path and execute chromedriver
def init_browser():
    # Initiate chromdriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

# Create an empty dictionary to store data we will retrieve
mars_data = {}

# Scrape Mars News
def scrape_mars_news():
    # Initiate Browser, visit the url and scrape
    browser = init_browser()
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    time.sleep(3)

    # Create a Beautiful Soup object
    html = browser.html
    soup = bs(html, 'html.parser')  

    # Extract info on title and paragraph using BS
    news_title = soup.find_all('div', class_='content_title')[1].text
    news_p = soup.find('div', class_='article_teaser_body').text

    # Add to dictionary
    mars_data['Title'] = news_title
    mars_data['Paragraph'] = news_p

    browser.quit()

    return mars_data

# Scrape Mars Images
def scrape_mars_image():

    # Initiate Browser, visit the url and scrape
    browser = init_browser()
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)

    # Create a Beautiful Soup object
    html = browser.html
    soup = bs(html, 'html.parser')

    # find necessary elements
    full_image = soup.find('div', class_='carousel_container')

    # Retrieve the anchor with the href needed
    picture = full_image.a['data-fancybox-href']

    # Base url to attach href to
    base_url="https://www.jpl.nasa.gov/"

    # Concatenate
    featured_image_url = base_url + picture

    featured_image_url

    mars_data['Image_URL'] = featured_image_url

    browser.quit()

    return mars_data

# Scrape Mars Facts
def scrape_mars_facts():
    # Initiate Browser, visit the url and scrape
    browser = init_browser()
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)

    # retrieve fact table using pd
    mars = pd.read_html(facts_url)
    mars_facts = mars[0]
    
    # change headers
    mars_facts.columns=['Category', 'Facts']

    # read to check
    mars_facts

    # convert to html table string
    mars_facts_html = mars_facts.to_html(header=False)
    mars_facts_html

    mars_data['Table'] = mars_facts_html

    browser.quit()

    return mars_data

# Scrape Mars Hemispheres
def scrape_mars_hems():
    # Initiate Browser, visit the url and scrape
    browser = init_browser()
    hems_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hems_url)

    # Create html object and parse with bs
    html = browser.html
    soup = bs(html, 'html.parser')

    # Retrieve all elements needed
    all_hems = soup.find_all('div', class_='item')

    # create an empty list to store data
    hem_img_urls = []

    # Create a base/main url to use in loop
    base_url = 'https://astrogeology.usgs.gov'

     # Iterate through the elements retrieved
    for hem in all_hems:
        
        # Store the title
        title = hem.find('h3').text
        # Get the link that has the full-res image
        img_url = hem.find('a', class_='itemLink')['href']
        # Visit that link
        browser.visit(base_url + img_url)

        # Create an html object of the site that has individual hemisphere data
        each_hem_html = browser.html
        # Parse html using bs
        soup = bs(each_hem_html, 'html.parser')

        # Retrieve the full-res image source
        hd_img_url = base_url + soup.find('img', class_='wide-image')['src']
        # Append the titles and high-res image links as a dict to the empty list
        hem_img_urls.append({'title': title, 'image_url': hd_img_url})

        
        
    mars_data['Hemisphere_URLs'] = hem_img_urls
        
    browser.quit()

    return mars_data