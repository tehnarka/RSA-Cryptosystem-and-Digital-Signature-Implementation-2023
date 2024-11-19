# RSA Cryptosystem and Digital Signature Implementation

## Description
This repository contains an implementation of the RSA cryptosystem, including key generation, encryption, decryption, digital signatures, and key exchange protocols. The project uses pseudo-random sequence generators and primality testing methods to ensure the secure generation of keys for cryptographic applications.

## Contents
- Implementation of primality tests:
  - Miller-Rabin probabilistic test.
  - Trial division.
- Generation of pseudo-random sequences using the BBS generator.
- Key generation and management for RSA.
- Encryption, decryption, and digital signature creation/verification.
- Key exchange protocol simulation between two users.

## Features
1. Securely generate large prime numbers using pseudo-random sequences and primality tests.
2. Create RSA key pairs for two users (A and B).
3. Encrypt and decrypt messages.
4. Sign and verify digital signatures.
5. Simulate a secure key exchange between two users.

## Usage
1. Run the script:  
   ```bash
   python AsymCryptoLab2-Python-2023-Nemkovych_fi-94.py
   ```
2. Follow the interactive or automated procedure to:
   - Generate prime numbers.
   - Create RSA key pairs.
   - Encrypt/decrypt messages.
   - Sign/verify messages.
   - Simulate key exchange.

## Requirements
- Python 3.9 or later.
- Libraries:
  - `random`
  - `datetime`
