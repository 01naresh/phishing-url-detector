def get_url_features(url):
    feature1 = 1 if "http" in url else 0
    feature2 = len(url)
    feature3 = url.count('.')
    feature4 = int("@" in url)
    feature5 = int("//" in url)
    feature6 = int("-" in url)
    feature7 = int(url.startswith("https"))
    return [feature1, feature2, feature3, feature4, feature5, feature6, feature7]
