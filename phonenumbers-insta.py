import phonenumbers
from phonenumbers import timezone,geocoder,carrier
phoneNumber=phonenumbers.parse("+918106507485")
timeZone=timezone.time_zone_for_numbers(phoneNumber)
carrier=carrier.name_for_number(phoneNumber,'en')
Region=geocoder>description_for_number(phoneNumber,'en')
print(phoneNumber)
print(timeZone)
print(carrier)
print(Region)






















