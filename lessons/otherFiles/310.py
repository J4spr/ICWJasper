dictionaryception = {
    "Lucky": {"name": "Luke",
              "horse": "Blackie"
              },
    "Alexander": {"name": "The great",
                  "horse": "John"
                  },
    "sheriff": {
        "name": "Douglass",
        "horse": "Bigbutt"
    }
}
sortby = input("Wat wil je sorteren")


def incaseOfValue(sortby):
    valuelist = []
    for person in dictionaryception:
        personvalues = dictionaryception.get(person)
        value = personvalues.get(sortby)
        valuelist.append(value)

    sortedlist = sorted(valuelist)

    for value in sortedlist:
        for person in dictionaryception:
            if dictionaryception[person][sortby] == value:
                print(
                    f"het paard {dictionaryception[person]['horse']} werd bereden door {person} {dictionaryception[person]['name']}")


def inCaseOfKey(sortby):
    sorteddictionary = sorted(dictionaryception)

    for voornaam in dictionaryception:
        for person in dictionaryception:
            if person == voornaam:
                print(
                    f"het paard {dictionaryception[person]['horse']} werd bereden door {person, dictionaryception[person]['name']}")


if sortby == "voornaam":
    inCaseOfKey(sortby)
else:
    incaseOfValue(sortby)
