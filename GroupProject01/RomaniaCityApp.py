import json

from GroupAssignment1 import romania_map_data
from GroupAssignment1.SimpleProblemSolvingAgent import SimpleProblemSolvingAgent


def main():
    print("Welcome to the RomaniaCityApp.")

    data = getMapData()
    map_data = romania_map_data.UndirectedGraph(data["distances"])
    locations = data["locations"]

    again = True
    while again:
        twocities = inputCities(locations.keys())

        start_city = twocities[0]
        end_city = twocities[1]
        search_strategy = "bfs"

        problem = SimpleProblemSolvingAgent(map_data, locations)
        route = problem.search(start_city, end_city, search_strategy)

        if route is not None:
            print("Route found: ", route)
        else:
            print("Route not found.")

        again = input("Again? Yes/No ")
        if again.lower() == "yes":
            again = True
        elif again.lower() == "no":
            again = False


def getMapData():
    notfound = True
    while notfound:
        print("Where is the map file in your local directory?")
        path = input()
        try:
            with open(path) as f:
                data = f.read()
        except:
            print("File not found try again")
            notfound = True
        else:
            notfound = False

    print("Map file found!")

    return json.loads(data)


def inputCities(locations):
    again = True
    while again:
        print("Input two cities from the map. Separate by a space.")
        twocities = input()
        cities = twocities.split()
        city1 = cities[0]
        city2 = cities[1]
        if city1 in locations and city2 in locations:
            again = False

    print("Cities are valid searching for best path!")
    return cities


if __name__ == "__main__":
    main()








