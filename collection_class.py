from packet_class import Packet

red_color = "\033[31m"
green_color = "\033[32m"
yellow_color = "\033[33m"
blue_color = "\033[34m"
magenta_color = "\033[35m"
cyan_color = "\033[36m"
reset_color = "\033[0m"

class Collection:

    def __init__(self, file_path, size = "byte", style = "spaced", mode = "r"):
        self.file_path = file_path
        self.size = size
        self.style = style
        self.list = []

    def read_in_packets(self):
        with open(self.file_path, "r") as file:
            buffer = ""
            for line in file:
                buffer += line.strip()
                
                while "," in buffer:
                    packet_data, buffer = buffer.split(",", 1)  #Split on first comma
                    packet = Packet(packet_data, self.size, self.style)
                    self.list.append(packet)

    def color_same_bits(self, start, end):
        """start and end indicate the slice of the packets list"""
        packet_slice = self.list[start:end]
        if not packet_slice:
            raise ValueError("bad packet slice, no packets in range given to 'color_same_bits()'")
        
        min_len = min(len(packet.list) for packet in packet_slice)

        for position in range(min_len):
            bits_at_position = [packet.list[position] for packet in packet_slice]

            if all(bit == bits_at_position[0] for bit in bits_at_position):
                for packet in packet_slice:
                    packet.color_bit(green_color, position)
            else:
                for packet in packet_slice:
                    packet.color_bit(red_color, position)
        
        for packet in packet_slice:
            packet.display()
    
    def color_all_bits_at(self, color, position, byte = 0):
        for item in self.list:
            item.color_bit(color, position, byte)

    def reset_all_color(self):
        for packet in self.list:
            for item in range(len(packet.list)):
                packet.color_bit(reset_color, item)

    def print_line(self):
        max_len = max(len(packet.list) for packet in self.list)
        for item in range(max_len):
            print("-", end="")
        print("\n")
        



    # packet1 = Packet("00000000111111110000000011111111", "byte", "stacked")
    # packet1.display()
    # print(f"packets around: {Packet.packets}")

    # packet2 = Packet("00000000111111110000000011111111", "32", "spaced")
    # packet2.display()
    # packet2.color_bit(green_color, 3, byte = 2)
    # packet2.display()
    # packet2.color_byte(green_color, 1)
    # packet2.display()
    # print(f"packets around: {Packet.packets}")

    # collection1 = Collection("tmp4.txt", "byte", "spaced")
    # collection1.read_in_packets()
    # collection1.print_line()
    # collection1.color_same_bits(0,4)
    # collection1.print_line()
    # collection1.reset_all_color()
    # collection1.print_line()
    # collection1.color_same_bits(0,2)
    # collection1.print_line()
    # collection1.reset_all_color()
    # collection1.print_line()
    # for packet in collection1.list:
    #     packet.display()
    # collection1.print_line()
