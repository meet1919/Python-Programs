class AddHref:
    def __init__(self, input_text):
        self.input_text = input_text.lower()
        self.words_list = []
        self.dictionary = {}

    def extract_words(self):
        common_words = [
            'they', 'is', 'about', 'this', 'are', 'rare', 'creatures', 'with', 'high', 'abilities', 'of', 'members', 'tribe']
        words = self.input_text.split()
        for word in words:
            if word not in common_words:
                self.words_list.append(word)
        return self.words_list

    def assign_link(self):
        import requests, bs4
        for keyword in self.words_list:
            search_link = 'https://www.google.com/search?q=' + keyword
            res = requests.get(search_link)
            soup = bs4.BeautifulSoup(res.text, features='html.parser')
            websites = soup.select('.kCrYT a')
            self.dictionary[keyword] = 'http://google.com' + websites[0].get('href')
        return self.dictionary



text = 'This is about intp This are rare creatures with high cognitive abilities They are members of Hunter Gatherer tribe'

href = AddHref(text)
href.extract_words()
print(href.assign_link())

