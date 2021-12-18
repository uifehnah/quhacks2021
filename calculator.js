function calculator(weight,mins_phys_activity){
	ounces = (weight * (2/3)) + ((12 * mins_phys_activity) / 30);
    liters =  ounces / 33.814;

    num_bottles = 2 * liters;

    return liters;
}




fs.writeFile('PLACEHOLDER.txt', calculator(INPUT, INPUT), (err) => {
      
    // In case of a error throw err.
    if (err) throw err;
})