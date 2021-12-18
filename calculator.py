import sys 


weight = int(sys.argv[1])
mins = int(sys.argv[2])



def liters_of_water(weight,mins_phys_activity):
    ounces = (weight * (2/3)) + ((12 * mins_phys_activity) / 30)
        
    liters =  ounces / 33.814

    num_bottles = 2 * liters

    return str(liters) + " liters of water or...\n" + "about " + str(num_bottles) + " bottles of water."



print(liters_of_water(weight,mins))

