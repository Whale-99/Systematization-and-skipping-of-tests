import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        # Создаем объект Runner
        runner = Runner("TestRunner")

        # Вызываем метод walk 10 раз
        for _ in range(10):
            runner.walk()

        # Проверяем, что distance равен 50 (10 * 5)
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        # Создаем объект Runner
        runner = Runner("TestRunner")

        # Вызываем метод run 10 раз
        for _ in range(10):
            runner.run()

        # Проверяем, что distance равен 100 (10 * 10)
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        # Создаем два объекта Runner
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        # У одного объекта вызываем run, у другого walk 10 раз
        for _ in range(10):
            runner1.run()
            runner2.walk()

        # Проверяем, что distance у объектов разное
        self.assertNotEqual(runner1.distance, runner2.distance)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
