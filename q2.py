from q2_atm import ATM, ServerResponse


def extract_PIN(encrypted_PIN) -> int:
    """Extracts the original PIN string from an encrypted PIN."""
    # TODO: IMPLEMENT THIS FUNCTION
    atm = ATM()
    for pin in range(10000):
        if atm.encrypt_PIN(pin) == encrypted_PIN:
            return pin
    raise NotImplementedError()


def extract_credit_card(encrypted_credit_card) -> int:
    """Extracts a credit card number string from its ciphertext."""
    # TODO: IMPLEMENT THIS FUNCTION
    low = 0
    high = 10 ** 9
    while low <= high:
        mid = (low + high) // 2
        cube = mid ** 3
        if cube == encrypted_credit_card:
            return mid
        elif cube < encrypted_credit_card:
            low = mid + 1
        else:
            high = mid - 1
    raise NotImplementedError()


def forge_signature():
    """Forge a server response that passes verification."""
    # Return a ServerResponse instance.
    # TODO: IMPLEMENT THIS FUNCTION
    return ServerResponse(ATM.CODE_APPROVAL, 1)
    raise NotImplementedError()
