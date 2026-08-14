user = {
    "id": 1,
    "firstName": "Emily",
    "lastName": "Johnson",
    "address": {
        "city": "Phoenix",
        "postalCode": "29112",
        "coordinates": {
          "lat": -77.16213,
          "lng": -92.084824
        }
      }
}

print(user["address"]["city"])
print(user["address"]["coordinates"]["lat"])