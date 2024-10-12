import http.client

conn = http.client.HTTPSConnection("whatsapp-number-validators.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "bc630e52eamshf94e9756bce8b9fp12cfedjsn0b12a1fa852e",
    'x-rapidapi-host': "whatsapp-number-validators.p.rapidapi.com"
}
number1=int(input("enter number here"))
conn.request("GET", "/v1/validate/phone?number=number1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
