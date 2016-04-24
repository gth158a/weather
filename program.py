import bs4
import requests


def print_header():
    print('---------------------')
    print('     WEATHER APP')
    print('---------------------')


def gather_input():
    zip = input('Please enter your zip code (ex:77055) ')
    #print(zip)

    return zip


def scrape_weather(zip):

    url = 'https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}'.format(zip)
    response = requests.get(url)

    #print(response.text[:250])


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    soup.fin


def main():
    print_header()
    zip = gather_input()
    scrape_weather(zip)
    get_weather_from_html(html)


if __name__ == '__main__':
    main()
