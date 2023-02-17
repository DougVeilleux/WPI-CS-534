import json
import os

import romania_map_data
import SimpleProblemSolvingAgent


def main():
    print('=====================================')
    print("Welcome to the RomaniaCityApp.\n")

    data = getMapData()
    map_data = romania_map_data.UndirectedGraph(data["distances"])
    locations = data["locations"]

    print("List of Cities:")
    print(map_data.nodes())
    print()

    again = True
    while again:
        twocities = inputCities(locations.keys())

        start_city = twocities[0]
        end_city = twocities[1]

        problem = SimpleProblemSolvingAgent.SimpleProblemSolvingAgent(map_data, locations)
        routeBFS = problem.search(start_city, end_city, 'BFS')
        routeASTAR = problem.search(start_city, end_city, 'ASTAR')

        if routeBFS is not None:
            print("Route found using BFS: ", routeBFS)
        else:
            print("Route not found using BFS.")

        if routeASTAR is not None:
            (came_from, cost_so_far) = routeASTAR
            routeASTAR = problem.reconstruct_path(came_from, start_city, end_city)
            print("Route found using ASTAR: ", routeASTAR)
        else:
            print("Route not found using ASTAR.")

        again = input("Again? Yes/No ")
        if again.lower() == "yes":
            again = True
        elif again.lower() == "no":
            print("Thank you for using the RomaniaCityApp!")
            again = False


def getMapData():
    notfound = True
    while notfound:
        print("Where is the map file in your local directory?")
        print("Example Syntax (windows): C:\\Users\\User\\Documents\\mapdata.txt")
        print("Example Syntax (mac): /Users/...Project01/mapdata.txt")
        # path = input()
        # path = "/Users/dougveilleux/Documents/GitHub/CS-534/WPI-CS-534/GroupProject01/mapdata.txt"
        cwd = os.getcwd()
        path = os.path.join(cwd, "mapdata.txt")
        try:
            with open(path) as f:
                data = f.read()
        except:
            print("File not found try again")
            notfound = True
        else:
            notfound = False

    print("Map file found!\n")

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

    print("\nCities are valid...searching for best path!")
    return cities


if __name__ == "__main__":
    main()



