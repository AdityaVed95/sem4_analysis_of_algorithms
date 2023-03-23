# implementing Dijkstra's algorithm of single source shortest
# path using greedy approach

# Assuming vertex numbers :  0,1,2,3,4

def initialise(number_of_vertices):
    # assuming 0 is the starting vertex
    # distance of starting vertex from 0 is zero

    set_of_selected_vertices = set()

    distance_of_vertex_from_source_dictionary = {0: 0}
    for i in range(1, number_of_vertices):
        distance_of_vertex_from_source_dictionary[i] = None

    weighted_directed_graph_adjacency_matrix = [[None for i in range(number_of_vertices)] for j in
                                                range(number_of_vertices)]

    for i in range(number_of_vertices):
        weighted_directed_graph_adjacency_matrix[i][i] = 0

    weighted_directed_graph_adjacency_matrix[0][1] = 10
    weighted_directed_graph_adjacency_matrix[0][3] = 5
    weighted_directed_graph_adjacency_matrix[1][2] = 1
    weighted_directed_graph_adjacency_matrix[1][3] = 2
    weighted_directed_graph_adjacency_matrix[2][4] = 4
    weighted_directed_graph_adjacency_matrix[3][1] = 3
    weighted_directed_graph_adjacency_matrix[3][2] = 9
    weighted_directed_graph_adjacency_matrix[3][4] = 2
    weighted_directed_graph_adjacency_matrix[4][2] = 6
    weighted_directed_graph_adjacency_matrix[4][0] = 7

    for row in weighted_directed_graph_adjacency_matrix:
        print(row)

    return (
        set_of_selected_vertices, distance_of_vertex_from_source_dictionary, weighted_directed_graph_adjacency_matrix)


def dijkstras_algorithm(set_of_selected_vertices, distance_of_vertex_from_source_dictionary,
                        weighted_directed_graph_adjacency_matrix):
    print("hello")


def main():
    number_of_vertices = 5
    set_of_selected_vertices, distance_of_vertex_from_source_dictionary, weighted_directed_graph_adjacency_matrix = initialise(
        number_of_vertices)

    dijkstras_algorithm(set_of_selected_vertices, distance_of_vertex_from_source_dictionary,
                        weighted_directed_graph_adjacency_matrix)


if __name__ == "__main__":
    main()
