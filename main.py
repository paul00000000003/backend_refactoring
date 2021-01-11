__winc_id__ = '9920545368b24a06babf1b57cee44171'
__human_name__ = 'refactoring'


electricians = []
painters = []
plumbers = []

class Specialists:
    class electrician:
        def __init__(self, name, price):
            self.name = name
            if name in electricians:
                None
            else:
                electricians.append({"name": name, "price": price})

    class painter:
        def __init__(self, name, price):
            self.name = name
            if name in painters:
                None
            else:
                painters.append({"name": name, "price": price})

    class plumber:
        def __init__(self, name, price):
            self.name = name
            if name in plumbers:
                None
            else:
                plumbers.append({"name": name, "price": price})


class Homeowner:
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs

    def make_contracts(self):
        contracts = []
        for need in self.needs:
            professions = {"electrician": electricians,
                           "plumber": plumbers,
                           "painter": painters}
            professions_table = professions.get(need, "not applicable")
            if len(professions_table) == 1:
                contracts.append(professions_table[0]['name'])
            else:
                if len(professions_table) == 0:
                    print(f"Voor het beroep {need} is nog niemand opgevoerd")
                else:
                    indexPreferred = -1
                    min_price = 0
                    for profession in professions_table:
                        if indexPreferred == -1:
                            indexPreferred = 0
                            min_price = profession['price']
                        else:
                            if profession['price'] < min_price:
                                indexPreferred = professions_table.index(
                                    profession)
                    # Merk op dat index hier altijd groter of gelijk aan nul is
                    contracts.append(professions_table[indexPreferred])
        return contracts


alice = Specialists().electrician('Alice Aliceville', 0)


alfred = Homeowner('Alfred Alfredson', 'Alfredslane 123',
                   ['painter', 'plumber'])
for contract in alfred.make_contracts():
    print(contract)


"""
print("Alfred's contracts:", alfred_contracts)
print("Bert's contracts:", bert_contracts)
print("Candice's contracts:", candice_contracts)
"""
