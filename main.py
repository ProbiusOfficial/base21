BASE21_ALPHABET = "ABCDFGHJKLMNPQRSTWXYZ"
BASE21_SIZE = len(BASE21_ALPHABET) # 21

VALUE_TO_CHAR = {i: char for i, char in enumerate(BASE21_ALPHABET)}
CHAR_TO_VALUE = {char: i for i, char in enumerate(BASE21_ALPHABET)}

def base21_encode(data: bytes) -> str:
    """
    将 bytes 数据编码为 Base21 字符串。
    (1 字节 -> 2 字符)
    """
    encoded_parts = []
    
    for byte in data:

        v1 = byte // BASE21_SIZE

        v2 = byte % BASE21_SIZE
        
        c1 = VALUE_TO_CHAR[v1]
        c2 = VALUE_TO_CHAR[v2]
        
        encoded_parts.append(c1)
        encoded_parts.append(c2)
        
    return "".join(encoded_parts)

def base21_decode(encoded_data: str) -> bytes:
    """
    将 Base21 字符串解码为 bytes 数据。
    (2 字符 -> 1 字节)
    """
    if len(encoded_data) % 2 != 0:
        raise ValueError("Base21 encoded data length must be a multiple of 2.")

    decoded_bytes = bytearray()
    
    for i in range(0, len(encoded_data), 2):
        c1 = encoded_data[i]
        c2 = encoded_data[i+1]

        try:
            v1 = CHAR_TO_VALUE[c1]
            v2 = CHAR_TO_VALUE[c2]
        except KeyError as e:
            raise ValueError(f"Invalid Base21 character: {e}")
      
        if byte_value > 255:
             raise ValueError(f"Decoded value {byte_value} exceeds 8-bit limit (255). Invalid Base21 sequence: {c1}{c2}")
        
        decoded_bytes.append(byte_value)
        
    return bytes(decoded_bytes)

# --- 示例用法 ---

original_text = "Hello Base21"
print(f"原始文本: {original_text}")

# 1. 编码
original_bytes = original_text.encode('utf-8')
encoded_string = base21_encode(original_bytes)
print(f"编码结果: {encoded_string}")

# 2. 解码
decoded_bytes = base21_decode(encoded_string)
decoded_text = decoded_bytes.decode('utf-8')
print(f"解码结果: {decoded_text}")
