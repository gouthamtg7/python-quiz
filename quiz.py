import random
A = bool()
class Game:
    def __init__(self,score):
        self.score = score
        self.answer = answer
    dic = {
        "Sachin Tendulkar has scored 100 international centuries.": True,
        "The FIFA World Cup is held every three years.": False,
        "Roger Federer has won more Wimbledon titles than any other male tennis player.": True,
        "Virat Kohli is known as the 'Wall of Indian Cricket.'": False,
        "Lionel Messi has never won a Ballon d'Or.": False,
        "The Indian Premier League (IPL) started in 2008.": True,
        "The movie 'Titanic' was directed by Steven Spielberg.": False,
        "Mary Kom is a famous Indian badminton player.": False,
        "Cristiano Ronaldo has never played for Manchester United.": False,
        "The Bollywood movie 'Sholay' was released in 1975.": True,
        "The Olympic Games originated in Greece.": True,
        "MS Dhoni is known as 'Captain Cool.'": True,
        "The movie 'Inception' was directed by Christopher Nolan.": True,
        "Leander Paes is an Indian cricket player.": False,
        "The movie 'Avatar' was released in 2010.": False,
        "Lionel Messi has won the FIFA World Cup.": True,
        "The Ashes is a cricket series between India and Australia.": False,
        "Saina Nehwal is an Indian tennis player.": False,
        "The movie 'Baahubali' is directed by S. S. Rajamouli.": True,
        "Tiger Woods is a professional golfer.": True,
        "The Bollywood movie 'Dilwale Dulhania Le Jayenge' was released in 1995.": True,
        "Michael Jordan is a famous baseball player.": False,
        "Rafael Nadal is known as the 'King of Clay' in tennis.": True,
        "India won its first Olympic gold medal in 1948.": True,
        "Cristiano Ronaldo is the all-time top scorer for the Portuguese national football team.": True,
        "The movie 'The Godfather' was directed by Francis Ford Coppola.": True,
        "P. V. Sindhu won a silver medal in the 2016 Rio Olympics.": True,
        "Kapil Dev was the captain of the Indian cricket team in the 1983 World Cup.": True,
        "The movie 'La La Land' won the Academy Award for Best Picture in 2017.": False,
        "The Olympic flag has five rings.": True,
        "The movie 'Dangal' is based on the life of wrestler Sushil Kumar.": False,
        "Cristiano Ronaldo has won more Ballon d'Or awards than Lionel Messi.": False,
        "The movie 'The Dark Knight' is part of the Marvel Cinematic Universe.": False,
        "Virat Kohli has captained India in more than 100 Test matches.": False,
        "Saina Nehwal is an Olympic medalist in badminton.": True,
        "The FIFA World Cup is played every four years.": True,
        "Serena Williams has won more Grand Slam singles titles than any other player in the Open Era.": True,
        "Aamir Khan starred in the Bollywood movie '3 Idiots.'": True,
        "The Indian cricket team has won three ICC T20 World Cups.": False,
        "The movie 'Jurassic Park' was directed by James Cameron.": False,
        "Lionel Messi has played for both FC Barcelona and Paris Saint-Germain (PSG).": True,
        "The movie 'Chak De! India' is about cricket.": False,
        "Roger Federer has won 20 Grand Slam titles.": True,
        "The movie 'Slumdog Millionaire' is set in Mumbai, India.": True,
        "Michael Schumacher is a famous Formula 1 driver.": True,
        "The Indian national football team has won the FIFA World Cup.": False,
        "The movie 'Inception' stars Leonardo DiCaprio.": True,
        "Sachin Tendulkar was the captain of the Indian cricket team when they won the 2011 World Cup.": False,
        "Mithali Raj is an Indian cricketer.": True,
        "The Bollywood movie 'Kabhi Khushi Kabhie Gham' was directed by Karan Johar.": True,
        "Tom Hanks starred in the movie 'Forrest Gump.'": True,
        "Rafael Nadal has never won the Australian Open.": False,
        "P. T. Usha is a famous Indian boxer.": False,
        "The movie 'Rocky' is about a professional wrestler.": False,
        "The Indian Premier League (IPL) is a Twenty20 cricket league.": True,
        "The movie 'The Shawshank Redemption' was released in 1994.": True,
        "Sania Mirza is a former World No. 1 in women's singles tennis.": False,
        "The movie 'Gladiator' won the Academy Award for Best Picture.": True,
        "Sunil Chhetri is the all-time leading goal scorer for the Indian football team.": True,
        "The movie 'Raees' stars Salman Khan.": False,
        "Usain Bolt is a famous Jamaican cricketer.": False,
        "The movie 'Black Panther' is part of the Marvel Cinematic Universe.": True,
        "The Indian national hockey team has won multiple Olympic gold medals.": True,
        "Roger Federer has won the French Open multiple times.": False,
        "Priyanka Chopra starred in the movie 'Mary Kom.'": True,
        "Sachin Tendulkar played for Mumbai Indians in the IPL.": True,
        "The movie 'Avatar' was directed by James Cameron.": True,
        "The Indian cricket team won the ICC Champions Trophy in 2013.": True,
        "The movie 'Gone with the Wind' is set during the American Civil War.": True,
        "The Indian national football team is known as the 'Blue Tigers.'": True,
        "The movie 'The Matrix' stars Tom Cruise.": False,
        "Mahendra Singh Dhoni is the captain of the Chennai Super Kings in IPL.": True,
        "The movie 'Zindagi Na Milegi Dobara' was directed by Farhan Akhtar.": False,
        "The movie 'Avengers: Endgame' is the highest-grossing film of all time.": True,
        "The movie 'Dhoom 3' stars Hrithik Roshan.": False,
        "Lewis Hamilton is a famous Formula 1 driver.": True,
        "The movie 'Pulp Fiction' was directed by Quentin Tarantino.": True,
        "The Indian cricket team won its first Test match in 1952.": True,
        "The movie 'The Lion King' is a live-action film.": False,
        "Rafael Nadal has won more French Open titles than any other male player.": True,
        "The movie 'PK' stars Aamir Khan.": True,
        "The Indian national cricket team is nicknamed 'The Men in Blue.'": True,
        "Cristiano Ronaldo has never won the UEFA Champions League.": False,
        "The movie 'The Godfather Part II' won the Academy Award for Best Picture.": True,
        "The Indian hockey team won its last Olympic gold medal in 1980.": True,
        "The movie 'Mission: Impossible' stars Matt Damon.": False,
        "Neeraj Chopra won India's first Olympic gold medal in athletics.": True,
        "The movie 'Dangal' is based on the life of wrestler Geeta Phogat.": True,
        "The movie 'Forrest Gump' was directed by Robert Zemeckis.": True,
        "The Indian cricket team has won the ICC Cricket World Cup three times.": False,
        "The movie 'Harry Potter and the Philosopher's Stone' was released in 2001.": True,
        "The movie 'Thor' stars Chris Hemsworth.": True,
        "The movie 'Gully Boy' was India's official entry to the Oscars in 2020.": True,
        "Lionel Messi has never won a Copa America title.": False,
        "The movie 'Shutter Island' was directed by Quentin Tarantino.": False,
        "The Indian footballer Sunil Chhetri has scored over 50 international goals.": True
    }
    questions = list(dic.keys)
    answ = list(dic.values)


    def answer_wrong(self,answer):
        if self.answer==False:
            print(f"Wrong Answer.\nYour final score is {self.score}")
            j=1
    def ask_q(self,score):
        Q = random.choice(questions)
        A = dic[Q]
        print(Q)
        return A
    def check_answer(self,answer):
        if self.answer==A:
            self.answer = True
        else :
            self.answer = False
            answer_wrong(answer)

j=0
answer = True
score = 0
while(j==0):
    user = Game(score)
    while(answer==True):
         if score >=0:
              ask_q(score)
         ans = input("True or False\n(Type T/F)").lower()
         check_answer(ans)
