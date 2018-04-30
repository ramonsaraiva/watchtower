import json
import requests
import time
import os


def routine():
    response = requests.get('http://localhost:5000/event/')
    data = json.loads(response.text)
    users = data['users']
    fingerprints = data['fingerprints']
    sessions = data['sessions']
    events = data['events']
    uas = data['uas']
    components = data['components']
    print('Users')
    for i, user in enumerate(users):
        print(f'#{i}: {user}')
    print()
    print('Fingerprints')
    for i, fingerprint in enumerate(fingerprints):
        print(f'#{i}: {fingerprint}')
    print()
    print('Sessions')
    for i, session in enumerate(sessions):
        print(f'#{i}: {session}')
    print()
    print('Events')
    for i, event in enumerate(events):
        print(f'#{i}: {event}')
    print()
    print('User Agents')
    for i, ua in enumerate(uas):
        print(f'#{i}: {ua}')
    print()
    print('UA Components')
    for i, c in enumerate(components):
        print(f'#{i}: {c}')


def main():
    while 1:
        os.system('clear')
        routine()
        time.sleep(1)


if __name__ == '__main__':
    main()
