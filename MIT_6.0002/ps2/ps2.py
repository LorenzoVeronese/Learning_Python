# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time: Started: 14/11/20
#       Finished: 22/11/20 (ci ho lavorato almeno 1/2 ore quasi tutti i giorni)

#
# Finding shortest paths through MIT buildings
#
import unittest
import copy
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer: nodes are buildings, edges are the direct path from one building to another, distances are both the total
#         distance (first argument) and the outdoor distance
#

'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
NB A LIVELLO DI TEST, SEMBRA CHE NON SIA GIUSTO. CI SONO UN PAIO DI ERRORI STR == NAME MA PER IL RESTO SE GUARDI LA PRIMA PARTE
DELL'OUTPUT (QUANDO RUNNI IL CODICE) VEDI CHE I PATH TROVATI COINCIDONO.
MI SONO ACCORTO DOPO GIORNI DI DEBUG CHE IL CODICE RESTITUIVA UN PATH CORRETTO, MA IL PRIMO CHE TROVAVA! QUESTO PERCHè FACEVO
NEXT_PATH = PATH, MA CIò COPIAVA L'INDIRIZZO! MA ALLORA DI FATTO MODIFICANDO NEXT_PATH MODIFICAVO ANCHE PATH. QUINDI RICORDATI
CHE SE ASSEGNI UNA LISTA A QUALCOSA, GLI ASSEGNI L'INDIRIZZO DELLA LISTA, NON IL CONTENUTO (PER ASSEGNARGLI IL CONTENUTO VEDI
STACK OVERFLOW. IL FATTO è CHE HO PROVATO 2/3 METODI DI QUELLI CONSIGLIATI, MA SOLO UNO MI FUNZIONA)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''

# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """

    """
    EXECUTION                                   
    take data from list
        put every line into a list
        split the list
    use data to create the graph. for every line of the file:
        if the node isn't in the digraph (see method), create the node and put it in the digraph
        if the path isn't in the digraph(see method), create the path, the weighted path and then add it to the digraph
    """

    print("Loading map from file...")
    digraph = Digraph()
    with open(map_filename, 'r') as mit_map:
        for line in mit_map:
            #Preparing line putting each element of it in a list
            if line[len(line) - 1] == '\n':
                line = line[0:len(line)-1]
            splitted_line = line.split(' ')
            #Create the node source and add it to the digraph
            node_src = Node(splitted_line[0])
            try: digraph.add_node(node_src) 
            except ValueError: pass
            #Create the node destination and add it to the digraph       
            node_dest = Node(splitted_line[1])
            try: digraph.add_node(node_dest) 
            except ValueError: pass
            #For every edge associated to the node, I control if there's the path I'm considering(this is implemented in the method, see graph.py)
            #create path
            path = WeightedEdge(splitted_line[0], splitted_line[1], splitted_line[2], splitted_line[3])
            #add path into digraph
            try: digraph.add_edge(path)
            except ValueError: pass
    return digraph


'''
For testing:
print(load_map('test_load_map.txt'))
'''

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out


#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer:
#

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist = 0,
                  best_path = []):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    #20 righe di codice totali
    #TO IMPLEMENT: point 2 of the text 
    #At first, I put the node at which I start (given at input) in the best_path list  
    #if path[0] == []:
        #path.append(start)
    #Base case
    if start == end:
        #Controlling that: my path isn't longer then the best one, best_path is not the starting value
        if (path[1] < best_dist or best_dist == 0) and (path[2] < max_dist_outdoors):      
            path[0].append(start)
            #print("ARRIVATO CON PATH - A: ", path, start)
            return (path[0], path[1]) #DEBUG: il next path mano a mano che risalgo è best_path, ma invece dovrebbe mantenere il valore vecchio
        else:
            #print("LA MIA DISTANZA è MAGGIORE: TORNO SU")
            return ([], best_dist)
    else:
        if (path[1] < best_dist \
            or best_dist == 0) \
            and (path[2] < max_dist_outdoors) \
            and (start not in path[0]):
            if digraph.get_edges_for_node(start) == []:
                return ([], best_dist)
            path[0].append(start)
            #print("ALL NEXT_PATHS WILL COME FROM ME: ", path)
            next_path = copy.deepcopy(path)
            #next_path[0].append(start)  # Node(n_to_n.get_source())
            for n_to_n in digraph.get_edges_for_node(start):
                #NB: return gives always back a string!
                next_path[1] += int(n_to_n.get_total_distance())
                next_path[2] += int(n_to_n.get_outdoor_distance())
                returned_path = get_best_path(digraph, Node(n_to_n.get_destination()), end, next_path, max_dist_outdoors, best_dist, best_path)
                #Re-setting next_path
                #print("ACTUAL NEXT PATH: ", next_path)
                #print("SEED NEXT NEXT PATH: ", path)
                next_path = copy.deepcopy(path)
                #print("ACTUAL PATH: ", n_to_n)
                #print("RETURNED PATH: ", returned_path[0], returned_path[1])
                #print("BEST DIST: ", best_dist)             
                if (returned_path[0] != [] and returned_path[1] != 0) and (best_dist == 0 or returned_path[1] < best_dist):
                    best_path = returned_path[0]
                    best_dist = returned_path[1]
                #print("BEST PATH - BEST DIST IN FOR: ", best_path, best_dist)
        else:
            #print("SONO UN FALLITO: TORNO SU")
            return ([], best_dist)
    #print("BEST PATH - BEST DIST: ", best_path, best_dist)
    return (best_path, best_dist)
                    



# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """

    best_path = ()
    #dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
    best_path = get_best_path(digraph, Node(start), Node(end), [[], 0, 0], max_dist_outdoors)
    if best_path[0] == []:
        raise ValueError("No path found")
    return list(best_path[0])


# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


if __name__ == "__main__":
    unittest.main()
