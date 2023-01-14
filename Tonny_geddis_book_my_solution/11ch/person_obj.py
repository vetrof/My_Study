
from objects import person

status_client = person.Customer('jon', 'NY', 345678543, 998, True)

print(status_client.get_name())
print(status_client.get_adress())
print(status_client.get_phone())
print(status_client.get_client_id())
print(status_client.get_subscribe_status())

