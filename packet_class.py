import re

red_color = "\033[31m"
green_color = "\033[32m"
yellow_color = "\033[33m"
blue_color = "\033[34m"
magenta_color = "\033[35m"
cyan_color = "\033[36m"
reset_color = "\033[0m"

class Packet:
    """"class that represents the packets and stores the following:
        desired subdivision (bits, bytes, etc)
        list of bits
        ability to display stacked or spaced
        stacked or spaced preference
        file path
        file descriptor"""
    packets = 0

    def __init__(self, input_string, size, style, mode="r"):
        """we have after the init:
                -a file accessible as "self.file"
                -a self.list that is the translation of that file to a list of bits (1 or 0) """

        if style != "stacked" and style != "spaced":
            raise ValueError("either stacked or spaced for display buddy")
        else:
            self.style = style

        if size != "bit" and size != "byte" and size != "word" and size != "32" and size != "64":
            raise ValueError("size invalid")
        else:
            if size == "64" or size == "32":
                self.size = int(size)
            else:
                if size == "bit":
                    self.size = 1
                elif size == "byte":
                    self.size = 8
                elif size == "word":
                    self.size = 16
                else:
                    print("howhowhowhowhowhwohwohwohdoieuhfkJHSDV<Zfj")

        self.list = self.read_in_packet(input_string)
        Packet.packets += 1
        self.translate_to_colored_list()

    def read_in_packet(self, input_string):
        lst = []
        clean_list = []
        for one_byte in input_string:
            if one_byte in ["\n", " "]:  # Skip newlines and spaces
                continue
            lst.append([one_byte])
        for item in lst:
            clean_list.append(item[0])
        return clean_list

    def translate_to_colored_list(self):
        new_list = []
        for item in self.list:
            new_list.append(reset_color + item[0] + reset_color)
        self.list = new_list

    def display(self):
        i = 0
        for item in self.list:
            if ((i % self.size) == 0):
                if self.style == "stacked":
                    print()
                else:
                    print(" ", end = "")
                
                print(f"{item}", end="")
            else:
                print(f"{item}", end="")
            i = i + 1
        print("\n")

    def color_bit(self, color, position, byte=0):
        if color != red_color and color != green_color \
            and color != yellow_color and color != blue_color \
                and color != magenta_color and color != cyan_color and color != reset_color:
                raise ValueError("unsupported coloring")
        
        pattern = r'\033\[\d+(?:;\d+)*m'

        bit = self.list[(8 * byte) + position]
        recolored_bit = re.sub(pattern, color, bit, count=1)
        self.list[(8 * byte) + position] = recolored_bit

    def color_byte(self, color, position):
        for item in range(8):
            self.color_bit(color, (position*8) + item)


        
        

    

# def main():
#     tmp = input("file plz: ")
#     size = input("input size (bit, byte, word, 32, 64): ")
#     display = input("input display style (stacked/spaced): ")
#     packet1 = Packet(tmp, size, display)


# if __name__ == "__main__":
#     main()