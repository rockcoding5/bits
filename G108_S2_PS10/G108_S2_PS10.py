import os
import sys


class ShoppingCounter:
    def dummy(self):
        pass


if __name__ == '__main__':
    # Initialize the Paths. Current folder is parent folder
    parentFolderPath = ''
    inputFileName = 'inputPS10.txt'
    outputFile = 'outputPS10.txt'

    # Clean the Output file if present
    if os.path.isfile(os.path.join(parentFolderPath, outputFile)):
        os.remove(os.path.join(parentFolderPath, outputFile))

    # Read the Input file to create a Binary Tree ------------------------------------
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
    except :  # Handle any other error
        print('Cannot Read input file! Please check')
        exit()
