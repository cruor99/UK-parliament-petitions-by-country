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

    def _sortCountries(self, data):
        sortedlist = sorted(data, key=lambda k: k["signature_count"], reverse=True)

        return sortedlist

    def getCountriesBySignatures(self):
        sortedlist = []
        json = pg._grabJson()
        countries = pg._grabCountries(json)
        sortedcountries = pg._sortCountries(countries)
        for country in sortedcountries:
            sortedlist.append((country["name"], country["signature_count"]))

        return sortedlist


if __name__ == "__main__":
    userinput = input("Plase input the URL to the petiton: ")
    pg = PetitionGrabber(url=userinput)

    countries = pg.getCountriesBySignatures()
    for country in countries:
        print(country[0]+": ", country[1])
