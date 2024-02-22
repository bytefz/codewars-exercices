# What I send to Codewars
def rolldice_sum_prob(num, quant_dies):
    
    from itertools import combinations_with_replacement
    # Initialize local variables
    cont = 0
    LIST_VALUES = [1, 2, 3, 4, 5, 6]*quant_dies
    
    # All numbers for each die
    total_combinations = list(set(combinations_with_replacement(LIST_VALUES, quant_dies)))

    for combination in total_combinations:
        sum_total = sum(combination)
        # Count how many combinations are
        if sum_total == num:
            cont+=1
    
    prob = cont/pow(6,quant_dies)
    return prob



# When I refactor the code 

def rolldice_sum_prob_2(num, quant_dies):
    
    from itertools import product
    # Initialize local variables
    cont = 0
    numbers_die = [1, 2, 3, 4, 5, 6]
    
    for combination in product(numbers_die, repeat=quant_dies):
        
        if sum(combination) == num:
            cont+=1
    
    prob = cont/pow(6,quant_dies)
    return prob
    

#? What did I refactor?
#* I changed the use of the "combinations_with_replacement" function, since it had to do conversions.
#* These conversions, first to set and then to list, occurred because there were repeated values ​​and
#* convert them to set only returned the non-repeated values. It was a good solution, but I feel
#* which was not the best. Later, I would transform it to a list because I needed to work with that object.
#* It was a good solution, but it consumed more memory than was really needed, so much so that I had
#* two errors in CodeWars, due to the fact of the execution time of the program.
#* Refactoring:
#* This refactoring was done with two very clear ideas: avoid the use of object conversion and
#* avoid saving all those combinations of numbers in memory, since it was only necessary to iterate it.
#* That's why I used the itertools library's "product" function, which solved the first problem.
#* Second, I avoided using a variable and directly put the "product object" in the for iteration.
#* This, adding that the code looks better designed, has better performance than the previous one.

print(rolldice_sum_prob_2(35, 7))