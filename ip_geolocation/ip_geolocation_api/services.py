import requests
import os


def fetch_geolocation_data_from_external_api(address):
    api_key = os.getenv("IPSTACK_API_KEY")
    url = f"https://api.ipstack.com/{address}?access_key={api_key}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "The external API took too long to respond. Please try again later."}
    except requests.exceptions.ConnectionError:
        return {"error": "Failed to connect to the API. Check your internet or API availability."}
    except requests.exceptions.RequestException as e:
        return {"error": f"Unexpected error: {str(e)}"}
