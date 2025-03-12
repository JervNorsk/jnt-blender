import urllib.request

url = 'https://raw.githubusercontent.com/aquaproj/aqua-registry/refs/heads/main/registry.yaml'
file_path = 'registry.yaml'

try:
    urllib.request.urlretrieve(url, file_path)
    print('Synchronization completed')
except Exception as e:
    print(f'Synchronization failed. Error: {e}')