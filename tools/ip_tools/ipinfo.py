import requests

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    
    # Print raw response for debugging
    print("Raw response:", response.text)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data (status code: {response.status_code})")
        return {}

def main():
    ip = input("Enter the IP address you want to get information about: ")
    info = get_ip_info(ip)
    
    print("\nIP Information:")
    print(f"IP: {info.get('ip', 'N/A')}")
    print(f"City: {info.get('city', 'N/A')}")
    print(f"Region: {info.get('region', 'N/A')}")
    print(f"Country: {info.get('country', 'N/A')}")
    print(f"Location: {info.get('loc', 'N/A')}")
    print(f"ISP: {info.get('org', 'N/A')}")
    
    # Pause until a key is pressed
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
