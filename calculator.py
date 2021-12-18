import sys 

weight = int(sys.argv[1])
mins = int(sys.argv[2])


def liters_of_water(weight,mins_phys_activity):
    ounces = (weight * (2/3)) + ((12 * mins_phys_activity) / 30)
    
    return ounces / 33.814

liters = liters_of_water(weight,mins)
num_ bottles = 2 * liters

print(liters + " liters of water or...\n")
print("about " + num_bottles + " bottles of water.")


#test
