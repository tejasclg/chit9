import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    # Count frequencies of characters
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1

    # Create a priority queue for Huffman nodes
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    # Build Huffman tree using a greedy approach
    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)

        internal_node = HuffmanNode(None, left_child.freq + right_child.freq)
        internal_node.left = left_child
        internal_node.right = right_child

        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]

def generate_huffman_codes(node, current_code="", huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = {}

    if node is not None:
        if node.char is not None:
            huffman_codes[node.char] = current_code
        generate_huffman_codes(node.left, current_code + "0", huffman_codes)
        generate_huffman_codes(node.right, current_code + "1", huffman_codes)

def huffman_encoding(data):
    if not data:
        return None, None

    root = build_huffman_tree(data)
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)

    encoded_data = "".join(huffman_codes[char] for char in data)
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data or root is None:
        return None

    decoded_data = ""
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root

    return decoded_data

if __name__ == "__main__":
    user_input = input("Enter data to be encoded: ")

    encoded_data, huffman_tree = huffman_encoding(user_input)

    print(f"\nEncoded data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, huffman_tree)

    print(f"Decoded data: {decoded_data}")
