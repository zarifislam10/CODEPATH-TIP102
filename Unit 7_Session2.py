# Problem 1: Finding the Perfect Song
# Abby Lee of Dance Moms is looking for the perfect song to choreograph a group routine to and 
# needs a song of a specified length. Given a specific song length length and
#  a list of song lengths playlist sorted in ascending order, use the binary search algorithm to return 
#  the index of the song in playlist with length. 
# If no song with the target length exists, return -1.

# Example output
# 2
# -1

def find_perfect_song(playlist, length):
    left = 0
    right = len(playlist) - 1

    while left <= right:
        mid = (left + right) // 2
        if playlist[mid] == length:
            return mid
        elif playlist[mid] < length:
            left = mid + 1
        else:
            if playlist[mid] > length:
                right = mid - 1

    return -1


print(find_perfect_song([101, 102, 103, 104, 105], 103))
print(find_perfect_song([201, 202, 203, 204, 205], 206))

# Problem 2: Finding Tour Dates
# Your favorite artist is doing a short residency in your city 
# and you're hoping to attend one of their concerts! But because of school, 
# you're only free one day this month :( . Given a sorted list of integers tour_dates representing the days
# this month your favorite artist is playing, and an integer available representing the day you are available, 
# write a recursive function can_attend() that returns True if you will be able to attend one of their concerts
# (some date in tour_dates matches available) and False otherwise.

# Your solution must have O(log n) time complexity.

def can_attend(tour_dates, available):

    def binary_search(tour_dates, available, left, right):
        if left > right:
            return False
        
        mid = (left + right) // 2

        if tour_dates[mid] == available:
            return True
        elif tour_dates[mid] < available:
            return binary_search(tour_dates, available, mid + 1, right)
        else:
            return binary_search(tour_dates, available, left, mid - 1)
        
    return binary_search(tour_dates, available, 0, len(tour_dates)-1)
        
     

    # Base, if find available in tour_dates, return true
    # Repetition, search for


print(can_attend([1, 3, 7, 10, 12], 12))
print(can_attend([1, 3, 7, 10, 12], 5))
# Example Output:

# True
# False
