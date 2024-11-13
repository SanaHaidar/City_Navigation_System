class CityNavigation:
    def __init__(self):

        self.city_map = {}

    def add_city(self, city):

        if not isinstance(city, str) or not city:
            raise ValueError("City name must be a non-empty string")
        if city not in self.city_map:
            self.city_map[city] = []

    def add_road(self, city1, city2):
        if city1 not in self.city_map:
            self.add_city(city1)
        if city2 not in self.city_map:
            self.add_city(city2)

        if city2 not in self.city_map[city1]:
            self.city_map[city1].append(city2)
        if city1 not in self.city_map[city2]:
            self.city_map[city2].append(city1)

    def display_map(self):
        print("City Map:")
        for city, neighbors in self.city_map.items():
            print(f"{city}: {', '.join(neighbors)}")

    def bfs_shortest_path(self, start, destination):
        if start == destination:
            return start, 0
        if start not in self.city_map or destination not in self.city_map:
            return None, f"One or both cities are not in the city map."

        queue = [(start, None)]
        visited = set()
        predecessors = {}

        while queue:
            current, before = queue.pop(0)
            if current in visited:
                continue

            visited.add(current)
            predecessors[current] = before

            if current == destination:
                path = []
                while current is not None:
                    path.append(current)
                    current = predecessors[current]
                return path[::-1], len(path) - 1  #

            for neighbor in self.city_map[current]:
                if neighbor not in visited:
                    queue.append((neighbor, current))

        return f"No path found from {start} to {destination}."


navigation = CityNavigation()

navigation.add_city("Beirut")
navigation.add_city("Jbeil")
navigation.add_road("Beirut", "Jbeil")
navigation.add_road("Jbeil", "Akkar")

navigation.display_map()

path, length = navigation.bfs_shortest_path("Beirut", "Akkar")
print(f"Shortest path: {path}, Length: {length}")
