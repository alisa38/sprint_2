class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        """Начисляет баллы в зависимости от занятого места."""
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0
        return 101 - place  # 1-е место = 100 баллов, 100-е = 1 балл


class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        """Начисляет баллы за количество метров."""
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0
        return meters * 0.5  # 1 метр = 0.5 балл


class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        """Возвращает общее количество баллов за место и метры."""
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total


# ===== Пример использования =====
if __name__ == "__main__":
    total_points = TotalPoints()

    # Примеры расчёта
    print("Пример 1:")
    print(total_points.get_total_points(300, 10))  # 300 м и 10-е место

    print("\nПример 2:")
    print(total_points.get_total_points(150, 1))   # 150 м и 1-е место

    print("\nПример 3 (ошибка):")
    print(total_points.get_total_points(-50, 200)) # Ошибочные данные