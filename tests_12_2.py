import unittest

class Runner:
  def __init__(self, name, speed=5):
    self.name = name
    self.distance = 0
    self.speed = speed

  def run(self):
    self.distance += self.speed * 2

  def walk(self):
    self.distance += self.speed

  def __str__(self):
    return self.name

  def __eq__(self, other):
    if isinstance(other, str):
      return self.name == other
    elif isinstance(other, Runner):
      return self.name == other.name


class Tournament:
  def __init__(self, distance, *participants):
    self.full_distance = distance
    self.participants = list(participants)

  def start(self):
    finishers = {}
    place = 1
    while self.participants:
      # Проверяем каждого участника, пока не достигнет финиша
      for i, participant in enumerate(self.participants):
        participant.run()
        if participant.distance >= self.full_distance:
          finishers[place] = participant
          place += 1
          self.participants.pop(i) # Удаляем участника из списка
          break # Переход к следующему участнику

    return finishers


class TournamentTest(unittest.TestCase):
  all_results = {}

  @classmethod
  def setUpClass(cls):
    cls.all_results = {}

  def setUp(self):
    self.Usain = Runner("Usain", speed=10)
    self.Andrey = Runner("Andrey", speed=9)
    self.Nick = Runner("Nick", speed=3)

  @classmethod
  def tearDownClass(cls):
    for key, value in sorted(cls.all_results.items()):
      print(f"{key}: {', '.join(str(v) for v in value.values())}") # Изменение вывода

  def test_usain_nick_tournament(self):
    tournament = Tournament(90, self.Usain, self.Nick)
    self.all_results[len(self.all_results) + 1] = tournament.start()
    self.assertTrue(self.all_results[len(self.all_results)][len(self.all_results[len(self.all_results)])] == "Nick")

  def test_andrey_nick_tournament(self):
    tournament = Tournament(90, self.Andrey, self.Nick)
    self.all_results[len(self.all_results) + 1] = tournament.start()
    self.assertTrue(self.all_results[len(self.all_results)][len(self.all_results[len(self.all_results)])] == "Nick")

  def test_usain_andrey_nick_tournament(self):
    tournament = Tournament(90, self.Usain, self.Andrey, self.Nick)
    self.all_results[len(self.all_results) + 1] = tournament.start()
    self.assertTrue(self.all_results[len(self.all_results)][len(self.all_results[len(self.all_results)])] == "Nick")

  def test_usain_andrey_tournament_short_distance(self):
    """Тест для короткой дистанции, чтобы проверить, что Usain приходит первым"""
    tournament = Tournament(20, self.Usain, self.Andrey)
    self.all_results[len(self.all_results) + 1] = tournament.start()
    self.assertTrue(self.all_results[len(self.all_results)][1] == "Usain")

  def test_nick_andrey_tournament_long_distance(self):
    """Тест для длинной дистанции, чтобы проверить, что Nick приходит последним"""
    tournament = Tournament(200, self.Nick, self.Andrey)
    self.all_results[len(self.all_results) + 1] = tournament.start()
    self.assertTrue(self.all_results[len(self.all_results)][len(self.all_results[len(self.all_results)])] == "Nick")

if __name__ == '__main__':
  unittest.main()
