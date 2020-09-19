# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from queue import Queue

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl[8:].split('/', 1)[0]
        
        todo = Queue()
        todo.put(startUrl)
        visited = set()
        visited.add(startUrl)
        crawled = [startUrl]
        
        while not todo.empty():
            url = todo.get()
            link_urls = htmlParser.getUrls(url)
            for link in link_urls:
                if hostname in link and link not in visited:
                    crawled.append(link)
                    visited.add(link)
                    todo.put(link)
        return crawled
                
            
                    
            
