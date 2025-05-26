import heapq

# note: membuat variabel negara
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



graph = {
    ind: {sgp: 863, brn:1300, mal:1369, mal:1369},
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

awal = input("Masukkan kota awal: ").lower()
akhir = input("Masukkan kota akhir: ").lower()

total_cost, route = dijkstra(graph, awal, akhir)

print(f"kota yang dilalui dari {awal} ke {akhir}: {' -> '.join(route)}")
print(f"Total jarak tempu dari {awal} ke {akhir}: {total_cost} km")