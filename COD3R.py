# Agar Daskariw Krd Naw Labir Maka @hama_software 
# instagram : hama_software
# telegram  : hama_software

import requests
import time
import re
import os
os.system('clear')
r = requests.session()
print("""
\033[0;36m


\x1b[0m
\033[0;31m
              ██  ██████  
              ██ ██       
              ██ ██   ███ 
              ██ ██    ██ 
              ██  ██████  
            
            \x1b[0m
       ╦═╗╔═╗╔═╗╔═╗╦═╗╔╦╗  ╔╗ ╔═╗╔╦╗
       ╠╦╝║╣ ╠═╝║ ║╠╦╝ ║   ╠╩╗║ ║ ║
       ╩╚═╚═╝╩  ╚═╝╩╚═ ╩   ╚═╝╚═╝ ╩
       
       [+] Tlegram : @RUSY780
       [+] Canale  : @kurany_agryn





""")

print('[+] 1- Auto All Report ')
print('[+] 2- Choose Report ')
kurd = input('\033[1;36m[+] Choose ==> : \x1b[0m ')
if kurd == '1':
    print('[!] Login With Account   ..')
    username = input('[+] User  ==> : ')
    password = input('[+] Password ==> : ')
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '274',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
    }
    data = {
    'username': username,
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:'+password,
    'queryParams': '{}',
    'optIntoOneTap': 'false'
    }
    req_login = requests.post(url, data=data, headers=headers)
    if '"authenticated":true' in req_login.text:
        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
        print('\033[1;32m[+] Login Successfully  ..')
    else:
        print('\033[0;31m[+] Faild Login\x1b[0m')
    sessionid1 = req_login.cookies['sessionid']
    print('[+] Dump ID Taret With Link ==> : https://codeofaninja.com/tools/find-instagram-user-id/')
    print('[+] And Paste ID Here ..')
    idinsta = input('\033[1;36m[+] User Target ==> : \x1b[0m')
    url_report_spam = f'https://www.instagram.com/users/{idinsta}/report/'
    headers_report_spam = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '37',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid1}; rur=VLL',
    'origin': 'https://www.instagram.com',
    'referer': f'https://www.instagram.com/users/{idinsta}/report/inappropriate',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest',
    }
    data_report_spam = {
    'source_name': '',
    'reason_id': '1',
    'frx_context': ''
    }
    url_report_self = f'https://www.instagram.com/users/{idinsta}/report/'
    headers_report_self = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '37',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid1}; rur=VLL',
        'origin': 'https://www.instagram.com',
        'referer': f'https://www.instagram.com/users/{idinsta}/report/inappropriate',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',
        'x-instagram-ajax': '1cb44f68ffec',
        'x-requested-with': 'XMLHttpRequest',
    }
    data_report_self = {
        'source_name': '',
        'reason_id': '2',
        'frx_context': ''
    }
    url_report_suicide = f'https://www.instagram.com/users/{idinsta}/report/'
    headers_report_suicide = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '37',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid1}; rur=VLL',
    'origin': 'https://www.instagram.com',
    'referer': f'https://www.instagram.com/users/{idinsta}/report/inappropriate',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest',
    }
    data_report_suicide = {
    'source_name': '',
    'reason_id': '4',
    'frx_context': ''
    }
    url_report_violence = f'https://www.instagram.com/users/{idinsta}/report/'
    headers_report_violence = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '37',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid1}; rur=VLL',
    'origin': 'https://www.instagram.com',
    'referer': f'https://www.instagram.com/users/{idinsta}/report/inappropriate',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest',
    }
    data_report_violence = {
    'source_name': '',
    'reason_id': '5',
    'frx_context': ''
    }
    while True:
        req_report_spam = requests.post(url_report_spam, data=data_report_spam, headers=headers_report_spam).text
        if '"description":"Your reports help keep our community free of spam.","status":"ok"' in req_report_spam:
            print(f'\033[1;32m[+] Report Spam Has Been Sent ')
            time.sleep(3)
        else:
            print('\033[0;31m[-] Faild Report Spam')
        req_report_self = requests.post(url_report_self, data=data_report_self, headers=headers_report_self).text
        if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_report_self:
            print('\033[1;32m[+] Report Self Has Been Sent')
            time.sleep(3)
        else:
            print('\033[0;31m[-] Faild Report Self')
        req_report_suicide = requests.post(url_report_suicide, data=data_report_suicide, headers=headers_report_suicide).text
        if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_report_suicide:
            print('\033[1;32m[+] Report Suicide Has Been Sent')
            time.sleep(3)
        else:
            print('\033[0;31m[-] Faild Report Suicide')
        req_report_violence = requests.post(url_report_violence, data=data_report_violence, headers=headers_report_violence).text
        if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_report_violence:
            print('\033[1;32m[+] Report Violence Has Been Sent')
            time.sleep(3)
        else:
            print('\033[0;31m[-] Faild Report Violence ')
