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
    print(response.text[:250])



def main():
    print_header()
    zip = gather_input()
    scrape_weather(zip)


if __name__ == '__main__':
    main()
