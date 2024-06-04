import requests

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Application is UP and functioning correctly."
        else:
            return "Application is DOWN. Status code: {}".format(response.status_code)
    except requests.ConnectionError:
        return "Could not connect to the application. It may be down or unavailable."

# Example usage:
if __name__ == "__main__":
    application_url = "http://example.com"  # Replace this with the URL of your application
    status = check_application_status(application_url)
    print(status)
