# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))
"""faiqua fatima changed ("Greetings! What is your year of origin? ')) to 
(("Greetings! What is your year of origin? ")), "==" to "=" & added paranthesis after int() """

if year <= 1900: #faiqua fatima added ":"
    print ("Woah, that's the past!") #faiqua fatima fixed the quotations
elif year >1900 and year <= 2020: #faiqua fatima removed an extra "&", changed it to "and" and changed <2020 to <=2020
    print ("That's totally the present!")
else:# faiqua fatima changed elif to else
    print ("Far out, that's the future!!")
