🔐 **AKRO Encryption**

AKRO (ASCII Keyed Reversal Obfuscation) is a lightweight Python-based encryption and obfuscation algorithm.
It transforms readable text into encoded data using ASCII conversion, a repeating key cipher, random junk insertion, and sequence reversal. The process is fully reversible using the provided decryption logic.

✨ **Features**

* ASCII-based encoding
* Repeating key encryption
* Random letter obfuscation
* Reversible encryption/decryption
* Simple and modular design

⚙️ **How It Works**

Encryption steps:

1. Convert text to ASCII values.
2. Add repeating key ASCII values.
3. Insert random letters after every third value.
4. Reverse the sequence.

Decryption performs these steps in reverse order.

🚀 **Usage**

Run:
python encrypt.py
python decrypt.py

📘 **Note**

This project is for educational purposes and learning encryption concepts. It is not intended for real-world cryptographic security.
