import requests
import json

# Replace 'your_json_file.json' with the path to your JSON file.
file_path = './alldata.json'

# Open the JSON file in read mode
with open(file_path, 'r', encoding='UTF-8') as file:
    c = 0
	# Read and process each line
    for line in file:
        c+=1
		# Parse the JSON data from the line
        if c>=6000:
            print('DONE', c)
            break
        else:
		
            try:
                # Now, 'data' contains the JSON object from the current line

                url = "http://agesamarkand.uz/api/create_building/"

                payload = json.dumps(json.loads(line.strip().rstrip(',')))
                headers = {
                'Content-Type': 'application/json'
                }

                response = requests.request("POST", url, headers=headers, data=payload)

                # if c == 3: break

                print(response.text, c)
                # print(payload)
        
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}", c)