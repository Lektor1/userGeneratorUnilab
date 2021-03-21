import requests


def get_users():
    resp = requests.get('https://randomuser.me/api/?results=200&inc=name,email,picture')
    if resp.status_code == 200:
        user_list = []

        num = 0
        for item in resp.json()['results']:
            temp_dict = {}
            temp_dict['id'] = num
            temp_dict['name'] = item['name']['title'] + ". " + item['name']['first'] + " " + item['name']['last']
            temp_dict['email'] = item['email']
            temp_dict['img'] = item['picture']['medium']
            num = num + 1
            user_list.append(temp_dict)

        return user_list
    else:
        raise Exception
