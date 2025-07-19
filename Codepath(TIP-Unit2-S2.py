# Unit 2 - Session 2 (Set Version 2)
# Problem 1

#Understand
#We need a founction most_endangered(species_list), name, habitat, population
#There are 2 loops for indexes-key and key-value

def most_endangered(species_list):

    name = species_list[0]["name"]
    lowest = species_list[0]["population"]
    for species in species_list[1:]:
        if species["population"] < lowest:
            lowest = species["population"]
            name = species["name"]
    return name
 


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 90
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 10
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 99
    }
]

print(most_endangered(species_list))
print("-" * 50)

#------------------------------------------------------------------------------------------------------------
# Problem 2

# We need to count the letters from endangered_species in observed_species.
# Return the count of the endangered species

def count_endangered_species(endangered_species, observed_species):

    endangered = set(endangered_species)

    Counter = 0 
    for species in observed_species:
        if species in endangered:
            Counter += 1
    return Counter


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2)) 
print("-" * 50)

#------------------------------------------------------------------------------------------------------------
# Problem 3

def navigate_research_station(station_layout, observations):

    total = 0
    curr_pos = 0

    for ch in observations:
        target_pos = station_layout.index(ch)
        total += abs(curr_pos - target_pos)
        curr_pos = target_pos
    return total



station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))
print("-" * 50)
#------------------------------------------------------------------------------------------------------------
# Problem 4

def prioritize_observations(observed_species, priority_species):

    result = [j for species in priority_species for j in observed_species if species == j]

    remaining = sorted([s for s in observed_species if s not in priority_species])
    
    result.extend(remaining)

    return result


observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 
