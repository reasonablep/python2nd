#custom filters for formatting data
#string format time method
def format_date(date):
    return date.strftime('%m/%d/%y')

#testing

from datetime import datetime
print(format_date(datetime.now()))

#remove all extraneous information from the URL

def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

print(format_url('http://google.com/test/'))
print(format_url('https://www.google.com?q=test'))

#pluralize words correctly

def format_plural(amount, word):
    if amount != 1:
        return word + 's'
    return word

print(format_plural(2, 'cat'))
print(format_plural(1, 'dog'))