from Wallet import Address

generator = Address()

class Attack:

  def __init__(self):
    None

  def check_address(self, addressOne, addressTwo, left, right):
    addressOneLeft = addressOne[0:left]
    addressTwoLeft = addressTwo[0:left]

    addressOneRight = addressOne[-right:]
    addressTwoRight = addressTwo[-right:]

    print(f"{addressOneLeft} {addressTwoLeft}")
    print(f"{addressOneRight} {addressTwoRight}")

    if addressOneLeft == addressTwoLeft and addressOneRight == addressTwoRight:
      return True
    else:
      return False

  def generate_malicious_wallet(self, addressOwner, number=4):
    notFound = True

    while (notFound):
      maliciousAddress = generator.generate_wallet_address()
      print(maliciousAddress)
      print(f"{addressOwner[2:]} {maliciousAddress[2:]}")
      check = self.check_address(addressOwner[2:].lower(),
                                 maliciousAddress[2:], number, number)

      if check:
        notFound = False
        return  maliciousAddress
