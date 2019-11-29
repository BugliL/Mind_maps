from graphviz import Digraph, render


def write_example_digraph(graph):
    graph.node(root_label)
    graph.edge(root_label, another_random_node)
    graph.save(file_name)


if __name__ == "__main__":
    another_random_node = 'Test_node'
    root_label = 'Root'
    file_name = "data/graph"

    graph = Digraph(format='png')
    graph.attr(rankdir='LR')
    #write_example_digraph(graph)

    render('dot', 'png', file_name)
