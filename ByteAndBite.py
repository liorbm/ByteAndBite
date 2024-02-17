import requests
import time
from datetime import datetime


def convert_wolt_url_to_api_url(wolt_restaurant):
    restaurant_url = wolt_restaurant.split("/")
    restaurant_name = restaurant_url[-1]
    api_url = f"https://consumer-api.wolt.com/order-xp/web/v1/venue/slug/{restaurant_name}/dynamic"
    return api_url, restaurant_name


def check_venue_status(api_url):
    while True:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            delivery_status = data["venue"]["delivery_open_status"]["style"]["type"]
            online_status = data['venue']['online']
            online_text_variations = ["OPEN", "CLOSING_SOON"]
            current_time = datetime.now().strftime("%H:%M:%S")
            is_venue_available = delivery_status in online_text_variations and online_status

            if is_venue_available:
                print(f"Venue is open at: {current_time}. Bon Appétit.")
                break
            else:
                print(f"Venue is closed. Retrying in 5 seconds... ({current_time})")
                time.sleep(5)
        else:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Error: Unable to fetch data. Status code: {response.status_code}. Retrying in 5 seconds... ({current_time})")
            time.sleep(5)


if __name__ == "__main__":
    wolt_restaurant = input("Enter the Wolt web address of the restaurant's page:\n")
    final_api_url, restaurant_name = convert_wolt_url_to_api_url(wolt_restaurant)
    print(f"Polling {final_api_url} to check if {restaurant_name} is open")

    check_venue_status(final_api_url)
    input("Press ENTER to close ByteAndBite....")
