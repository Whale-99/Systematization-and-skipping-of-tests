import unittest
from runner_test import RunnerTest  # Импортируем наш тестовый класс RunnerTest
from tournament_test import TournamentTest  # Импортируем наш тестовый класс TournamentTest

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.suite = unittest.TestSuite()

        # Добавляем тесты в TestSuite
        self.suite.addTest(unittest.makeSuite(RunnerTest))
        self.suite.addTest(unittest.makeSuite(TournamentTest))

    def test_run(self):
        # Создаём TextTestRunner и указываем verbosity=2 для подробного вывода
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(self.suite)
