#%% Day 16
import math

with open('data/input16.txt') as f:
    hex = f.readline()

v_counter = []

def strip_off(bin_signal, num=1):
    return bin_signal[:num], bin_signal[num:]

def parse_hex(hex):
    return bin(int(hex, 16))[2:].zfill(len(hex)*4)

def strip_version(bin_signal):
    v, bin_signal = strip_off(bin_signal, num=3)
    v = int(v,2)
    v_counter.append(v)
    return v, bin_signal

def strip_type(bin_signal):
    t , bin_signal = strip_off(bin_signal, num=3)
    return int(t, 2), bin_signal

def literal_parse(bin_signal):
    ls = []
    while True:   
        is_last = bin_signal[0]
        ls.append(bin_signal[1:5])
        bin_signal = bin_signal[5:]
        if is_last == '0': 
            return int("".join(ls),2), bin_signal


def parse_packet(bin_signal):
    version_number, bin_signal  = strip_version(bin_signal)
    packet_type, bin_signal  = strip_type(bin_signal)
    # 4 represent a literal value
    if packet_type == 4:
        literal, bin_signal = literal_parse(bin_signal)
        ans = literal
    else: #its an operator        
        length_type_ID, bin_signal = strip_off(bin_signal)        
        ls = []

        if length_type_ID == '0':             
            total_length_of_packet, bin_signal = strip_off(bin_signal, num=15)
            total_length_of_packet = int(total_length_of_packet,2)
            subpacks, bin_signal = strip_off(bin_signal, num=total_length_of_packet)
            ls = parse_whole_sequence(subpacks)
        
        if length_type_ID == '1': 
            number_of_sub_packets, bin_signal = strip_off(bin_signal, num=11)
            number_of_sub_packets = int(number_of_sub_packets,2)
            
            for _ in range(number_of_sub_packets):                
                res = parse_packet(bin_signal)                
                bin_signal = res[3]
                ls.append(res[2])

        
        print(packet_type, ls)
        # Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
        if packet_type==0:
            print('SUM')
            ans = sum(ls)
        # Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
        elif packet_type==1:
            print('product')            
            ans = math.prod(ls)
        # Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
        elif packet_type==2:
            print('min')            
            ans = min(ls)
        # Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
        elif packet_type==3:
            print('max')            
            ans = max(ls)        
        # Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
        elif packet_type==5:
            print('greater than')            
            ans = 1 if ls[0]>ls[1] else 0
        # Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
        elif packet_type==6:
            print('greater than')            
            ans = 1 if ls[0]<ls[1] else 0
        # Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
        elif packet_type==7:
            print('greater than')            
            ans = 1 if ls[0]==ls[1] else 0
        else: 
            assert(True), "Packet_type is unknown"
        
    return version_number, packet_type, ans, bin_signal


def parse_whole_sequence(bin_signal):    
    ls = []
    while len(bin_signal)>1:                
        _,_,literal, bin_signal = parse_packet(bin_signal)        
        ls.append(literal)
    return ls

#hex = 'D2FE28'          #test 1
#hex = '38006F45291200'  #test 2
#hex = 'EE00D40C823060'  #test 3
#hex = '8A004A801A8002F478' #test 4 -> res 16
#hex = '620080001611562C8802118E34' #test 5 -> res 12
#hex = 'C0015000016115A2E0802F182340' #test 6 -> res 23
#hex = 'A0016C880162017C3686B18A3D4780' #test 7 -> res 31
#hex = '005532447836402684AC7AB3801A800021F0961146B1007A1147C89440294D005C12D2A7BC992D3F4E50C72CDF29EECFD0ACD5CC016962099194002CE31C5D3005F401296CAF4B656A46B2DE5588015C913D8653A3A001B9C3C93D7AC672F4FF78C136532E6E0007FCDFA975A3004B002E69EC4FD2D32CDF3FFDDAF01C91FCA7B41700263818025A00B48DEF3DFB89D26C3281A200F4C5AF57582527BC1890042DE00B4B324DBA4FAFCE473EF7CC0802B59DA28580212B3BD99A78C8004EC300761DC128EE40086C4F8E50F0C01882D0FE29900A01C01C2C96F38FCBB3E18C96F38FCBB3E1BCC57E2AA0154EDEC45096712A64A2520C6401A9E80213D98562653D98562612A06C0143CB03C529B5D9FD87CBA64F88CA439EC5BB299718023800D3CE7A935F9EA884F5EFAE9E10079125AF39E80212330F93EC7DAD7A9D5C4002A24A806A0062019B6600730173640575A0147C60070011FCA005000F7080385800CBEE006800A30C023520077A401840004BAC00D7A001FB31AAD10CC016923DA00686769E019DA780D0022394854167C2A56FB75200D33801F696D5B922F98B68B64E02460054CAE900949401BB80021D0562344E00042A16C6B8253000600B78020200E44386B068401E8391661C4E14B804D3B6B27CFE98E73BCF55B65762C402768803F09620419100661EC2A8CE0008741A83917CC024970D9E718DD341640259D80200008444D8F713C401D88310E2EC9F20F3330E059009118019A8803F12A0FC6E1006E3744183D27312200D4AC01693F5A131C93F5A131C970D6008867379CD3221289B13D402492EE377917CACEDB3695AD61C939C7C10082597E3740E857396499EA31980293F4FD206B40123CEE27CFB64D5E57B9ACC7F993D9495444001C998E66B50896B0B90050D34DF3295289128E73070E00A4E7A389224323005E801049351952694C000'

#Task2
# hex = 'C200B40A82'  #SUM 3
# hex = '04005AC33890' #produkt 54
# hex = '880086C3E88112' # min 7
# hex = 'CE00C43D881120' # min 9
# hex = 'D8005AC2A8F0' # produces 1, because 5 is less than 15.
# hex = 'F600BC2D8F' # produces 0, because 5 is not greater than 15.
# hex = '9C005AC2F8F0' # produces 0, because 5 is not equal to 15.
# hex = '9C0141080250320F1802104A08' # produces 1, because 1 + 3 = 2 * 2

bin_signal = parse_hex(hex) 
version_number, packet_type, literal, bin_signal = parse_packet(bin_signal)
print("Task1, ", sum(v_counter))
print("Task2, ", literal)

assert(literal == 299227024091)

# %%
