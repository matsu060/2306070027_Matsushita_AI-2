import requests

def get_country_info(name: str):
    """国名を指定して情報を取得"""
    url = f"https://restcountries.com/v3.1/name/{name}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    if not data:
        return None

    country = data[0]
    return {
        "name": country["name"]["common"],
        "capital": country.get("capital", ["不明"])[0],
        "population": country["population"],
        "region": country["region"],
        "flag": country["flags"]["png"],
    }
