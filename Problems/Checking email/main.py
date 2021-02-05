def check_email(string):
    if " " not in string and "@" in string:
        domain = string[string.index("@") + 1:]
        if "." in domain and not domain.startswith("."):
            return True
    return False
