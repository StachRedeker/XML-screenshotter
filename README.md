# Automatic XML Sitemap Screenshotter
> Automatically generate screenshots from URLs found in an XML sitemap using the ScreenshotOne API in Python. Developed by Stach Redeker & ChatGPT, 2023. Released under the MIT license.

As a WordPress specialist, I like to show my work. This means that I often have to take screenshots of websites. Although browser extensions exist that can capture a single, full-page screenshot, little tooling is available for capturing an entire website. The Automatic XML Sitemap Screenshotter aims to change that. The program is open-source and Python-based. Automatic XML Sitemap Screenshotter uses the ScreenshotOne API to capture images of an entire website, based on an XML sitemap input.

I opted for an implementation using the ScreenshotOne API because making full-page screenshots is not trivial. Nowadays, sites have sticky headers, cookie banners, and other annoying pop-ups, making capturing a proper full-page image very difficult. The ScreenshotOneAPI has inbuilt tooling to combat all these issues. Why bother reinventing the wheel, right?

## Features
The program...
- automatically extracts URLs from a provided XML sitemap;
- generates full-page screenshots with a width of 1920 pixels using the ScreenshotOne API;
- gets rid of cookie banners, floating elements, etc.;
- allows the user to set a folder where the screenshots are saved.

![Results](/Images/result.png)
*Figure 1: the result after running the program: a folder with every page of a website screenshotted.*

## Minimal (system) requirements
- The program is built and tested for Windows operating systems using Python 3.9. It is also tested on Python 3.8.
- The working on other technology stacks cannot be guaranteed. 

### Python dependencies
- `os`
- `requests`
- `shutil`
- `bs4` (Beautiful Soup 4)
- `screenshotone`

## Installation, setup and usage

### Quick installation guide
   
1. **Installing Dependencies**
    ```bash
    pip install requests beautifulsoup4 screenshotone
    ```
   
2. **Creating API Credentials**
    - Sign up for a [ScreenshotOne](https://screenshotone.com/) account and obtain your API `access_key` and `secret_key`. The free plan allows for 100 screenshots each month.
    - Input the API credentials when prompted by the application during runtime.
  
3. **Running the script**
    ```bash
    python Screenshotter.py
    ```

### Beginner-friendly installation guide
   
   1. Download Python 3.9 at the [Python website](https://www.python.org/downloads/release/python-390/).
   2. Download the latest release of XML-screenshotter at [Releases](https://github.com/StachRedeker/XML-screenshotter/releases).
   3. Sign up for a [ScreenshotOne](https://screenshotone.com/) account and obtain your API `access_key` and `secret_key`. The free plan allows for 100 screenshots each month.
   4. Press the Windows key and the R key simultaneously. A 'run' dialog will show up.
   5. Type `cmd` and press enter.
   6. Type `cd` and then the [folder path](https://www.sony.com/electronics/support/articles/00015251) of the folder where `Screenshotter.py` is located. Example: `cd C:\Users\stach\OneDrive\Bureaublad\screenshotter`. Press enter.
   7. Type `pip install requests beautifulsoup4 screenshotone` and press enter.
   8. Type `python Screenshotter.py`. Press enter.
   9. Follow the instructions in the terminal to create screenshots.


![Program](/Images/program.png)
*Figure 2: the program in action.*

## Limitations

 - Nested sitemaps (sitemaps linking to other sitemaps), such as the default `/sitemap.xml` on WordPress installs, are not supported. For WordPress, use the individual sitemaps instead, such as `/wp-sitemap-posts-page-1.xml`.
 - The free plan at ScreenshotOne allows for 100 screenshots each month.
 - There is little error-checking built in. If the program stops, it is most likely because something went wrong with the API (e.g. you entered the wrong credentials, or the connection timed out).

## License
This project is released under the MIT License. See [LICENSE](LICENSE) for details.


## Acknowledgements
