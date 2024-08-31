import whois

def whois_query(domain):
    try:
        info = whois.query(domain)
        return info
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    domain = input("Please enter a domain: ")
    result = whois_query(domain)
    print(result)