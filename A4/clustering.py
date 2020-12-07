# COMP3651
# Assignment 4
# K-Means
# Logan DiAdams

import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

def show_image(image):
    plt.imshow(image.astype(np.uint8))
    plt.show()

def calc_distance(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    z = point1[2] - point2[2]
    return math.sqrt(x*x + y*y + z*z)

def find_clustered_points(data_values, centroid_list, K):
    print("Assigning points...")
    result = [[] for i in range(K)]
    for data in data_values:
        smallest = -1.0
        chosen_idx = -1
        for idx, centroid in enumerate(centroid_list):
            distance = calc_distance(data, centroid)
            if (smallest == -1 or distance < smallest):
                smallest = distance
                chosen_idx = idx
        result[chosen_idx].append(data)
    return result

def update_centroids(centroid_list, clustered_points, K):
    print("Updating centroids...")
    for cluster in range(K):
        points_cnt = len(clustered_points[cluster])
        if (points_cnt == 0):
            continue
        centroid_list[cluster] = [0, 0, 0]
        for point in clustered_points[cluster]:
            for idx in range(len(point)):
                centroid_list[cluster][idx] += point[idx]
        for idx in range(len(centroid_list[cluster])):
            centroid_list[cluster][idx] /= points_cnt

def run_k_means(img_name, K, iterations):
    # Read grayscale image
    image = cv2.imread(img_name, cv2.IMREAD_UNCHANGED)
    image = cv2.cvtColor(image, cv2.IMREAD_GRAYSCALE)

    # Extract (x, y, brightness) from the image
    data_values = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            data_values.append([i, j, image[i, j, 0]])
    data_values = np.float32(data_values)
    print("Data Values shape:")
    print(data_values.shape)
    print("Data Values:")
    print(data_values)

    # K-Means Algorithm
    centroid_list = []
    print("Initializing Centroids...")
    for i in range(K):
        centroid_list.append([
            np.random.randint(image.shape[0]),
            np.random.randint(image.shape[1]),
            np.random.randint(256)
        ])

    for i in range(iterations):
        print(f"Running Iteration #{i}...")
        clustered_points = find_clustered_points(data_values, centroid_list, K)
        if (i + 1 < iterations):
            update_centroids(centroid_list, clustered_points, K)

    print("Creating image visualization...")
    image_data_list = []
    id_counter_list = [0] * K
    for data in data_values:
        for cluster in range(K):
            id_counter = id_counter_list[cluster]
            if (id_counter < len(clustered_points[cluster]) and np.array_equal(data, clustered_points[cluster][id_counter])):
                alpha = round(centroid_list[cluster][2])
                image_data_list.append([alpha, alpha, alpha, 255])
                id_counter_list[cluster] += 1
                break

    print("Final Centroid List:")
    print(np.array(centroid_list))
    image_data_list = np.array(image_data_list)
    segmented_image = image_data_list.reshape((image.shape))
    show_image(segmented_image)

def main():
    print("------------------")
    print("K-Means Clustering")
    print("------------------")
    img_name = input("Image name: ")
    K = int(input("K: "))
    iterations = int(input("Number of iterations: "))
    run_k_means(img_name, K, iterations)

if __name__ == "__main__":
    main()
