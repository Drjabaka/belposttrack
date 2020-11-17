# get status for parcel

from bs4 import BeautifulSoup
import urllib.request


BASEURL = "https://webservices.belpost.by/searchRu/"

class Track:
    def __init__(self, track):
        self.track = track
        self.items = []
        # GET request
        response = urllib.request.urlopen(BASEURL + track).read().decode('utf-8')
        soup = BeautifulSoup(response, 'html.parser')

        # get data from table -> list[timestamp, status, place]
        table = soup.find_all('table')[0].find_all('tr')[1:]
        for item in table:
            self.items.append([i.text for i in item.find_all('td')])
        self._counter = 0
        self._limit = len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if self._counter < self._limit:
            self._counter += 1
            return self.items[self._counter - 1]
        else:
            raise StopIteration

    def status(self):
        if self.items:
            return ' '.join(self.items[-1])
        else:
            return False

    def get_all(self):
        if self.items:
            all = ''
            for i in self.items:
                all += ' '.join(i) + '\n'
            return all
        else:
            return False

if __name__ == '__main__':
    for date, status, delivery in Track('Vv311081079by'):
        print(date, status, delivery)
