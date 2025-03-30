from packet_class import Packet
from collection_class import Collection
import sys

def main():
    if len(sys.argv) > 1:
        print()
        global collection
        collection = None

        division = "byte"
        display = "spaced"

        if len(sys.argv) > 2:
            division = sys.argv[2]

        if len(sys.argv) > 3:
            display = sys.argv[3]

        collection = Collection(sys.argv[1], division, display)
        collection.read_in_packets()

        collection.color_same_bits(0, len(collection.list) + 1)

    else:
        print("USAGE: python3 diff_bits.py comma_separated_packets [bit,byte,word,32,64 (optional) ] [spaced,stacked (optional)] ")


if __name__ == "__main__":
    main()