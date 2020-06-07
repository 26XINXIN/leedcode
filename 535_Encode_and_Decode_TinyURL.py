class Codec:
    def __init__(self):
        self.table = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        loc = hash(longUrl)
        while loc in self.table:
            loc += 1
        self.table[loc] = longUrl
        return 'http:/tinyurl.com/{}'.format(loc)
            

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        loc = int(shortUrl.rsplit('/', 1)[1])
        return self.table[loc]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))