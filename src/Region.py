class Region:

    media = []
    identifier = ""
    trends = []
    useful_links = {}

    def __init__(self, media=None, identifier=None):
        self.media = media
        self.identifier = identifier

    def getMedia(self):
        return self.media

    def getIdentifier(self):
        return self.identifier

    def updateTrends(self, trends):
        self.trends = trends

    def getTrends(self):
        return self.trends

    def addUsefulLink(self, link, trend):
        if trend in self.useful_links:
            if link not in self.useful_links[trend]:
                self.useful_links[trend].add(link)
        else:
            new_set = {link}
            self.useful_links[trend] = new_set

    def cleanArticles(self):
        for trend, article_list in self.get_news().items():
            self.useful_links[trend] = set(self.useful_links[trend])

    def get_news(self):
        return self.useful_links
