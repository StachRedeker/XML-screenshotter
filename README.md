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
   
1. **Installing Dependencies**
    ```bash
    pip install requests beautifulsoup4 screenshotone
    ```
   
2. **Creating API Credentials**
    - Sign up for a [ScreenshotOne](https://screenshotone.com/) account and obtain your API `access_key` and `secret_key`. The free plan allows for 100 screenshots each month
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
