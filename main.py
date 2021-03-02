from app import Resident

resident = Resident(name='Harry', age='30', id=21)

resident.print_name()
resident.print_age()
resident.print_id()


resident.title()
print(Resident.mro())