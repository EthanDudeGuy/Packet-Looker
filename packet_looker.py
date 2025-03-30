from packet_class import Packet
from collection_class import Collection


red_color = "\033[31m"
green_color = "\033[32m"
yellow_color = "\033[33m"
blue_color = "\033[34m"
magenta_color = "\033[35m"
cyan_color = "\033[36m"
reset_color = "\033[0m"

def main():
    print()
    print(f"""             {red_color}welcome to packet looker v2.0.
             An interactive packet analysis tool by Ethan Emery
             Type "help" to get started.{reset_color}""")
    print()

    global collection
    collection = None

    while True:
        option = input(">> ").strip().lower()
        
        if option == "help":
            print(f"""Hello and welcome to packet looker 2.0
designed and implemented by Ethan Emery

description:
    During a project I required the ability to line up
    and compare binary data packets in the command line
    to do some rudimentary analysis and reverse engineering of an RF protocol.
    I made a hacky command line took that lined up the packets and it was enough for my purposes,
    but I thought it might be nice to make a tool that would allow this to be done more easily

current features/how to use:
    packets are read in as a .txt file separated by commas. Packets
    can occupy multiple lines and include spaces or other whitespace characters (these will be removed in processing). 

            IMPORTANT NOTE: The last packet in the file 
                            will not be read if it does not end 
                            with a comma

            Example file contents:
                tmp.txt:
                        1111 0000 1111 0000 11111111,
                        0000000000000000 1111111111111111,
                        11111
                        1110000000011111111,

                will give the following packet objects to work with:
                11110000 11110000 11111111
                00000000 00000000 11111111 11111111
                11111111 00000000 11111111

current options supported:
    >> file
        -file will ask you for a file path to the above text file
         the text file should be in this directory or a subdirectory
         of this one (I think?)
        -When file has done its job it will tell you what it did
        -you can update your collection by using file again at any time

    >> display
        -display will immediately show you the packets in your collection
        according to the display options you chose in 'file' (spaced/stacked and size)

    >> diff
        -displays diff from slice of collection [start:end]
        -green packets are identical across the sliced packets, red are different
        -resets colorings when done if you tell it to
    
    >> color_bit
        -colors all bits at a certain index across packets from specific slice 
        -may crap out if you do it weird
        -start:end will be affected, position indicates the index
    
    >> color_byte
        -color bit but you index a byte directly

    >> reset
        -resets any coloring you may have done

    >> exit
        -exits
    
    TIPS:
        -keep screen wide so packets line up correctly

        -if packets are longer than screen width use 'stacked'
         when reading in packets. It's ugly but it fits on the screen

        -Look at the <stuff in here> when the program asks you for an input
         those are your options
        
        -if you pass something that is not an option either you will be informed of this
         or everything will break
        
        -Use 'diff' with wipe set to 'no' to start and then use color_bit and color_byte 
         to further anotate your file. color_bit allows for arbitrarily indexed ranges to be colored.
         color_byte colors a whole byte at a position (index of that byte)
""")

        elif option == "file":
            path = input(">> File path please >> ")
            division = input(">> How would you like these broken up? <bit/byte/word/32/64> >> ")
            display = input(">> How would you like them displayed? <stacked/spaced> (you probably want spaced) >> ")
            collection = Collection(path, division, display)
            collection.read_in_packets()
            print()
            print(f"System >> unless everything broke, you now have 1 collection with {len(collection.list)} packets in it")
            print("System >> for better or worse I let you put whatever you want in there")
            print()

        elif option == "display":
            if collection == None:
                print("use 'file' first")
                continue
            print()
            for item in collection.list:
                item.display()

        elif option == "diff":
            if collection == None:
                print("use 'file' first")
                continue
            print(">> show similarities from packet:")
            start = int(input(">> staring packet index <0,1,2,3,...> >> "))
            end = int(input(">> ending packet index (not included) <0,1,2,3,...> >> "))
            keep = input(">> wipe color after showing you? <yes/no> >> ").strip().lower()
            print()
            if keep == "yes":
                collection.color_same_bits(start, end)
                continue
            elif keep == "no":
                collection.color_same_bits(start, end)
                continue
            else:
                print()
                print("System >> invlalid wipe option")
                print()
                continue

        elif option == "color_bit":
            if collection == None:
                print("use 'file' first")
                continue
            color = input(">> color to color with? <red, green, blue, yellow, magenta, cyan, white> >> ").strip().lower()
            if color == "red":
                color = red_color
            elif color == "green":
                color = green_color
            elif color == "blue":
                color = blue_color
            elif color == "yellow":
                color = yellow_color
            elif color == "magenta":
                color = magenta_color
            elif color == "cyan":
                color = cyan_color
            elif color == "white":
                color = reset_color
            else:
                print("unsupported color option")
                continue
            rng = input(">> do you want to color a range of indices? <yes/no> >> ").strip().lower()
            if rng == "yes":
                start = int(input(">> starting index (absolute) <0,1,2,3,...> >> "))
                end = int(input(">> ending index (not included) <0,1,2,3,...> >> "))
                for item in range(max(len(packet.list) for packet in collection.list))[start:end]:
                    collection.color_all_bits_at(color, item, 0)
                print()
                print("System >> either I did it or everything is broken, might as well check with 'display")
                print()
            
            else:
                byte = int(input(">> byte number (0 for absolute indexing) >> "))
                position = int(input(">> index (offset from byte or absolute index) >> "))
                collection.color_all_bits_at(color, position, byte)
                print()
                print("System >> ok either every bit at that index is colored the color you chose or everything broke")
                print("System >> type 'display' to see")
                print()
        
        elif option == "color_byte":
            if collection == None:
                print("use 'file' first")
                continue
            color = input(">> color to color with? <red, green, blue, yellow, magenta, cyan, white> >> ").strip().lower()
            if color == "red":
                color = red_color
            elif color == "green":
                color = green_color
            elif color == "blue":
                color = blue_color
            elif color == "yellow":
                color = yellow_color
            elif color == "magenta":
                color = magenta_color
            elif color == "cyan":
                color = cyan_color
            elif color == "white":
                color = reset_color
            else:
                print("unsupported color")
                continue
            byte = int(input(">> byte number >> "))

            for item in collection.list:
                item.color_byte(color, byte)

            print()
            print("System >> did it (maybe)")
            print("System >> check with 'display'")
            print()

        elif option == "reset":
            if collection == None:
                print("use 'file' first")
                continue
            collection.reset_all_color()
            print()
            print("System >> diddly done boss")
            print()


        elif option == "exit":
            return 0

        else:
            print("invalid option, type 'help' for a complete list of currently supported options, or 'exit' to... you know")



if __name__ == "__main__":
    main()