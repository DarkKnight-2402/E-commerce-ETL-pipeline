import requests
import json
import os


def extract():
    url = "https://fakestoreapi.com/products"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        os.makedirs("data/raw", exist_ok=True)

        with open("data/raw/products.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Extraction completed.")

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        raise

    except ValueError as e:
        print(f"Invalid JSON response: {e}")
        raise


if __name__ == "__main__":
    extract()