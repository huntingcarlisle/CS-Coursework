# Prints form letters based on hard-coded string values organized in a list of tuples.

# List of tuples containing string value for sender, cnadidate, and addressee
letters = [("Hildegard", "Hillary Clinton", "Brunhilda"), ("Cheech", "Donald Trump", "Chong"), ("Moe", "Bernie Sanders", "Jack")]

# output Form letters
for formTuple in letters:
    print()
    print ("Dear %s,\nI would like you to vote for %s\nbecause I think %s is best for\nthis country.\nSincerely,\n%s" % (formTuple[0], formTuple[1], formTuple[1], formTuple[2]))
    print()

"""
~/workspace/PythonClass/ $ python hcarlisle_assignment2.py

Dear Hildegard,
I would like you to vote for Hillary Clinton
because I think Hillary Clinton is best for
this country.
Sincerely,
Brunhilda


Dear Cheech,
I would like you to vote for Donald Trump
because I think Donald Trump is best for
this country.
Sincerely,
Chong


Dear Moe,
I would like you to vote for Bernie Sanders
because I think Bernie Sanders is best for
this country.
Sincerely,
Jack

"""