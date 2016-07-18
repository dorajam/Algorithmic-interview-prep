# Dora Jambor
# interview cake prep
# write a function that takes some meetings scheduled and gives you a condensed overview of when the meetings are happening.

def condense_meetings(schedule):
    res = []

    schedule = sorted(schedule)   # O(n * logn)

    curr_meeting = schedule[0]
    start = curr_meeting[0]
    end = curr_meeting[1]

    for e in schedule:
        if e == curr_meeting:
            continue
        if e[0] <= end:
            if e[1] > end:
                end = e[1]
        else:
            res.append((start, end))
            start = e[0]
            end = e[1]
    res.append((start,end))
    return res

# TEST 
##################
# schedule = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
schedule =  [(1, 10), (2, 6), (3, 5), (7, 9)]
print condense_meetings(schedule)
        
