import os
import sys


class Node:

    def __init__(self, data, idx=None):
        self.data = data
        self.index = idx


class serverGraph:

    def __init__(self, n, m, nodes=None):
        """
        Create the adjency graph for server with n rows and m columns
        :param n: no of rows
        :param m: no of colms
        :param nodes: Node objects from the ncde class
        """
        # Create the adjency matrix
        self.adj_matrix = [[0] * m for _ in range(n)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    @classmethod
    def create_graph_from_nodes(self, nodes):
        """
        This returns the class object of graph. Basically calls the internal function __init__ which initializes
        the graph with n rows and m columns for us
        :param nodes: list of node objects
        :return: Graph Object (serverGraph)
        """
        return serverGraph(len(nodes), len(nodes), nodes)

    def node(self, index):
        return self.nodes[index]

    def get_index_from_node(self, node):
        """
        Gets the index of the node from the server graph. Internal function
        :param node: node object
        :return: index of the node
        """
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("Incorrent dtype of node. Please check!")
        if isinstance(node, int):
            return node
        else:
            return node.index

    def connect_graph_nodes(self, node1, node2, val=1):
        """
        Connect the nodes in the graph with the given value
         ** IMP its a directed graph. hence node1->node2 is not equal to node2->node1
        :param node1: node object 1
        :param node2: node object 2
        :param val: ping time of the server from node1 to node2
        :return: None
        """
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_matrix[node1][node2] = val

    def draw_graph(self, node1, node2, val=1):
        """
        Wrapper to connect funtion
        :param node1: node object 1
        :param node2: node object 2
        :param weight:
        :return:
        """
        self.connect_graph_nodes(node1, node2, val)

    def connections_from(self, node):
        """
        Get the connections of the servers from the current server node
        :param node: node object
        :return: list of tuples of the connections
        """
        node = self.get_index_from_node(node)
        return [(self.nodes[col], self.adj_matrix[node][col]) for col in range(len(self.adj_matrix[node]))
                if self.adj_matrix[node][col] != 0]

    def connections_to(self, node):
        """
        Get the connections of the servers to the current server node
        :param node: node object
        :return: list of tuples of connections
        """
        node = self.get_index_from_node(node)
        column = [row[node] for row in self.adj_matrix]
        return [(self.nodes[row_num], column[row_num]) for row_num in range(len(column)) if column[row_num] != 0]

    def is_server_closed(self):
        """
        Check if the server is closed, i.e if all the nodes have to and from connections
        :return: bool
        """
        self.isolated_nodes = []
        for i in range(len(self.adj_matrix[0])):
            if sum(self.adj_matrix[i]) == 0:
                self.isolated_nodes.append(self.node(i).data)

        return len(self.isolated_nodes) == 0

    def print_graph(self):
        for row in self.adj_matrix:
            print(row)

    def shortest_path(self, node):
        """
        Use dijkstras algorithm to find the shortest path from source to all the servers
        :param node: soruce server node
        :return: list of tuples of connections and distance from source to all the servers
        """
        num_node = self.get_index_from_node(node)

        path = [None] * len(self.nodes)
        for i in range(len(path)):
            path[i] = [float("inf")]
            path[i].append([self.nodes[num_node]])

        path[num_node][0] = 0

        to_visit = [i for i in range(len(self.nodes))]
        visited = set()
        while len(to_visit) > 0:

            min_dist = float("inf")
            min_node = None
            for n in to_visit:
                if path[n][0] < min_dist and n not in visited:
                    min_dist = path[n][0]
                    min_node = n

            to_visit.remove(min_node)
            visited.add(min_node)
            connections = self.connections_from(min_node)

            for (node, weight) in connections:
                dist_total = weight + min_dist
                if dist_total < path[node.index][0]:
                    path[node.index][0] = dist_total
                    path[node.index][1] = list(path[min_node][1])
                    path[node.index][1].append(node)
        return path


def get_node(node_for):
    """
    Get the node object for given string value of node
    :param node_for: String data value of node
    :return: node object
    """
    for node in myServer:
        if node_for == node[0]:
            return node[1]


def output(to_write):
    """
    This function just writes the text given to it in the output file (output*.txt)
    :param to_write:
    :return: None
    """
    # print(to_write)
    outputFile = 'outputPS6.txt'
    with open(outputFile, 'a+') as outf:
        outf.write(to_write + "\n")


if __name__ == '__main__':
    # Initialize the Paths. Currently current folder is parent folder
    parentFolderPath = ''
    inputFileName = 'inputPS6.txt'
    outputFile = 'outputPS6.txt'

    # Clean the Output file if present
    if os.path.isfile(os.path.join(parentFolderPath, outputFile)):
        os.remove(os.path.join(parentFolderPath, outputFile))

    # Initialize global variables for
    myServer = []

    # ======================== Read the Input file to create a Binary Tree ==========================================
    try:
        with open(os.path.join(parentFolderPath, inputFileName), 'r') as input_file:
            lines = input_file.readlines()
            if len(lines) == 0:
                print('Input file is Empty! Please check')
            else:
                lines = [line.rstrip('\n') for line in lines]
                # print(lines)

                # Get the total number of servers and source from input file
                try:
                    number_of_servers = int(lines[0].split(" ")[-1])
                except:
                    print(f"Incorrect format for No of servers. Expected e.g 'No of servers: 5' ")
                    print(f"Exiting the program!")
                    sys.exit()
                try:
                    routing_table_server = lines[1].split(" ")[-1]
                except:
                    print(f"Incorrect routing table format. Expected e.g 'Routing Table for server A' ")
                    print(f"Exiting the program!")
                    sys.exit()

                # print(f"Number of servers = {number_of_servers}")
                # print(f"Routing table to be generaetd for server = {routing_table_server}")

                # Initialize global variables for
                servers_in_network = []  # list of string names of servers. ['A','B'...]
                connections = []  # list of tuples of connections [('A','B',60),...]

                for network in lines[2:]:
                    # route is in form "source <space> destination <space> time" hence split basis on space
                    # network = network.rstrip()    # remove rightmost spaces if any
                    route = network.split(" ")

                    # If length of split is not 3, there is some mistake in input
                    if len(route) != 3:
                        print(f"Incorrect input format. Please check the input line {route}")
                        print(f"Exiting the program!")
                        exit()

                    (source, destination, time) = route
                    connections.append((source, destination, time))

                    # Create a set of all servers to create nodes of the graph
                    if source not in servers_in_network:
                        servers_in_network.append(source)
                    if destination not in servers_in_network:
                        servers_in_network.append(destination)

                servers_in_network = sorted(servers_in_network)  # sort the servers for better viz
                # print(f"Total Servers in the Network are {len(servers_in_network)} : {servers_in_network}")

                if number_of_servers != len(servers_in_network):
                    print(
                        f"Total number of servers expected = {number_of_servers} "
                        f"but input connections contained {len(servers_in_network)} servers")
                    print(f"Please check the input file and connections!\nExiting the program")
                    exit()

    except FileNotFoundError:  # Handle the File not found error
        print('Input file not found! Please check')
        exit()
    except:  # Handle any other error
        print('Cannot Read input file! Please check')
        exit()

    # ================== Main code starts here: generating nodes and shortest route =================================

    # Create a Graph node for each server
    for server in servers_in_network:
        myServer.append((server, Node(server)))

    # Create the server routing Graph
    w_graph = serverGraph.create_graph_from_nodes([get_node(node[0]) for node in myServer])

    # Recheck the total servers from file and in graph
    if len(w_graph.adj_matrix[0]) != number_of_servers:
        print(
            f"Mismatch in total nodes in graph and total servers. Expected {number_of_servers} "
            f"in graph got {len(w_graph.adj_mat[0])}")
        print(f"Exiting the Program")
        exit(-1)

    # Connect the edges of the graph
    for conn in connections:
        w_graph.draw_graph(get_node(conn[0]), get_node(conn[1]), int(conn[2]))

    # Check for isolated nodes (servers) in the graph
    # w_graph.print_adj_mat()
    if not w_graph.is_server_closed():
        print(
            f"[Warning!]: One or more servers do not have 'to' and 'from' connections!")

    # Generate the routing table for the given server
    if not routing_table_server in servers_in_network:
        print(
            f"Source Server '{routing_table_server}' not present in given servers {servers_in_network}. Please check!")
        print(f"Exiting the program!")
        exit(-1)

    try:
        routing_table = w_graph.shortest_path(get_node(routing_table_server))
    except:
        print(f"Cannot find shortest route to all servers.")
        print(f"Probable reasons: 1. Disjoint Graph 2. Isolated Servers")
        print("Exiting the Program!")
        exit()

    # Traverse thru the routing table and write to output file
    for route in routing_table:
        ping_time = route[0]
        path = [n.data for n in route[1]]

        if path[-1] == routing_table_server:
            continue
        output_to_write = f"{path[-1]} {str(ping_time)}"
        output(output_to_write)
        # print(f"Ping Time = {ping_time} | Destination = {path[-1]} | Path = {path}")

    print(f"Program Successfully executed!")
