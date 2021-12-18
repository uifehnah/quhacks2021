import sys 


weight = int(sys.argv[1])
mins = int(sys.argv[2])



def liters_of_water(weight,mins_phys_activity):
        ounces = (weight * (2/3)) + ((12 * mins_phys_activity) / 30)
        
    liters =  ounces / 33.814

    num_ bottles = 2 * liters

    return liters + " liters of water or...\n" + "about " + num_bottles + " bottles of water."


if __name__ == "main":
    liters_of_water(weight,mins)

