"""
After framesplitting
136 frames
"""
from pprint import pprint
import collections
import re


frame_string = "0010111100111001011010000110000100111000011011100011010101111001011000110110100101101101011001010111001100110000011100100111100001110110"
def split2len(s, n):
    def _f(s, n):
        while s:
            yield s[:n]
            s = s[n:]
    return list(_f(s, n))


def first_clue_decode():
    groups = split2len(frame_string, 8)
    output = ''
    for group in groups:
        output += chr(int(group, 2))
    print output


def second_clue_decode():
    second_clue = "1grfyye47bmn4ir51um6h235a20zjhvq0nxu2y022xwjc0752nyvqkam2ts9q5sjj0lvuwga9efqhc5xzwdrk0nvyevapnc2xvhzjjd0qaotvqvk5u07k12aqlfmeqkgknvwfo1w1bm77xrue8oeeb50jk4r4e9bh0lelsf0hl1duo1atixxrj0ry4aiuolmfr41hwqxy76tmv68j2ikyzuab0x1y74u8dhis3li7zy616zi9hitjkayr38a51wdwuf7wz4w47v7wbxile55cayxszupu4a08qi1w46pwctviihetsws1lvivhaf147gw511q4ssdzstzalmp67hpzsyn18f4i3cbdok02qnuqp3c4jnir9za5h16awp4xy1f3b5rlwvbunolmad99eazslnllvoklfr2h81zi06drapvlr0ucfjscnwo7xv1ukuup04b3h6nwzxbdln2q7y8xmm5dbsg7p2kulfvlwxdzxowx1exvdcnuzbcw5po5g1"
    c = collections.Counter(second_clue)
    print 'Char, Count'
    for key, val in c.iteritems():
        print key, val
second_clue_decode()
