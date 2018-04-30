import os
import requests
import secrets
import pprint

def send_event(event):
    del event['description']
    response = requests.post(
        'http://localhost:5000/event/', json=event)
    return response


def main():
    sk = secrets.token_hex()
    sk_ = secrets.token_hex()
    events = [
        {
            'description': 'anonymous user views a page',
            'sk': sk,
            'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'ip': '201.21.33.54',
            'ts': '12345',
            'ec': 'root',
            'en': 'pageview',
            'ed': {
                'hostname': 'localhost',
                'path': '/a/random/path/',
            }
        },
        {
            'description': 'anonymous user views another page (same session key)',
            'sk': sk,
            'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'ip': '201.21.33.54',
            'ts': '23456',
            'ec': 'root',
            'en': 'pageview',
            'ed': {
                'hostname': 'localhost',
                'path': '/another/random/path/',
            }
        },
        {
            'description': 'anonymous user registers in the site (event contains an `uid`)',
            'sk': sk,
            'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'ip': '201.21.33.54',
            'ts': '34567',
            'uid': 'ramonsaraiva@gmail.com',
            'ec': 'accounts',
            'en': 'user registration',
            'ed': {
                'email': 'ramonsaraiva@gmail.com',
                'social': True,
                'source': 'facebook'
            }
        },
        {
            'description': 'anonymouse user logs out (event does not contain an `uid` anymore)',
            'sk': sk,
            'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'ip': '201.21.33.54',
            'ts': '34567',
            'ec': 'accounts',
            'en': 'logout',
        },
        {
            'description': 'pageview from another IP with another session',
            'sk': sk_,
            'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'ip': '72.229.28.185',
            'ts': '45678',
            'ec': 'root',
            'en': 'pageview',
            'ed': {
                'path': '/my/amazing/path/',
                'category': 'my site category'
            }
        },
        {
            'description': 'another IP user logged in',
            'sk': sk_,
            'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'ip': '72.229.28.185',
            'ts': '45678',
            'uid': 'john@doe.com',
            'ec': 'accounts',
            'en': 'login',
            'ed': {
                'login_flow_version': 2.0,
                'login_flow_variant': 'big green login button'
            }
        },
    ]
    for event in events:
        os.system('clear')
        pprint.pprint(event)
        input(f'\nPress enter to send the next event')
        response = send_event(event)


if __name__ == '__main__':
    main()
