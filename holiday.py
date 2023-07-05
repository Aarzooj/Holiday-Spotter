'''other group member: Vanshika Pal (2022560)
APIs used:
the code checks if any holiday was celebrated in a country on the specific date provided by the user.
(by default location is set to the country the user is running the program from.)'''
import requests

url1="http://ip-api.com/json/"                                   #detecting user's country and countryCode by IP Address
resp=requests.get(url1)
data=resp.json()

if resp.status_code==200:
    print("Your current location details are:")
    for x in data.keys():
        if x=="country":
            country=data.get(x)
            print('country:',data.get(x))
        elif x=="countryCode":
            countryCode=data[x]
            print('countryCode:',data.get(x),'\n')
    print("Would you like to change this?")
    c=input("Enter(Yes/No):")
    if c=="Yes":                                                  #getting country code, in case the user decides to check for another country
        country = input('Entry Country:')
        url3 = 'https://api.first.org/data/v1/countries'
        resp3 = requests.get(url3)
        data3 = resp3.json()
        for (x, y) in data3.items():
            cc = {}
            if x == 'data':
                cc[x] = y
                break
        d = cc['data']
        for code, details in d.items():
            for x1, y1 in details.items():
                if y1 == country:
                    countryCode = code
                    print('Your Updated country is:',country)
                    print('Your Updated countryCode:', countryCode,'\n')
                    break
else:
    print("Invalid")
                                                                   #asking the user to input date
print('Enter date below:\n')
year=input("Enter the year:")
month=input("Enter the month:")
day=input("Enter the day:")


base_url="https://holidays.abstractapi.com/v1/?"                    #checking if a holiday was celebrated in the country
url2=base_url+f'api_key=3b7cc2f8c08240d996b322f77de86216&country={countryCode}&year={year}&month={month}&day={day}'

response = requests.get(url2)
print(response.status_code)
data3=response.json()

if data3==[]:
    print('No holiday was celebrated on this day in',country)
else:
    data4=data3[0]
    print(data4)
    print(data4.get('name'),' was celebrated on ',day,'/',month,'/',year,' in ',country,'.',sep='')


