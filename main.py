# install pip
# install the phonenumbers(package) through terminal
# pip install phonenumbers
import phonenumbers 
# imports the number from test.py
from test import number

from phonenumbers import geocoder
# C- country name H- for history
ch_number = phonenumbers.parse(number, "CH")
# print the country name 
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))