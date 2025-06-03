def katta_harfga(value:dict) -> None:
    for k in value.keys():
        value[k] = value[k].upper()
        

dct = {"Ism": "Ali", "Familya": "Kamolov", "Manzil": "Angren shahri"}

katta_harfga(dct)
print(dct)
