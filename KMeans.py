def calculate_distance(dx, dy, cx, cy): # this will calculate the distance between points
    first = (dx - cx) ** 2 + (dy - cy) **2 
    if first == 0:
        return 0
    last_guess= first/2.0
    while True:
        guess= (last_guess + first/last_guess)/2
        if abs(guess - last_guess) < .00000000001:
            return guess
        last_guess= guess

def assign_clusters(datapoints, centroids):
    clusters = {key: [] for key in range(len(centroids))}  
    for point in datapoints:
        x, y = point

        closest = min(range(len(centroids)), key=lambda i: calculate_distance(x, y, centroids[i][0], centroids[i][1]))
        clusters[closest].append(point)
    return clusters


def calculate_new_centroids(clusters, old_centroids):
    new_centroids = []
    for cluster in clusters.values():
        if cluster: 
            x_avg = sum(p[0] for p in cluster) / len(cluster)
            y_avg = sum(p[1] for p in cluster) / len(cluster)
            new_centroids.append([x_avg, y_avg])
        else:
            new_centroids.append(old_centroids[len(new_centroids)])  
    return new_centroids


def KMeans(datapoints, k=3, max_iterations=100):

    centroids = [datapoints[i] for i in range(k)]
    
    for _ in range(max_iterations):

        clusters = assign_clusters(datapoints, centroids)


        new_centroids = calculate_new_centroids(clusters, centroids)


        if new_centroids == centroids:
            break  

        centroids = new_centroids 

    return centroids, clusters


datapoints = [
    [2,10], [2,5], [8,4], [5,8], 
    [7,5], [6,4], [1,2], [4,9]
]


final_centroids, final_clusters = KMeans(datapoints)

# Output results
print("Final Centroids:", final_centroids)
for cluster_id, points in final_clusters.items():
    print(f"Cluster {cluster_id + 1}: {points}")