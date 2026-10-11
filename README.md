# Cryptography and Cryptanalysis

This project explores how weaknesses in encryption design can allow information to be recovered without knowing the secret key. It covers a repeating-key XOR cipher and a simplified RSA-based ATM system.

## Part 1: Repeating-Key XOR Cipher

The cipher encrypts a message by XORing each plaintext byte with a key byte. When the key ends, it repeats from the beginning. Applying the same XOR operation again recovers the original message.

The exercises include implementing encryption and decryption, then recovering plaintext without being given the key:

- **Plaintext scoring:** Rank candidate messages using letters, spaces, punctuation, and common English words.
- **Brute-force recovery:** Try every possible key of a specified length and select the highest-scoring plaintext.
- **More efficient recovery:** Group ciphertext bytes by their position within the repeating key. Test each key byte separately, then refine the recovered key using the score of the complete message.

This demonstrates why repeating a short XOR key creates patterns that can be used for cryptanalysis.

## Part 2: Simplified RSA ATM

The second part examines weaknesses in a toy ATM system that applies RSA directly to numeric values:

- **PIN recovery:** Test all 10,000 possible four-digit PIN values and compare their encrypted results with the supplied ciphertext.
- **Small-message recovery:** For a sufficiently small message encrypted with exponent 3, the ciphertext is simply the message cubed. An integer cube-root search recovers the original value.
- **Signature verification:** Demonstrate why accepting the numeric value 1 as both an approval status and its signature makes the toy verification scheme ineffective.

These examples concern simplified, unpadded RSA constructions.

## Files

- `q1.py`: Repeating-key XOR cipher and plaintext-recovery methods.
- `q2.py`: Solutions for the RSA ATM exercises.

## Environment

Python 3. `q2.py` depends on the course-provided `q2_atm.py` module, which uses PyCryptodome. That module and the original exercise inputs are not included in this code-only upload.