if kurd == '2':
    print('[+] 1 - Report Spam')
    print('[+] 2 - Report Self Injury')
    print('[+] 3 - Report Suicide')
    print('[+] 4 - Report Violence')
    kurd2 = input('\033[1;36m[+] Choose ==> : \x1b[0m')
    if kurd2 == '1':
        print('[!] Login With Account ..')
        username_login = input('[+] User  ==> : ')
        password_login = input('[+] Password ==> : ')
        url_login = 'https://www.instagram.com/accounts/login/ajax/'
        headers_login = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '274',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest'
        }
        data_login = {
            'username': username_login,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:' + password_login,
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        req_login2 = requests.post(url_login, data=data_login, headers=headers_login)
        if '"authenticated":true' in req_login2.text:
            r.headers.update({'X-CSRFToken': req_login2.cookies['csrftoken']})
            print('\033[1;32m[+] Login Successfully ..')
        else:
            print('\033[0;31m[+] Faild Login\x1b[0m')
        sessionid2 = req_login2.cookies['sessionid']
        print('[+] Dump ID Taret With Link ==> : https://codeofaninja.com/tools/find-instagram-user-id/')
        print('[+] And Paste ID Here ..')
        idinsta2 = input('\033[1;36m[+] User Target ==> : \x1b[0m')
        url_report_spam2 = f'https://www.instagram.com/users/{idinsta2}/report/'
        headers_report_spam2 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '37',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid2}; rur=VLL',
            'origin': 'https://www.instagram.com',
            'referer': f'https://www.instagram.com/users/{idinsta2}/report/inappropriate',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest',
        }
        data_report_spam2 = {
            'source_name': '',
            'reason_id': '1',
            'frx_context': ''
        }
        while True:
            req_spam2 = requests.post(url_report_spam2, data=data_report_spam2, headers=headers_report_spam2).text
            if '"description":"Your reports help keep our community free of spam.","status":"ok"' in req_spam2:
                print(f'\033[1;32m[+] Report Spam Has Been Sent')
                time.sleep(3)
            else:
                print('\033[0;31m[-] Faild Report Spam\x1b[0m')
    if kurd2 == '2':
        print('[!] Login With Account   .. ..')
        username_login3 = input('[+] User  ==> : ')
        password_login3 = input('[+] Password ==> : ')
        url_login3 = 'https://www.instagram.com/accounts/login/ajax/'
        headers_login3 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '274',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest'
        }
        data_login3 = {
            'username': username_login3,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:' + password_login3,
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        req_login3 = requests.post(url_login3, data=data_login3, headers=headers_login3)
        if '"authenticated":true' in req_login3.text:
            r.headers.update({'X-CSRFToken': req_login3.cookies['csrftoken']})
            print('\033[1;32m[+] Login Successfully ...')
        else:
            print('\033[0;31m[+] Faild Login\x1b[0m')
        sessionid3 = req_login3.cookies['sessionid']
        print('[+] Dump ID Taret With Link ==> : https://codeofaninja.com/tools/find-instagram-user-id/')
        print('[+] And Paste ID Here ..')
        idinsta3 = input('\033[1;36m[+] User Target ==> : \x1b[0m')
        url_report_self2 = f'https://www.instagram.com/users/{idinsta3}/report/'
        headers_report_self2 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '37',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid3}; rur=VLL',
            'origin': 'https://www.instagram.com',
            'referer': f'https://www.instagram.com/users/{idinsta3}/report/inappropriate',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest',
        }
        data_report_self2 = {
            'source_name': '',
            'reason_id': '2',
            'frx_context': ''
        }
        while True:
            req_self = requests.post(url_report_self2, data=data_report_self2, headers=headers_report_self2).text
            if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_self:
                print('\033[1;32m[+] Report Self Has Been Sent')
                time.sleep(3)
            else:
                print('\033[0;31m[-] Faild Report Self\x1b[0m')
    if kurd2 == '3':
        print('[!] Login With Account   ..')
        username_login4 = input('[+] User  ==> : ')
        password_login4 = input('[+] Password ==> : ')
        url_login4 = 'https://www.instagram.com/accounts/login/ajax/'
        headers_login4 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '274',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest'
        }
        data_login4 = {
            'username': username_login4,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:' + password_login4,
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        req_login4 = requests.post(url_login4, data=data_login4, headers=headers_login4)
        if '"authenticated":true' in req_login4.text:
            r.headers.update({'X-CSRFToken': req_login4.cookies['csrftoken']})
            print('\033[1;32m[+] Login Successfully  ..')
        else:
            print('\033[0;31m[-] Faild Login\x1b[0m')
        sessionid4 = req_login4.cookies['sessionid']
        print('[+] Dump ID Taret With Link ==> : https://codeofaninja.com/tools/find-instagram-user-id/')
        print('[+] And Paste ID ..')
        idinsta4 = input('\033[1;36m[+] User Target ==> : \x1b[0m')
        url_report_suicide2 = f'https://www.instagram.com/users/{idinsta4}/report/'
        headers_report_suicide2 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '37',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid4}; rur=VLL',
            'origin': 'https://www.instagram.com',
            'referer': f'https://www.instagram.com/users/{idinsta4}/report/inappropriate',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest',
        }
        data_report_suicide2 = {
            'source_name': '',
            'reason_id': '4',
            'frx_context': ''
        }
        while True:
            req_ant7ar = requests.post(url_report_suicide2, data=data_report_suicide2, headers=headers_report_suicide2).text
            if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_ant7ar:
                print('\033[1;32m[+] Report Suicide Has Been Sent')
                time.sleep(3)
            else:
                print('\033[0;31m[-] Faild Report Suicide\x1b[0m')
    if kurd2 == '4':
        print('[!] Login With Account   ..')
        username_login5 = input('[+] User  ==> : ==> : ')
        password_login5 = input('[+] Password ==> : ')
        url_login5 = 'https://www.instagram.com/accounts/login/ajax/'
        headers_login5 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '274',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest'
        }
        data_login5 = {
            'username': username_login5,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:' + password_login5,
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        req_login5 = requests.post(url_login5, data=data_login5, headers=headers_login5)
        if '"authenticated":true' in req_login5.text:
            r.headers.update({'X-CSRFToken': req_login5.cookies['csrftoken']})
            print('\033[1;32m[+] Login Successfully  ..')
        else:
            print('\033[0;31m[+] Faild Login ...\x1b[0m')
        sessionid5 = req_login5.cookies['sessionid']
        print('[+] Dump ID Taret With Link ==> : https://codeofaninja.com/tools/find-instagram-user-id/')
        print('[+] And Paste ID Here ..')
        idinsta5 = input('\033[1;36m[+] User Target ==> : \x1b[0m')
        url_report_violence2 = f'https://www.instagram.com/users/{idinsta5}/report/'
        headers_report_violence2 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '37',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid5}; rur=VLL',
            'origin': 'https://www.instagram.com',
            'referer': f'https://www.instagram.com/users/{idinsta5}/report/inappropriate',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest',
        }
        data_report_violence2 = {
        'source_name': '',
        'reason_id': '5',
        'frx_context': ''
        }
        while True:
            req_3nf = requests.post(url_report_violence2, data=data_report_violence2, headers=headers_report_violence2).text
            if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_3nf:
                print('\033[1;32m[+] Report Violence Has Been Sent')
                time.sleep(3)
            else:
                print('\033[0;31m[-] Faild Report Violence\x1b[0m ')
