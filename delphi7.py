# Delphi7 Enterprise *KEYGEN*
class KeyGenerator:
    def __init__(self):
        self.lcg_state = 0
        self.charset = "ABC2DE34FGHJKM5NPQRST6U7VWX8YZ?9"
        
    def lcg_random(self, a1):
        self.lcg_state = (134775813 * self.lcg_state + 1) & 0xFFFFFFFF
        temp = (self.lcg_state * a1) & 0xFFFFFFFFFFFFFFFF
        return (temp >> 32) & 0xFFFFFFFF
    
    def hash_transform_1(self, data):
        v1 = 0xB93AC32C
        for i in range(20):
            v4 = data[i]
            data[i] ^= v1 >> 27
            temp = (32 * (v4 ^ v1)) ^ v4 ^ v1
            temp = ((temp << 10) ^ temp)
            temp = ((temp << 15) ^ temp)
            temp = ((temp << 20) ^ temp)
            temp = ((temp << 25) ^ temp)
            v1 = ((temp << 30) ^ temp)
            v1 &= 0xFFFFFFFF
        return v1
    
    def hash_transform_2(self, data):
        v1 = 0xB93AC32C
        for i in range(20):
            data[i] ^= v1 >> 27
            v4 = (32 * (data[i] ^ v1)) ^ data[i] ^ v1
            v5 = ((v4 << 10) ^ v4)
            v6 = ((v5 << 15) ^ v5)
            v7 = ((v6 << 20) ^ v6)
            v8 = ((v7 << 25) ^ v7)
            v1 = (v8 << 30) ^ v8
            v1 &= 0xFFFFFFFF
        return v1
    
    def encode_structure(self, data):
        struct_data = [0] * 8
        struct_data[0] = 2
        struct_data[1] = 1
        struct_data[2] = self.lcg_random(80)
        struct_data[3] = 0
        struct_data[4] = 0
        struct_data[5] = 4007
        struct_data[6] = 3
        struct_data[7] = self.lcg_random(80)
        for i in range(20):
            data[i] = 0
        data[0] |= (2 * (struct_data[5] & 0xFF)) & 2
        data[1] |= (struct_data[0] >> 8) & 1
        data[1] |= (2 * ((struct_data[0] >> 6) & 0xFF)) & 2
        data[2] |= (2 * ((struct_data[0] >> 5) & 0xFF)) & 2
        data[2] |= (struct_data[7] >> 2) & 1
        data[2] |= (4 * ((struct_data[5] >> 3) & 0xFF)) & 4
        data[3] |= (16 * ((struct_data[5] >> 2) & 0xFF)) & 0x10
        data[4] |= (8 * ((struct_data[0] >> 7) & 0xFF)) & 8
        data[5] |= (8 * ((struct_data[7] >> 3) & 0xFF)) & 8
        data[6] |= (2 * (struct_data[7] & 0xFF)) & 8
        data[7] |= (4 * (struct_data[0] & 0xFF)) & 4
        data[7] |= (2 * ((struct_data[5] >> 4) & 0xFF)) & 2
        data[8] |= (struct_data[0] >> 1) & 1
        data[8] |= struct_data[1] & 1
        data[8] |= (2 * (struct_data[4] & 0xFF)) & 2
        data[8] |= (4 * (struct_data[4] & 0xFF)) & 4
        data[8] |= (8 * (struct_data[4] & 0xFF)) & 8
        data[9] |= (16 * ((struct_data[0] >> 2) & 0xFF)) & 0x10
        data[15] |= (4 * ((struct_data[0] >> 4) & 0xFF)) & 4
        data[15] |= (8 * (struct_data[6] & 0xFF)) & 8
        data[16] |= (16 * ((struct_data[7] >> 1) & 0xFF)) & 0x10
        data[16] |= (struct_data[5] >> 1) & 1
        data[18] |= (4 * ((struct_data[0] >> 3) & 0xFF)) & 4
        data[18] |= (8 * ((struct_data[0] >> 9) & 0xFF)) & 8
        
        return struct_data
    
    def decode_structure(self, data):
        struct_data = [0] * 8
        struct_data[0] |= (data[1] & 1) << 8
        struct_data[0] |= ((data[1] & 2) >> 1) << 6
        struct_data[0] |= ((data[2] & 2) >> 1) << 5
        struct_data[0] |= ((data[4] & 8) >> 3) << 7
        struct_data[0] |= (data[7] & 4) >> 2
        struct_data[0] |= (data[8] & 1) << 1
        struct_data[0] |= ((data[9] & 0x10) >> 4) << 2
        struct_data[0] |= ((data[15] & 4) >> 2) << 4
        struct_data[0] |= ((data[18] & 4) >> 2) << 3
        struct_data[0] |= ((data[18] & 8) >> 3) << 9
        
        struct_data[7] |= (data[2] & 1) << 2
        struct_data[7] |= ((data[5] & 8) >> 3) << 3
        struct_data[7] |= ((data[6] & 2) >> 1)
        struct_data[7] |= ((data[16] & 0x10) >> 4) << 1
        
        struct_data[5] |= (data[0] & 2) >> 1
        struct_data[5] |= ((data[2] & 4) >> 2) << 3
        struct_data[5] |= ((data[3] & 0x10) >> 4) << 2
        struct_data[5] |= ((data[7] & 2) >> 1) << 4
        struct_data[5] |= (data[16] & 1) << 1
        
        struct_data[6] |= (data[15] & 8) >> 3
        
        struct_data[1] |= data[8] & 1
        
        struct_data[4] |= (data[8] & 2) >> 1
        struct_data[4] |= (data[8] & 4) >> 2
        struct_data[4] |= (data[8] & 8) >> 3
        
        return struct_data
    
    def string_to_codes(self, input_str):
        codes = []
        for char in input_str:
            if char in self.charset:
                codes.append(self.charset.index(char))
            else:
                codes.append(0)
        return codes
    
    def codes_to_string(self, codes):
        result = ""
        for code in codes:
            if 0 <= code < len(self.charset):
                result += self.charset[code]
            else:
                result += '?'
        return result
    
    def generate_serial(self):
        data = [0] * 20
        struct_data = self.encode_structure(data)
        decoded_struct = self.decode_structure(data)
        self.hash_transform_2(data)
        serial_codes = []
        for i in range(20):
            serial_codes.append(data[i] & 0x1F)
        serial_str = self.codes_to_string(serial_codes)
        formatted_serial = (
            f"{serial_str[0:4]}-{serial_str[4:10]}-{serial_str[10:16]}-{serial_str[16:20]}"
        )
        return formatted_serial, serial_str
    
    def generate_key_from_serial(self, serial_str):
        clean_serial = serial_str.replace('-', '')
        codes = self.string_to_codes(clean_serial)
        data = [0] * 20
        for i in range(min(20, len(codes))):
            data[i] = codes[i]
        hash_result = self.hash_transform_1(data)
        key_codes = []
        for i in range(6):
            v9 = (hash_result >> (5 * i)) & 0x1F
            key_codes.append(v9)
        key_str = self.codes_to_string(key_codes)
        if len(key_str) >= 6:
            formatted_key = f"{key_str[0:3]}-{key_str[3:6]}"
        else:
            formatted_key = key_str
        return formatted_key
    
    def generate_keypair(self):
        serial_formatted, serial_raw = self.generate_serial()
        key_formatted = self.generate_key_from_serial(serial_raw)
        return serial_formatted, key_formatted

if __name__ == "__main__":
    generator = KeyGenerator()
    print("Index Serial Key")
    for i in range(5):
        serial, key = generator.generate_keypair()
        print(f"{i+1}: {serial} {key}")
