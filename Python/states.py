# states = ['california', 'Arizona', 'Arkansas']
# abbrv = ['CA', 'AZ', 'AK']
#
# for i in range(len(states)):
#     print("State: %s Abbrv %s" % (states[i], abbrv[i]))




# states = {
# "CA" : "California",
# "AZ" : "Arizona",
# "AK" : "Arkansas",
# }
#
# for state in states:
#     print(" %s is the abbreviation for %s" % (state, states[state]))


storePrices = {
    "cereal" : 2.00,
    "stapler" : 1.50,
    "fiber optic" : 25,
    "lambo" : 75000,

}

print(storePrices["cereal"]) + (storePrices["lambo"])


storeInventory = {
    "cereal" : 400,
    "stapler" : 50,
    "fiber optic" : 30,
    "lambo" : 3,

}

print(storePrices["cereal"]) + storePrices["cereal"] + storePrices["lambo"]

storeInventory["cereal"] -= 2
storeInventory["lambo"] -= 1


for item in storePrices :
    storePrices[item] *= 1.03

print(storePrices)
