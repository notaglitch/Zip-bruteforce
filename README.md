# ZIP Password Cracker

A simple Python script that attempts to crack password-protected ZIP files using a wordlist.

## Description

This tool takes a ZIP file and a wordlist as input, then systematically tries each password in the wordlist to unlock the ZIP file. It's a basic implementation of a brute-force attack specifically for ZIP files.

## Features

- Supports password-protected ZIP files
- Accepts custom wordlists
- Automatically adds .zip extension if not present
- Shows progress by displaying each attempted password
- Stops and displays the correct password when found
