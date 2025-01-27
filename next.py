import requests

API_KEY = "YOUR_API_KEY"
STOP_ID = "12345"  

def get_next_muni_trains(api_key, stop_id):
    base_url = "https://api.511.org/transit/predictions"
    params = {
        "api_key": api_key,
        "stopCode": stop_id,
        "agency": "SF"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        predictions = data.get("predictions", [])
        if not predictions:
            print("No upcoming trains found.")
            return

        print(f"Upcoming Muni trains for stop ID {stop_id}:")
        for prediction in predictions:
            route = prediction.get("routeTitle", "Unknown Route")
            direction = prediction.get("directionTitle", "Unknown Direction")
            minutes = prediction.get("minutes", "N/A")
            print(f"Route: {route}, Direction: {direction}, Arrival in: {minutes} minutes")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Muni data: {e}")

if __name__ == "__main__":
    get_next_muni_trains(API_KEY, STOP_ID)
