from eth_keys import keys
import secrets


class Address:

  def __init__(self):
    return None

  def generate_wallet_address(self):
    priv = secrets.token_hex(32)
 
    # Generate a random private key
    private_key = keys.PrivateKey(bytes.fromhex(priv))
    public_key = private_key.public_key
    address = public_key.to_address()

    return  address
