class RepeatedKeyCipher:

    def __init__(self, key: bytes = bytes([0, 0, 0, 0, 0])):
        """Initializes the object with a list of integers between 0 and 255."""
        # WARNING: DON'T EDIT THIS FUNCTION!
        self.key = list(key)

    def encrypt(self, plaintext: str) -> bytes:
        """Encrypts a given plaintext string and returns the ciphertext."""
        # TODO: IMPLEMENT THIS FUNCTION
        plaintext_bytes = plaintext.encode('latin-1')
        ciphertext = bytearray()
        for i in range(len(plaintext_bytes)):
            key_byte = self.key[i % len(self.key)]
            ciphertext.append(plaintext_bytes[i] ^ key_byte)
        return bytes(ciphertext)
        raise NotImplementedError()

    def decrypt(self, ciphertext: bytes) -> str:
        """Decrypts a given ciphertext string and returns the plaintext."""
        # TODO: IMPLEMENT THIS FUNCTION
        return RepeatedKeyCipher(bytes(self.key)).encrypt(ciphertext.decode('latin-1')).decode('latin-1')
        raise NotImplementedError()


class BreakerAssistant:

    def plaintext_score(self, plaintext: str) -> float:
        """Scores a candidate plaintext string, higher means more likely."""
        # Please don't return complex numbers, that would be just annoying.
        # TODO: IMPLEMENT THIS FUNCTION
        score = 0
        common_words = ["the", "and", "to", "of", "in", "is", "it", "that","you", "with", "as", "for", "was", "are", "be", "we","can", "not", "this", "have", "on", "but", "at"]
        for i in plaintext:
            if ord(i) < 32 and i != '\n':
                score -= 10
            elif ord(i) > 126:
                score -= 10
            elif i.isalpha():
                score += 3
            elif i == ' ':
                score += 3
            elif i in ".,!?'-\"\n":
                score += 1
        lower_text = plaintext.lower()
        for word in common_words:
            score += lower_text.count(" " + word + " ") * 10
        return score
        raise NotImplementedError()

    def brute_force(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher by brute-forcing all keys."""
        # TODO: IMPLEMENT THIS FUNCTION
        best_score = 0
        best_plaintext = ""
        for i in range(256 ** key_length):
            key_list = []
            temp = i
            for k in range(key_length):
                key_list.append(temp % 256)
                temp = temp // 256
            key = bytes(key_list)
            cipher = RepeatedKeyCipher(key)
            plaintext = cipher.decrypt(cipher_text)
            score = self.plaintext_score(plaintext)
            if score > best_score:
                best_score = score
                best_plaintext = plaintext
        return best_plaintext
        raise NotImplementedError()

    def smarter_break(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher any way you like."""
        # TODO: IMPLEMENT THIS FUNCTION
        key = bytearray()
        for i in range(key_length):
            group = cipher_text[i::key_length]
            best_score = -10000
            best_key = 0
            for possible_key in range(256):
                decrypted_group = bytearray()
                for byte in group:
                    decrypted_group.append(byte ^ possible_key)
                plaintext_i = decrypted_group.decode('latin-1')
                score = self.plaintext_score(plaintext_i)
                if score > best_score:
                    best_score = score
                    best_key= possible_key
            key.append(best_key)
        for j in range(key_length):
            best_score = -10000
            best_key = key[j]
            for possible_key in range(256):
                key[j] = possible_key
                plaintext = RepeatedKeyCipher(bytes(key)).decrypt(cipher_text)
                score = self.plaintext_score(plaintext)
                if score > best_score:
                   best_score = score
                   best_key = possible_key
            key[j] = best_key
        cipher = RepeatedKeyCipher(bytes(key))
        return cipher.decrypt(cipher_text)
        raise NotImplementedError()
        
        
        
        
        
        
        
        
