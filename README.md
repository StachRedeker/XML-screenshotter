# Automatic XML Sitemap Screenshotter
> Automatically generate screenshots from URLs found in an XML sitemap using the ScreenshotOne API in Python.

Developed by Stach Redeker & ChatGPT, 2023. Released under the MIT license.

## Features
- Automatically extract URLs from a provided XML sitemap.
- Generate full-page screenshots with a width of 1920 pixels using the ScreenshotOne API.
- Customizable screenshot save location.

## Minimal (system) requirements
- The program is built and tested for Windows operating systems using Python 3.9.
- The working on other technology stacks cannot be guaranteed. 

### Python dependencies
- `os`
- `requests`
- `shutil`
- `bs4` (Beautiful Soup 4)
- `screenshotone`

## Installation, setup and usage

### Beginner-friendly installation guide

<details>
   
   1. Download Python 3.9 at the [Python website](https://www.python.org/downloads/release/python-390/).
   2. Download the latest release of XML-screenshotter at (Releases)[https://github.com/StachRedeker/XML-screenshotter/releases].
   3. Sign up for a [ScreenshotOne](https://screenshotone.com/) account and obtain your API `access_key` and `secret_key`. The free plan allows for 100 screenshots each month.
   4. Press the Windows key and the R key simultaneously. A 'run' dialog will show up.
   5. Type `cmd` and press enter.
   6. Type `cd` and then the [folder path](https://www.sony.com/electronics/support/articles/00015251) of the folder where `Screenshotter.py` is located. Example: `cd C:\Users\stach\OneDrive\Bureaublad\screenshotter`. Press enter.
   7. Type `pip install requests beautifulsoup4 screenshotone` and press enter.
   8. Type `python Screenshotter.py`. Press enter.
   9. Follow the instructions in the terminal to create screenshots.
 
</details>


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

## Limitations

 - Nested sitemaps (sitemaps linking to other sitemaps) are not supported.

## License
This project is released under the MIT License. See [LICENSE](LICENSE) for details.


## Acknowledgements
