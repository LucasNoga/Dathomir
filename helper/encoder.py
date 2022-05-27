'''Encoder module'''


def encode_token(message: str) -> str:
    '''Encode message with Dathomir method'''
    encoded = message.replace('ghp_', '')
    return encoded


def decode_token(encoded: str) -> str:
    '''Decode message with Dathomir method'''
    token_prefix = "ghp_"
    res = list(encoded)
    res.insert(0, token_prefix)
    return ''.join(res)


if __name__ == '__main__':
    token: str = '<ACCESS_TOKEN>'
    print(f"token tested: {token}")
    encoded_token: str = encode_token(token)
    print(f"message encoded {encoded_token}")
    decoded_token: str = decode_token(encoded_token)
    print(f"key decoded: {decoded_token}")
