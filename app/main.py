class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                total_income += wash_cost
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        result = 0.0
        if self.distance_from_city_center == 0.0 or car.clean_mark >= self.clean_power:
            return 0.0

        result = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating
        result /= self.distance_from_city_center
        if result > 0:
            return round(result, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> float:
        count_rate = self.average_rating * self.count_of_ratings
        new_rate = round(count_rate, 1) + rate
        new_count_of_ratings = self.count_of_ratings + 1
        new_average_rate = new_rate / new_count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(new_average_rate, 1)
        new_average_rate = round(new_rate) / new_count_of_ratings
        return new_average_rate
