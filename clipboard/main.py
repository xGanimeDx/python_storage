import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

# Save the data to JSON file
def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

# Read the data from JSON file 
def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

# Actions depends on the command entered
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print('Data saved')
    elif command == 'load':
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard')
        else:
            print('Key does not exist')
    elif command == 'list':
        for key in data:
            print(key + " : " + data[key])
    elif command == 'delete':
        key = input("Enter a key: ")
        del data[key]
        save_data(SAVED_DATA, data)
        print('Data deleted')
    else:
        print('Unknown command')
else:
    print('Please pass exactly one command')