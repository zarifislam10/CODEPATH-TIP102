# Problem 1

def filter_meme_lengths(memes, max_length):
    result = []
    
    for word in memes:
        if len(word) <= max_length:
            result.append(word)               

    return result



memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]

print(filter_meme_lengths(memes, 20))
print(filter_meme_lengths(memes_2, 15))
print(filter_meme_lengths(memes_3, 10))
print( "-" * 50)

# Problem 2

def count_meme_creators(memes):
    creators = {}

    for meme in memes:
        if meme["creator"] not in creators:
            creators[meme["creator"]] = 1
        else:
            creators[meme["creator"]] += 1

    return creators

memes = [
    {"creator": "Alex", "text": "Meme 1"},
    {"creator": "Jordan", "text": "Meme 2"},
    {"creator": "Alex", "text": "Meme 3"},
    {"creator": "Chris", "text": "Meme 4"},
    {"creator": "Jordan", "text": "Meme 5"}
]

memes_2 = [
    {"creator": "Sam", "text": "Meme 1"},
    {"creator": "Sam", "text": "Meme 2"},
    {"creator": "Sam", "text": "Meme 3"},
    {"creator": "Taylor", "text": "Meme 4"}
]

memes_3 = [
    {"creator": "Blake", "text": "Meme 1"},
    {"creator": "Blake", "text": "Meme 2"}
]

print(count_meme_creators(memes))
print(count_meme_creators(memes_2))
print(count_meme_creators(memes_3))
print( "-" * 50)

# Problem 3

def find_trending_memes(memes):

    counter = {}
    res = []

    for meme in memes:
        counter[meme] = counter.get(meme, 0) + 1
         

    for key, value in counter.items():
        if value > 1:
            res.append(key)

    return res

memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(find_trending_memes(memes))
print(find_trending_memes(memes_2))
print(find_trending_memes(memes_3))
print( "-" * 50)

# Problem 4

def reverse_memes(memes):
        
    result = []

    for i in range(len(memes) - 1, -1, -1):
        result.append(memes[i])

    return result


memes = ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(reverse_memes(memes))
print(reverse_memes(memes_2))
print(reverse_memes(memes_3))
print( "-" * 50)

# Problem 5

def find_trending_meme_pairs(meme_posts):
    pair_count = {}

    for post in meme_posts:
        for i in range(len(post)):
            for j in range(len(post)):
                if i != j:
                    meme1 = post[i]
                    meme2 = post[j]

                    if meme1 < meme2:
                        meme1, meme2 = meme2, meme1
                    pair = (meme1, meme2)
                    if pair in pair_count:
                        pair_count[pair] += 1
                    else:
                        pair_count[pair] = 1

    trending_pairs = []
    for pair in pair_count:
        if pair_count[pair] >= 2:
            trending_pairs.append(pair)

    return trending_pairs


meme_posts_1 = [
    ["Dogecoin to the moon!", "Distracted boyfriend"],
    ["One does not simply walk into Mordor", "Dogecoin to the moon!"],
    ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"],
    ["Distracted boyfriend", "One does not simply walk into Mordor"]
]

meme_posts_2 = [
    ["Surprised Pikachu", "This is fine"],
    ["Expanding brain", "Surprised Pikachu"],
    ["This is fine", "Expanding brain"],
    ["Surprised Pikachu", "This is fine"]
]

meme_posts_3 = [
    ["Y U No?", "First world problems"],
    ["Philosoraptor", "Bad Luck Brian"],
    ["First world problems", "Philosoraptor"],
    ["Y U No?", "First world problems"]
]

print(find_trending_meme_pairs(meme_posts))
print(find_trending_meme_pairs(meme_posts_2))
print(find_trending_meme_pairs(meme_posts_3))