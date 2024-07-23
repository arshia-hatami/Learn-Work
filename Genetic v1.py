import random


def sazgari_function(x):
    return x ** 2


def generate_prime_population(size, x_min, x_max):
    return [random.uniform(x_min, x_max) for i in range(size)]


def selection(population, sazgari):
    toatal_sazgari = sum(sazgari)
    pick = random.uniform(0, toatal_sazgari)
    current = 0
    for i, sazgari in enumerate(sazgari):
        current += sazgari
        if current > pick:
            return population[i]


def tarkib(parent1, parent2):
    farzand = random.uniform(0, 1)
    return farzand * parent1 + (1 - farzand) * parent2


def jahesh(individuals, jahesh_rate, x_min, x_max):
    if random.uniform(0, 1) < jahesh_rate:
        return random.uniform(x_min, x_max)
    return individuals


def genetic_algorithm(sazgari_function, populatin_size, generations, jahesh_rate, x_min, x_max):
    populatin = generate_prime_population(populatin_size, x_min, x_max)

    for generation in range(generations):
        sazgari = [sazgari_function(individual) for individual in populatin]

        new_population = []
        for _ in range(populatin_size):
            parent1 = selection(populatin, sazgari)
            parent2 = selection(populatin, sazgari)
            offspring = tarkib(parent1, parent2)
            offspring = jahesh(offspring, jahesh_rate, x_min, x_max)
            new_population.append(offspring)

        populatin = new_population

    sazgari = [sazgari_function(individual) for individual in populatin]
    best_individual = populatin[sazgari.index(max(sazgari))]

    return best_individual


population_size = 20
generations = 50
sazgari_rate = 0.01
x_max = 10
x_min = -10

best_gen = genetic_algorithm(sazgari_function, population_size, generations, sazgari_rate, x_min, x_max)
print("best solution is: ", best_gen)
print("sazgari for best solution is: ", sazgari_function(best_gen))

