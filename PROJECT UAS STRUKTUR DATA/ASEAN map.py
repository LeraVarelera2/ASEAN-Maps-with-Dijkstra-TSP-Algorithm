import heapq
from itertools import permutations

print("""Daftar Negara ASEAN:
1. indonesia
2. brunei
3. kamboja
4. laos
5. malaysia
6. myanmar
7. filipina
8. singapura
9. thailand
10. vietnam""")

# Variabel negara (simpul) 
ind  = "indonesia"
brn  = "brunei"
khm  = "kamboja"
lao  = "laos"
mal  = "malaysia"
myan = "myanmar"
phl  = "filipina"
sgp  = "singapura"
tha  = "thailand"
vnm  = "vietnam"

# Graph (peta jarak antar negara) 
graph = {
    ind: {sgp: 863, brn:1300, mal:1369},
    brn: {ind: 100, sgp:1301, khm:1414, phl:1259},
    khm: {mal: 1029, vnm:421, brn:1505, tha:527, sgp:1295, phl: 1942},
    lao: {myan: 686, vnm: 837, tha: 425},
    mal: {ind:1369, sgp: 411, khm: 1071},
    myan: {lao: 686, tha: 857},
    phl: {brn: 1259, khm: 1942, vnm: 1625},
    sgp: {ind:863, mal:411, brn: 1301, khm: 1295},
    tha: {myan: 857, lao: 425, khm: 527, vnm: 730},
    vnm: {khm: 421, lao: 837, tha: 730, phl: 1625}
}

# Dijkstra : Cari jarak terpendek antar negara
def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        if node == end:
            return (cost, path)
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    return float("inf"), []

# A* Search: Rute tercepat dengan heuristik 
heuristic = {
    ind: 1000, brn: 800, khm: 400, lao: 500, mal: 300,
    myan: 600, phl: 700, sgp: 200, tha: 350, vnm: 100
}

def astar(graph, start, end):
    queue = [(0 + heuristic[start], 0, start, [])]
    visited = set()
    while queue:
        (est_total, cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        if node == end:
            return (cost, path)
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                est_cost = cost + weight + heuristic[neighbor]
                heapq.heappush(queue, (est_cost, cost + weight, neighbor, path))
    return float("inf"), []

# TSP : Kunjungi semua kota sekali
def tsp(graph, start):
    cities = list(graph.keys())
    cities.remove(start)
    min_cost = float('inf')
    best_path = []
    for perm in permutations(cities):
        path = [start] + list(perm) + [start]
        cost = 0
        valid = True
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            if v in graph[u]:
                cost += graph[u][v]
            else:
                valid = False
                break
        if valid and cost < min_cost:
            min_cost = cost
            best_path = path
    return min_cost, best_path


# Input dan Pemanggilan Algoritma
awal = input("Masukkan negara awal: ").lower()
akhir = input("Masukkan negara akhir: ").lower()

print("\n--- Dijkstra ---")
total_cost, route = dijkstra(graph, awal, akhir)
print(f"Jalur: {' -> '.join(route)}")
print(f"Total jarak: {total_cost} km")

print("\n--- A* Search ---")
a_cost, a_route = astar(graph, awal, akhir)
print(f"Jalur: {' -> '.join(a_route)}")
print(f"Total jarak: {a_cost} km")

print("\n--- TSP ---")
tsp_cost, tsp_path = tsp(graph, awal)
print(f"Rute: {' -> '.join(tsp_path)}")
print(f"Total jarak: {tsp_cost} km")


