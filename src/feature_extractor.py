import re
from urllib.parse import urlparse

def extract_features_from_url(url):
    """
    Extracts a list of advanced features from a given URL for phishing detection.
    """
    features = []

    # 1. URL Length
    features.append(len(url))

    # 2. Presence of IP Address
    has_ip = 1 if re.match(r"^(http[s]?://)?\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", url) else 0
    features.append(has_ip)

    # 3. Presence of '@' symbol
    features.append(1 if '@' in url else 0)

    # 4. Uses HTTPS
    features.append(1 if url.startswith("https") else 0)

    # 5. Number of suspicious keywords
    keywords = ['login', 'secure', 'account', 'update', 'free', 'verify', 'bank', 'paypal', 'ebay', 'microsoft']
    features.append(sum(1 for keyword in keywords if keyword in url.lower()))

    # 6. Number of dots in the hostname
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if hostname:
        features.append(hostname.count('.'))
    else:
        features.append(0) # Handle invalid URLs

    # 7. Number of slashes in the path
    path = parsed_url.path
    features.append(path.count('/'))

    # 8. Is URL shortened?
    shortening_services = ['bit.ly', 'goo.gl', 'tinyurl.com', 'shorte.st', 'is.gd']
    features.append(1 if hostname in shortening_services else 0)

    # 9. URL Redirection (presence of //)
    features.append(1 if '//' in url[8:] else 0)

    return features

# A list of all feature names for documentation/model training
FEATURE_NAMES = [
    'url_length', 'has_ip', 'has_at_symbol', 'uses_https', 
    'num_suspicious_keywords', 'num_dots', 'num_slashes', 
    'is_shortened', 'is_redirection'
]