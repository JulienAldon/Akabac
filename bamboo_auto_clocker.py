import datetime
import requests
import json
import sys
import browser_cookie3
from requests.utils import dict_from_cookiejar
import re
import argparse

def clock_day(date: str, header_cookie: str, csrf_token: str, time_ranges):
    """
    date format YYYY-MM-DD
    """
    resp = requests.post('https://epitech.bamboohr.com/timesheet/clock/entries',
            json=json.loads('{"entries":[{"id":null,"trackingId":1,"employeeId":1295,"date":"' + date + '","start":"' + time_ranges[0][0] + '","end":"' + time_ranges[0][1] + '","note":"","projectId":null,"taskId":null},{"id":null,"trackingId":2,"employeeId":1295,"date":"' + date +'","start":"' + time_ranges[1][0] + '","end":"' + time_ranges[1][1] + '","projectId":null,"taskId":null}]}'),
            headers={
                'Content-Type': 'application/json;charset=utf-8', 
                'X-CSRF-TOKEN': csrf_token,
                'Cookie': header_cookie
            }
        )
    print(resp)

def generate_date_range(month: str):
    first_day = datetime.datetime.strptime(f'2022-{month}-01', '%Y-%m-%d')
    delta = datetime.timedelta(days=1)
    current_date = first_day
    date_range = []
    while current_date.month == int(month):
        if current_date.isoweekday() < 6:
            date_range.append(current_date.strftime('%Y-%m-%d'))
        current_date += delta
    return date_range

def clock_month(month: str, cookie_jar: str, csrf_token: str, time_ranges):
    dates = generate_date_range(month)
    for date in dates:
        clock_day(date, cookie_jar, csrf_token, time_ranges)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clock for the current month (use it at the end of the month)')
    parser.add_argument('--browser', metavar='browser', type=str, nargs=1,
                    help='Browser used to get the cookie jar', required=True)
    parser.add_argument('--time-range', type=str, nargs=2, 
                    help='Time range of the clock in', required=False)
    args = parser.parse_args()
    if args:
        if args.browser[0] == 'firefox':
            cj = browser_cookie3.firefox(domain_name='bamboohr.com')
        elif args.browser[0] == 'chrome':
            cj = browser_cookie3.chrome(domain_name='bamboohr.com')
        else:
            print('Browser not supported')
            sys.exit(84)
    else: 
        cj = browser_cookie3.firefox(domain_name='bamboohr.com')

    if not cj:
        print('Error could not get cookie jar')
        sys.exit(84)
    
    if args.time_range:
        time_ranges = [
            (args.time_range[0].split('-')[0], args.time_range[0].split('-')[1]),
            (args.time_range[1].split('-')[0], args.time_range[1].split('-')[1]),            
        ]
    else:
        time_ranges = [('9:00', '12:00'), ('13:00', '18:00')]

    cj_dict = dict_from_cookiejar(cj)
    cj_string = 'Cookie: '
    for a in cj_dict.items():
        cj_string += f'{a[0]}={a[1]}; '

    resp = requests.get('https://epitech.bamboohr.com/employees/timesheet/?id=1295&et_id=23529', headers={
        'Cookie': cj_string
    })

    csrf_token = re.findall(r'var CSRF_TOKEN = "(.*?)"', resp.text)[0]
    today = datetime.datetime.today()
    clock_month(today.strftime("%m"), cj_string, csrf_token, time_ranges)