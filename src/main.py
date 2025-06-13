from osint_collector import shodan_search
from vulnerability_scanner import scan_target
from visualization import draw_network_graph

def main():
    SHODAN_API_KEY = "Vmdv3acZ7IJjnzwmNGIFM2SddSCPOurk"
    target = "example.com"

    shodan_search(SHODAN_API_KEY, target)
    scan_target("8.8.8.8")
    connections = [("PC", "Router"), ("Router", "Internet")]
    draw_network_graph(connections)

if __name__ == "__main__":
    main()
