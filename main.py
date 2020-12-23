import requests
import fake_useragent

user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user
}

with open('Get_url.txt') as file:
    lines = [line.strip() for line in file]

    for line in lines:
        try:
            r = requests.head(line, headers=headers, timeout=4)
            if r.ok:
                print('ok')
                result = r
                with open('save_url/status_code_200.txt', 'a', encoding='utf-8') as file:
                    file.write(line + '\n')

        except requests.ConnectionError as e:
            print('OOPS!! Connection Error')
            with open('save_url/status_code_404.txt', 'a', encoding='utf-8') as file:
                file.write(line + '\n')



