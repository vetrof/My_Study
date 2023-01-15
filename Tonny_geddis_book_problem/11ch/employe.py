from objects import employe_production

supervisor_info = employe_production.ShiftSupervisor('вася', 984, 123, 5567)

print(supervisor_info.get_name())
print(supervisor_info.get_id())
print(supervisor_info.get_year_rate())
print(supervisor_info.get_year_bonus())



