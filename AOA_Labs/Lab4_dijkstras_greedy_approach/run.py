# implementing Dijkstra's algorithm of single source shortest
# path using greedy approach
import copy


# Assuming vertex numbers :  0,1,2,3,4

def initialise(number_of_vertices):
    # assuming 0 is the starting vertex
    # distance of starting vertex from 0 is zero

    set_of_selected_vertices = set()

    distance_of_vertex_from_source_dictionary = {0: 0}
    for i in range(1, number_of_vertices):
        distance_of_vertex_from_source_dictionary[i] = None

    print("Assuming starting vertex is zero and all existing vertex numbers : 0,1,2,3,4 ", end="\n\n")
    print("Initial distances of vertices from starting vertex:")
    print(distance_of_vertex_from_source_dictionary, end="\n\n")

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

    print("The initial adjacency matrix of the directed graph is : ")
    for row in weighted_directed_graph_adjacency_matrix:
        print(row)

    print("\nNote : None is used to denote infinity", end="\n")
    return (
        set_of_selected_vertices, distance_of_vertex_from_source_dictionary, weighted_directed_graph_adjacency_matrix)


def select_vertex(set_of_selected_vertices, distance_of_vertex_from_source_dictionary,
                  weighted_directed_graph_adjacency_matrix, number_of_vertices):
    distance_of_vertex_from_source_dictionary_copy = copy.deepcopy(distance_of_vertex_from_source_dictionary)

    for i in range(0, number_of_vertices):
        if distance_of_vertex_from_source_dictionary[i] is None:
            distance_of_vertex_from_source_dictionary_copy.pop(i)

    # distance_of_vertex_from_source_dictionary_copy contains vertex and their distances from source
    # for only those vertices whose distance from source is not None

    while True:
        vertex = min(distance_of_vertex_from_source_dictionary_copy,
                     key=distance_of_vertex_from_source_dictionary_copy.get)

        if vertex in set_of_selected_vertices:
            distance_of_vertex_from_source_dictionary_copy.pop(vertex)
            continue
        else:
            return vertex


def dijkstras_algorithm(set_of_selected_vertices, distance_of_vertex_from_source_dictionary,
                        weighted_directed_graph_adjacency_matrix, number_of_vertices):
    # selecting 0 vertex at the start
    set_of_selected_vertices.add(0)
    for i in range(1, number_of_vertices):
        distance_of_vertex_from_source_dictionary[i] = weighted_directed_graph_adjacency_matrix[0][i]

    print("\n")
    print("Below is the distance(value) of vertex(Key) from source (dictionary) for each iteration :", end="\n\n")

    print("On selecting vertex 0")
    print("Set of selected vertices are : ", set_of_selected_vertices)
    print("Distances of vertices from source vertex are : ")
    print(distance_of_vertex_from_source_dictionary)

    # selecting each vertex of the graph:
    for i in range(1, number_of_vertices):
        # the vertex which is at minimum distance from the starting vertex is selected
        selected_vertex = select_vertex(set_of_selected_vertices, distance_of_vertex_from_source_dictionary,
                                        weighted_directed_graph_adjacency_matrix, number_of_vertices)

        set_of_selected_vertices.add(selected_vertex)
        for j in range(0, number_of_vertices):
            # if there is no path from selected vertex to given vertex then continue to next vertex
            if weighted_directed_graph_adjacency_matrix[selected_vertex][j] is None:
                continue

            # if there is a path from selected vertex to given vertex
            else:
                # if the path of given vertex from source is current infinity
                if distance_of_vertex_from_source_dictionary[j] is None:
                    distance_of_vertex_from_source_dictionary[j] = distance_of_vertex_from_source_dictionary[
                                                                       selected_vertex] + \
                                                                   weighted_directed_graph_adjacency_matrix[
                                                                       selected_vertex][j]

                # if the path of given vertex from source is not infinity but is greater than d[u] + w(w,v)
                elif distance_of_vertex_from_source_dictionary[selected_vertex] + \
                        weighted_directed_graph_adjacency_matrix[selected_vertex][j] < \
                        distance_of_vertex_from_source_dictionary[j]:

                    distance_of_vertex_from_source_dictionary[j] = distance_of_vertex_from_source_dictionary[
                                                                       selected_vertex] + \
                                                                   weighted_directed_graph_adjacency_matrix[
                                                                       selected_vertex][j]
        print("\nOn selecting vertex : ", selected_vertex)
        print("Set of selected vertices are : ", set_of_selected_vertices)
        print("Distances of vertices from source vertex are : ")
        print(distance_of_vertex_from_source_dictionary, end="\n\n")

    print("\nThus the final single source shortest path is : ")
    for key in distance_of_vertex_from_source_dictionary:
        print("Distance of ", key, " from source vertex is : ", distance_of_vertex_from_source_dictionary[key],
              end="\n\n")


def main():
    number_of_vertices = 5
    set_of_selected_vertices, distance_of_vertex_from_source_dictionary, weighted_directed_graph_adjacency_matrix = initialise(
        number_of_vertices)

    dijkstras_algorithm(set_of_selected_vertices, distance_of_vertex_from_source_dictionary,
                        weighted_directed_graph_adjacency_matrix, number_of_vertices)


if __name__ == "__main__":
    main()
