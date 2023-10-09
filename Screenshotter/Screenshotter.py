## Automatic XML sitemap screenshotter
## By Stach Redeker & ChatGPT
## 2023 - MIT licence

# dependencies
import os
import requests
import shutil
from bs4 import BeautifulSoup
from screenshotone import Client, TakeOptions

# we use BeautifulSoup to extract URLs from a sitemap XML
def get_urls_from_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, 'xml')
    urls = [loc.text for loc in soup.find_all('loc')] # all URLs in an XML file (at least in WordPress) are between <loc></loc>
    return urls

# we use the ScreenshotOne API to deal with all the screenshot stuff
def take_screenshot(url, save_path, client):
    options = (TakeOptions.url(url)
               .format("png")
               .full_page(True) 
               .viewport_width(1920) 
               .block_cookie_banners(True)  
               .block_chats(True)) 

    image = client.take(options)

    with open(save_path, 'wb') as result_file:
        shutil.copyfileobj(image, result_file)
    print(f'Screenshot saved to {save_path}')

# save the screenshots to the correct folder
def save_screenshots(urls, save_folder, client):
    if not os.path.exists(save_folder): # if the output folder does not exist yet, create it
        os.makedirs(save_folder)
    
    # loop through all URLs in the sitemap and take a screenshot
    for url in urls:
        screenshot_path = os.path.join(save_folder, f"{url.replace('http://', '').replace('https://', '').replace('/', '_')}.png")
        take_screenshot(url, screenshot_path, client)

if __name__ == "__main__":

    # intoductionairy TUI
    print(f'------------------------------------')
    print(f'Automatic XML sitemap screenshotter')
    print(f'By Stach Redeker & ChatGPT')
    print(f'2023 - MIT licence')
    print(f'------------------------------------')

    # fetch sitemap URL and user credentials
    sitemap_url = input("Enter your sitemap URL. Sitemaps that consists of other sitemaps (such as /wp-sitemap.xml) are not supported: ")
    access_key = input("Enter your ScreenshotOne access key: ")
    secret_key = input("Enter your ScreenshotOne secret key: ")

   # allow users to change the default storage location
    print(f'The default storage location is ~/Desktop/Screenshots. Change? y/n')
    change_location = input().strip().lower()
    if change_location == 'y':
        save_folder = input("Enter the new storage location (path): ").strip()
    else:
        save_folder = os.path.join(os.path.expanduser('~'), 'Desktop', 'Screenshots')


    # fetch URLs from sitemap
    urls = get_urls_from_sitemap(sitemap_url)

    # start a ScreenshotOne API client
    client = Client(access_key, secret_key)
    
    # make screenshots and store to disk
    save_screenshots(urls, save_folder, client)

