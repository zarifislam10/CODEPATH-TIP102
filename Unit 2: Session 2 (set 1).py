# Unit 2: Session 2 (Set Version 1)

# Problem 1

# Reschedule adds back the Cancelled string 
# Cancelled strings are stored in a stack, you pop it back in when Reschedule is inserted

def manage_stage_changes(changes):

    stack = []
    stored = []
    for s in changes:
        if "Schedule" in s:
            stack.append(s.split(" ")[1])
        elif "Cancel" == s:

            stored.append(stack.pop())
        else:
            if "Reschedule" in s:
                stack.append(stored.pop())

    return stack

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
print("-" * 50)
    
# Problem 2

def process_performance_requests(requests):
    
    return sorted(requests, reverse=True)

['Music', 'Dance', 'Drama']
['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']

print("-" * 50)



nums = [100, 4, 200, 1, 3, 2]
visited = set(nums)
result = sorted(visited)

print(result)