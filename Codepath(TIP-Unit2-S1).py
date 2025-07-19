# Unit 2: Session 1 (Set Version 1)

def lineup(artists, set_times):

    new_dict = {}
    for i in range(len(artists)):
        new_dict[artists[i]] = set_times[i]
    return new_dict
    # return (dict(zip(artists, set_times)))                               
            
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
print("-" * 50)

#----------------------------------------------------------------------------------
def get_artist_info(artist, festival_schedule):
    
    message = {'message' : 'Artist not found'}
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return message

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
print("-" * 50)

#----------------------------------------------------------------------------------

def total_sales(ticket_sales):
    #return sum(ticket_sales.values())

    total = 0
    for value in ticket_sales.values():
        total += value
    return total



ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
print(total_sales(ticket_sales))
print("-" * 50)

#----------------------------------------------------------------------------------

def identify_conflicts(venue1_schedule, venue2_schedule):

    conflicts = {}
    
    for venue in venue1_schedule:
        if venue in venue2_schedule and venue1_schedule[venue] == venue2_schedule[venue]:
            conflicts[venue] = venue1_schedule[venue]
    return conflicts



venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
print("-" * 50)
#----------------------------------------------------------------------------------

def best_set(votes):

    counter = {}
    for i in votes.values():
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    return max(counter, key= counter.get)

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
print("-" * 50)
#----------------------------------------------------------------------------------


def max_audience_performances(audiences):

    max_aud = max(audiences)
    max_count = audiences.count(max_aud)
    return max_aud * max_count



audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
print("-" * 50)

#----------------------------------------------------------------------------------

def max_audience_performances(audiences):

    counter = {}
    for i in audiences:
        counter[i] = counter.get(i, 0) + 1
    max_key = max(counter)
    return max_key * counter[max_key]
  


audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
print(25 * "-" + "Problem-8 " + "-" * 25)


def encode(strs: list[str]) -> str:
    
    result = []
    return result.append(" ".join(strs))

def decode(s: str) -> list[str]:
    result2 = s.split(",")
    return result2


strs = ["neet","code","love","you"]
strs1 = encode(strs)
strs2 = decode(strs1)
print(strs2)
