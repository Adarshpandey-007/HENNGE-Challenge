# HENNGE Challenge

This repository contains solutions for the HENNGE backend recursion challenge, focusing on:

- **Time-based One-Time Password (TOTP) Generation**  
  Implements TOTP using RFC 6238 and RFC 2617 standards for secure authentication.

- **Recursive List Processing**  
  Demonstrates recursive techniques for processing lists and handling test cases.

## Files

- `main.py`  
  Handles recursive input processing and computes results based on custom logic.

- `totp.py`  
  Generates a TOTP password and submits it to the HENNGE challenge API using HTTP Basic Authentication.

## Usage

1. **TOTP Submission**  
   Run `totp.py` and follow the prompts to enter your email and Gist URL. The script will generate a TOTP password and submit your solution to the challenge endpoint.

   ```sh
   python totp.py
   ```
