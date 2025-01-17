import requests

access_token = 'YOUR_ACCESS_TOKEN'
user_id = 'PERSON_ID'
fields = 'birthday,about'
url = f'https://graph.facebook.com/v18.0/{user_id}?fields={fields}&access_token={access_token}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    birthday = data.get('birthday')
    about = data.get('about')
    print(f"Birthday: {birthday}, About: {about}")
else:
    print(f"Error: {response.status_code} - {response.text}")





access_token = 'YOUR_ACCESS_TOKEN'
user_id = 'PERSON_ID'
url = f'https://graph.facebook.com/v18.0/{user_id}/friends?access_token={access_token}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    friends = data.get('data', [])
    for friend in friends:
        friend_id = friend.get('id')
        print(f"Friend ID: {friend_id}")
else:
    print(f"Error: {response.status_code} - {response.text}")