#huffman code
from heapq import heappush, heappop, heapify
from collections import defaultdict
 
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def decode(raw_decodetable_header, image_bin):
    #ReadInHeader Color Entries
    indexcount = "" #total number of RGB values
    spacer_reached = False
    counter = 0
    while spacer_read is False:
        indexcount = indexcount + raw_decodetable_header[counter]
        counter += 1
        if raw_decodetable_header[counter] is " ":
            spacer_read = True


        #read in number
    
    #Read in pixels and frequency     


    #Generate Huffman Codes

        
    #Read In huffman codes
        #iterate one at a time, until you find key



