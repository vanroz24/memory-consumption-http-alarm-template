import psutil
import requests
import time

API_URL = 'https://example.com/api/alarm'

# Get memory usage percentage
def get_memory_usage():
    return psutil.virtual_memory().percent

# Send HTTP request to the API
def send_alarm():
    payload = {'message': 'Memory consumption exceeded threshold!'}
    response = requests.post(API_URL, data=payload)
    if response.status_code == 200:
        print('Alarm sent successfully!')
    else:
        print('Failed to send alarm.')

# Set the memory percentage threshold
memory_threshold = 80

if __name__ == '__main__':
    # Main loop to monitor memory usage
    while True:
        memory_usage = get_memory_usage()

        # Check if memory usage exceeds the threshold
        if memory_usage > memory_threshold:
            send_alarm()

        print(memory_usage)

        # Sleep for a short interval before checking again
        time.sleep(5)
