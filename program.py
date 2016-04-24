import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


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
    response = requests.get(url) #what type of object is response?? bc we need to use .text

    return response.text

    #print(response.text[:250])


def cleanup_text(text: str):
    if not text:
        return text
    text = text.strip()
    return text


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()



def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    
    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(loc=loc, cond=condition, temp=temp, scale=scale)
    return report


def print_report(rep: WeatherReport):
    print('The temp in {} is {} {} and {}'.format(
        rep.loc,
        rep.temp,
        rep.scale,
        rep.cond
    ))


def main():
    print_header()
    zip = gather_input()
    html = scrape_weather(zip)
    rep = get_weather_from_html(html)
    print_report(rep)


if __name__ == '__main__':
    main()
