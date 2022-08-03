class Codec:
    def __init__(self) -> None:
        self.database = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.id += 1
        self.database[self.id] = longUrl
        return f"https://tinyurl/{self.id}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        i = shortUrl.rfind('/')
        id = int(shortUrl[i+1:])
        return self.database[id]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
