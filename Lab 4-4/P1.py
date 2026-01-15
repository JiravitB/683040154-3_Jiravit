from room import Bedroom, Kitchen

bed = Bedroom(10,20,5)
print(bed.describe_room())
print(f"Bed size : {bed.bed_size} ft")
print(f"Reccommended lighting : {bed.get_recommended_lighting()} lumen / square foot ")
print()

K_no = Kitchen(15,25)
print("Kitchen with island")
print(K_no.describe_room())
print(f"Reccommended lighting : {K_no.get_recommended_lighting()} lumen / square foot ")
island1,wall1 = K_no.calculate_counter_space()
print(f"Counter space : Wall {wall1}, Island {island1}")
print()

K_yes = Kitchen(15,25,False)
print("Kitchen without island")
print(K_yes.describe_room())
print(f"Reccommended lighting : {K_yes.get_recommended_lighting()} lumen / square foot ")
island2,wall2 = K_yes.calculate_counter_space()
print(f"Counter space : Wall {wall2}, Island {island2}")
print()

print(K_yes.calculate_counter_space.__doc__)