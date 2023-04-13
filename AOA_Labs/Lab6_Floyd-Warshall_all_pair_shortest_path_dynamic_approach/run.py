def initialise_adjacency_matrix(number_of_vertices: int):
    weighted_directed_graph_adjacency_matrix = [[float('inf') for i in range(number_of_vertices)] for j in
                                                range(number_of_vertices)]

    for i in range(number_of_vertices):
        weighted_directed_graph_adjacency_matrix[i][i] = 0

    weighted_directed_graph_adjacency_matrix[0][1] = 3
    weighted_directed_graph_adjacency_matrix[0][3] = 7
    weighted_directed_graph_adjacency_matrix[1][0] = 8
    weighted_directed_graph_adjacency_matrix[1][2] = 2
    weighted_directed_graph_adjacency_matrix[2][0] = 5
    weighted_directed_graph_adjacency_matrix[2][3] = 1
    weighted_directed_graph_adjacency_matrix[3][0] = 2

    print("Initial input matrix is : ")
    for row in weighted_directed_graph_adjacency_matrix:
        print(row)
    return weighted_directed_graph_adjacency_matrix


def main():
    number_of_vertices = 4
    weighted_directed_graph_adjacency_matrix = initialise_adjacency_matrix(number_of_vertices)

    k = 0

    j = 0

    while k < number_of_vertices:
        # The algorithm repeats this process for all possible intermediate nodes until all shortest paths have been
        # found. Once the algorithm has finished, the final table contains the shortest path between all pairs of
        # vertices in the graph.

        i = 0
        while i < number_of_vertices:
            j = 0
            while j < number_of_vertices:
                weighted_directed_graph_adjacency_matrix[i][j] = min(weighted_directed_graph_adjacency_matrix[i][j],
                                                                     weighted_directed_graph_adjacency_matrix[i][k] +
                                                                     weighted_directed_graph_adjacency_matrix[k][j])
                j += 1
            i += 1

        print("\n==================================\n")
        print("The Matrix after ", k + 1, "th iteration is : ")
        for row in weighted_directed_graph_adjacency_matrix:
            print(row)

        k += 1
    print("\n==================================\n ")

    print("Thus Final Output matrix of all pair shortest path is : ")
    for row in weighted_directed_graph_adjacency_matrix:
        print(row)


if __name__ == "__main__":
    main()
