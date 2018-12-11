class RockGuitars():
    def __init__(self, guitarist="", guitar=""):
        self.guitar = guitar
        self.guitarist = guitarist
    
    def set_entry(self, guitarist, guitar=""):
        self.guitar = guitar
        self.guitarist = guitarist

    def __str__(self):
        return '{:<20s} {:<20s}'.format(self.guitarist, self.guitar)


g1 = RockGuitars()
g1.set_entry("Jimmy Page", "Gibson Les Paul Standard")
g2 = RockGuitars()
g2.set_entry("Angus Young", "Jaydee SG")
g3 = RockGuitars("Mark Knoppfler")
print(g1)
print(g2)
print(g3)