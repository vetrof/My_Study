total_second = 10123

hours = total_second // 3600

minutes = (total_second // 60) % 60

seconds = total_second % 60


print(hours)
print(minutes)
print(seconds)