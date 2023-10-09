# Automatic XML Sitemap Screenshotter
> Automatically generate screenshots from URLs found in an XML sitemap.

Developed by Stach Redeker & ChatGPT, 2023. Released under the MIT license.

## Features
- Automatically extract URLs from a provided XML sitemap.
- Generate full-page screenshots with a width of 1920 pixels using the ScreenshotOne API.
- Customizable screenshot save location.

## Dependencies
- `os`
- `requests`
- `shutil`
- `bs4` (Beautiful Soup 4)
- `screenshotone`

## Installation & Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/[your_username]/sitemap-screenshotter.git
    cd sitemap-screenshotter
    ```
   
2. **Install Dependencies**
    ```bash
    pip install requests beautifulsoup4 screenshotone
    ```
   
3. **Configure API Credentials**
    - Sign up on [ScreenshotOne](https://screenshotone.com/) and obtain your API `access_key` and `secret_key`.
    - Input the API credentials when prompted by the application.

## Usage

Run the script:
```bash
python sitemap_screenshotter.py
```

## Limitations

 - Nested sitemaps (sitemaps linking to other sitemaps) are not supported.

## License
This project is released under the MIT License. See LICENSE for details.


## Acknowledgements
