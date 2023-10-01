def is_ipv4(content):
    import re
    pattern = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)$"
    matchPattern = re.search(pattern, content)
    if matchPattern:
        return True
    else:
        return False

def return_ip():
    import requests
    import re
    r = requests.get("https://ifconfig.io")
    where = r.text.index(">IP Address<")
    pattern = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)$"
    strip = str(r.text[where + 39:where + 51]).replace("</di", "")
    ip_address = re.sub(r'[^0-9.$]', "", r.text[where + 37:where + 100:])
    ip_address = re.search(r'(\b\d+).(\b\d+).(\b\d+).(\b\d+)', r.text)
    return (ip_address.group())

print(return_ip())
print(is_ipv4(str("92.5.238.242")))

