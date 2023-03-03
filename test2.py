
import requests 

url = "https://flagcdn.com/fr/codes.json"

try:
    response_dict   = requests.request("GET", url).json()
except:
    pass

for v in response_dict:
    url = f"https://flagcdn.com/h240/{v}.png"

    try:
        response   = requests.get(url)
        with open(f'{response_dict[v]}.png', 'wb') as f:
            f.write(response.content)
    
    except:
        pass

