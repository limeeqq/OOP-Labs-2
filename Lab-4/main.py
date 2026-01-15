from typing import Callable, List

FuelHandlerDelegate = Callable[[str], None]
    #пальне
class Event:
    def __init__(self):
        self._handlers: List[FuelHandlerDelegate] = []

    def add(self, handler: FuelHandlerDelegate):
        self._handlers.append(handler)
        #викликаний методом 
    def invoke(self, message: str):
        for handler in self._handlers:
            handler(message)

class Car:
    def __init__(self, fuel):
        self.fuel = fuel
        self.fuel_empty_event = Event()

    def drive(self, km):
        needed = km * 0.1
        if needed > self.fuel:
            self.fuel_empty_event.invoke(f"бракує пального, треба {needed}л.")
        else:
            self.fuel -= needed
            print(f"проїхали {km} залишок: {self.fuel}л")


def on_fuel_empty_handler(msg: str):
    print(f"обробник події: {msg}")


if __name__ == "__main__":
    print("делегат і лямбда")
    
    SortDelegate = Callable[[list], list]
    #лямбда функція
    my_sort_delegate: SortDelegate = lambda arr: sorted(arr)
    
    numbers = [5, 1, 9, -2]
    print(f"Результат через делегат: {my_sort_delegate(numbers)}")

    print("\n--- Частина 2: Подія ---")
    my_car = Car(fuel=5)

    my_car.fuel_empty_event.add(on_fuel_empty_handler)

    my_car.drive(30)
    my_car.drive(100)