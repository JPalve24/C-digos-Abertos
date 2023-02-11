import json

carros_dictionary = {
    "marca":"honda"
}

carros_list = ["honda"]
carros_tupla = ("honda")

carrosj = json.dumps(carros_list)

print(carrosj)