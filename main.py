__winc_id__ = '9920545368b24a06babf1b57cee44171'
__human_name__ = 'refactoring'


class electrician:
    def __init__(self, name, price):
        self.name = name
        if "electrician" in specialists:
            specialists["electrician"].append({"name": name, "price": price})
        else:
            specialists["electrician"] = [{"name": name, "price": price}]


class painter:
    def __init__(self, name, price):
        self.name = name
        if "painter" in specialists:
            specialists["painter"].append({"name": name, "price": price})
        else:
            specialists["painter"] = [{"name": name, "price": price}]


class plumber:
    def __init__(self, name, price):
        self.name = name
        if "plumber" in specialists:
            specialists["plumber"].append({"name": name, "price": price})
        else:
            specialists["plumber"] = [{"name": name, "price": price}]


def get_cheapest_specialist(needed_people):
    indexPreferred = -1
    min_price = 0
    for professional_person in needed_people:
        if indexPreferred == -1:
            indexPreferred = 0
            min_price = professional_person['price']
        else:
            if professional_person['price'] < min_price:
                indexPreferred = needed_people.index(professional_person)
    return


class Homeowner:
    def __init__(self, name, address, needs, specialists):
        self.name = name
        self.address = address
        self.needs = needs
        self.specialists = specialists

    def make_contracts(self):
        contracts = []
        print("specialists :"+specialists.__repr__())
        print(specialists['electrician'])

        for need in self.needs:
            if need in self.specialists:
                needed_people = self.specialists[need]
                if len(needed_people) == 1:
                    contracts.append(needed_people[0]['name'])
                elif len(needed_people) == 0:
                    print(f"Voor het beroep {need} is nog niemand opgevoerd")
                else:
                    desired_specialist = get_cheapest_specialist(needed_people)
                    contracts.append(desired_specialist['name'])
            else:
                print(f"there's no {need}")
        return contracts


specialists = {}

alice = electrician('Alice Aliceville', 0)
bob = painter('Bob Bobsville', 0)
craig = plumber('Craig Craigsville', 0)

alfred = Homeowner('Alfred Alfredson', 'Alfredslane 123',
                   ['painter', 'plumber'], specialists)
for contract in alfred.make_contracts():
    print("wanted person : "+contract)
