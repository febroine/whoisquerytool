# WhoisLookup 🕵️‍♂️

A minimal Python tool to perform **WHOIS queries** on domain names using the `whois` Python library.

## 🌐 Example Usage

```bash
$ python whois.py
Please enter a domain: example.com
<WhoisEntry example.com>
```

The output will include domain registration details such as:

-Registrar

-Creation date

-Expiration date

-Name servers

-Status

-And more (depending on TLD)

## 🚀 Features

Simple CLI-based interface

Uses whois Python library

Gracefully handles exceptions

Works for most generic and country-code domains

## 📦 Requirements

Python 3.x

whois Python library

```bash
pip install python-whois
```

Note: On some systems, python-whois may be installed with:
```bash
pip install whois
```

## 🔐 Legal & Ethical Use

This tool is intended for educational and authorized research purposes only.
Always ensure you comply with domain registrar terms of service and legal requirements in your region.
