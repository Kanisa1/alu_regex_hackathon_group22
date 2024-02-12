import re

class RegexValidation:
    def __init__(self, validation: list):
        self.validation = validation

    def movie_titles(self):
        #Movie titles
        pattern = r"^[a-zA-Z]+(\d{4})$ if only letters are needed else:^[^\d]+(\d{4})$"
        movies = re.findall(pattern, self.validation)
        if movies is None or len(movies) == 0:
            raise FileNotFoundError("None of these match")
        else:
            print(movies, end=",")

    def songs(self):
         #Songs
        pattern = r'^\[Verse/\d+].+$'
        songs = re.findall(pattern, self.validation)
        if songs is None or len(songs) == 0:
            raise FileNotFoundError("None of these match")
        else:
            print(songs, end=",")

    def twitter(self):
         #Twitter Usernames
        pattern = r'^@[a-zA-Z0-9]+$'
        usernames = re.findall(pattern, self.validation)
        if usernames is None or len(usernames) == 0:
            raise FileNotFoundError("None of these match")
        else:
            print(usernames, end=",")

    def isbn(self):
         #ISBN
        pattern = r"^ISBN\s[0-9]{3}[-][0-9]{1}[-][0-9]{3}[-][0-9]{5}[-]{0-9]{1}"
        isbns = re.findall(pattern, self.validation)
        if isbns is None or len(isbns) == 0:
            raise FileNotFoundError("None of these match")
        else:
            print(isbns, end=",")

    def jokes(self):
         #Jokes
        pattern = r"^Why did the .+\?Because.+"
        joke = re.findall(pattern, self.validation)
        if joke is None or len(joke) == 0:
            raise FileNotFoundError("None of these match")
        else:
            print(joke, end=",")

    def tv(self):
         #TV Episodes
        pattern = r"insert your TV episode regex pattern here"
        episodes = re.findall(pattern, self.validation)
        if episodes is None or len(episodes) == 0:
            raise FileNotFoundError("None of these match")
        else:
            print(episodes, end=",")

    def dates(self):
         #Weird Dates
        pattern = r"insert your date regex pattern here"
        dates = re.findall(pattern, self.validation)
        if dates is None or len(dates) == 0:
            raise FileNotFoundError("None of these match")
        else:
            print(dates, end=",")

    def hex(self):
         #Hex Codes
        pattern = r"#[a-zA-Z0-9]{6,8}"
        codes = re.findall(pattern, self.validation)
        if codes is None or len(codes) == 0:
            raise FileNotFoundError("None of these match")
        else:
            print(codes, end=",")

    def ip(self):
         #IP address
        pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
"
        addresses = re.findall(pattern, self.validation)
        if addresses is None or len(addresses) == 0:
            raise FileNotFoundError("None of these match")
        else:
            print(addresses, end=",")


if __name__ == "__main__":
    checkers = ['movie_titles', 'songs', 'twitter', 'isbn', 'jokes', 'tv', 'dates', 'hex', 'ip']
    print(checkers)
    question = input("Enter what you want to check: ")
    validation_data = input("Enter a list of what you want: ")

    if question not in checkers:
        raise NameError("Enter the right options")

    rg = RegexValidation(validation_data)

    if question == 'movie_titles':
        rg.movie_titles()
    elif question == 'songs':
        rg.songs()
    elif question == 'twitter':
        rg.twitter()
    elif question == 'isbn':
        rg.isbn()
    elif question == 'jokes':
        rg.jokes()
    elif question == 'tv':
        rg.tv()
    elif question == 'dates':
        rg.dates()
    elif question == 'hex':
        rg.hex()
    elif question == 'ip':
        rg.ip()
