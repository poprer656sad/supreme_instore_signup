import subprocess, sys, json, time, urllib.parse

def install_dependencies():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'httpx'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'lxml'])

try:
    import httpx, lxml.html as html
except:
    install_dependencies()
    import httpx, lxml.html as html


def get_captcha():
    print('waiting for captcha')
    while True:
        try:
            captcha = json.loads(httpx.get('http://your_captcha_harvester/fetch').text.strip('[]').strip())['token']
            if len(captcha) > 2:
                return captcha
        except:
            continue

class supremesignup():
    def __init__(self, customer, billing, card):
        self.name, self.email, self.tel, self.location, self.state = customer['name'], customer['email'], customer['tel'], customer['location'], customer['state']
        self.st1, self.st2, self.zip, self.city, self.state = billing['st3'], billing['street_2'], billing['zip'], billing['city'], billing['state']
        self.cn, self.month, self.year, self.verification_value = card['cn'], card['month'], card['year'], card['verification_value']
        self.session = httpx.Client(http2=True)
        self.registry_page()
        self.set_form_cookie()
        self.customers()
        while self.status == 'queued':
            time.sleep(1)
            self.get_status()
        print(self.state)


    def registry_page(self):
        headers = {
            'authority': 'register.supremenewyork.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        response = self.session.get('https://register.supremenewyork.com/signup', headers=headers)
        self.csrf_token = html.fromstring(response.content).xpath('//*[contains(@name,"csrf-token")]')[0].get('content')

    def set_form_cookie(self):
        cookie_val = urllib.parse.quote('{"utf8":"✓","authenticity_token":"{}","nime":"","nrime":"{}","customer[email]":"{}","customer[tel]":"{}","customer[location_preference]":"{}","st3":"","customer[street_2]":"","customer[zip]":"","customer[city]":"","customer[state]":"{}","credit_card[cn]":"","credit_card[month]":"","credit_card[year]":"","credit_card[verification_value]":"","g-recaptcha-response":""}'.format(self.csrf_token, self.name, self.email, self.tel, self.location, self.state))
        try:
            del self.session.cookies['form']
        except:
            pass
        self.session.cookies.set(name='form', value=cookie_val, domain='register.supremenewyork.com')

    def customers(self):
        headers = {
            'authority': 'register.supremenewyork.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': '*/*',
            'x-csrf-token': self.csrf_token,
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://register.supremenewyork.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://register.supremenewyork.com/signup/2',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        data = {
            'utf8': '\u2713',
            'authenticity_token': self.csrf_token,
            'nime': '',
            'nrime': self.name,
            'customer[email]': self.email,
            'customer[tel]': self.tel,
            'customer[location_preference]': self.location,
            'st3': self.st1,
            'customer[street_2]': self.st2,
            'customer[zip]': self.zip,
            'customer[city]': self.city,
            'customer[state]': self.state,
            'credit_card[cn]': self.cn,
            'credit_card[month]': self.month,
            'credit_card[year]': self.year,
            'credit_card[verification_value]': self.verification_value,
            'g-recaptcha-response': get_captcha()
        }

        response = self.session.post('https://register.supremenewyork.com/customers', headers=headers, data=data)
        self.status, self.slug_val = json.loads(response.content)['status'], json.loads(response.content)['queue_slug']

    def get_status(self):
        headers = {
            'authority': 'register.supremenewyork.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': '*/*',
            'x-csrf-token': self.csrf_token,
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://register.supremenewyork.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://register.supremenewyork.com/signup/2',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        params = {'id':self.slug_val}

        data = {
            'utf8': '\u2713',
            'authenticity_token': self.csrf_token,
            'nime': '',
            'nrime': self.name,
            'customer[email]': self.email,
            'customer[tel]': self.tel,
            'customer[location_preference]': self.location,
            'st3': self.st1,
            'customer[street_2]': self.st2,
            'customer[zip]': self.zip,
            'customer[city]': self.city,
            'customer[state]': self.state,
            'credit_card[cn]': self.cn,
            'credit_card[month]': self.month,
            'credit_card[year]': self.year,
            'credit_card[verification_value]': self.verification_value,
            'g-recaptcha-response': ''
        }

        response = self.session.post('https://register.supremenewyork.com/customers/status.json', headers=headers, params=params, data=data)
        self.status = json.loads(response.content)['status']



customer_info = {
    'name':'jasper briggs',
    'email':'jasperbriggs677@gmail.com',
    'tel':'(123) 456-7890',
    'location': 'manhattan',
    'state':'NY'
}

billing_info = {
    'st3': '123-45 jane doe lane', #addr line 1
    'street_2': '2B', #addr line 2
    'zip': '12345',
    'city': 'Hackensack',
    'state': 'NJ',
}

card_info = {
    'cn': 'xxxx xxxx xxxx xxxx',
    'month': 'xx',#one or two digits. dont write may as 05 just write 5. you get the idea
    'year': 'xxxx',
    'verification_value': 'xxx', #cvv
}

_ = supremesignup(customer_info)