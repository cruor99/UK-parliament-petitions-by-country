import requests


class PetitionGrabber():
    def __init__(self, url):
        self.petitonurl = url

    def _grabJson(self):
        r = requests.get(str(self.petitonurl) + ".json")

        return r.json()

    def _grabCountries(self, data):
        countries = data["data"]["attributes"]["signatures_by_country"]

        return countries

    def _grabConstituencies(self, data):
        constituencies = data["data"]["attributes"][
            "signatures_by_constituency"]

        return constituencies

    def _sortBySigns(self, data):
        sortedlist = sorted(data,
                            key=lambda k: k["signature_count"],
                            reverse=True)

        return sortedlist

    def getCountriesBySignatures(self):
        sortedlist = []
        json = pg._grabJson()
        countries = pg._grabCountries(json)
        sortedcountries = pg._sortBySigns(countries)
        for country in sortedcountries:
            sortedlist.append((country["name"], country["signature_count"]))

        return sortedlist

    def getConstituenciesBySignatures(self):
        sortedlist = []
        json = pg._grabJson()
        constituencies = pg._grabConstituencies(json)
        sortedconstituencies = pg._sortBySigns(constituencies)
        for constituency in sortedconstituencies:
            sortedlist.append((constituency["name"], constituency[
                "signature_count"]))

        return sortedlist


if __name__ == "__main__":
    userinput = input("Plase input the URL to the petiton: ")
    pg = PetitionGrabber(url=userinput)

    countries = pg.getCountriesBySignatures()
    numberofvotes = 0
    for country in countries:
        print(country[0] + ": ", country[1])
        numberofvotes += country[1]

    print ("/nBy Constituencies:")
    constituencies = pg.getConstituenciesBySignatures()
    numberofconstituencyvotes = 0
    for constituency in constituencies:
        print(constituency[0] + ":", constituency[1])
        numberofconstituencyvotes += constituency[1]
    print("\n Number of votes by Country:", numberofvotes)
    print ("Number of votes by Constituency:", numberofconstituencyvotes)
    print("Total number of votes:", numberofvotes + numberofconstituencyvotes)
