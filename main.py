mport json

def transform_data(data):
    result = []
    
    for item in data:
        new_item = {
            "device_id": item.get("device_id", item.get("id")),
            "temperature": item.get("temperature", item.get("temp")),
            "humidity": item.get("humidity"),
            "timestamp": item.get("timestamp")
        }
        result.append(new_item)
    
    return result

with open('data-1.json') as f:
    data1 = json.load(f)

with open('data-2.json') as f:
    data2 = json.load(f)

result1 = transform_data(data1)
result2 = transform_data(data2)

final_result = result1 + result2

with open('data-result.json', 'w') as f:
    json.dump(final_result, f, indent=4)

print("Done")
