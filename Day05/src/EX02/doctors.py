import threading
from time import sleep

class Screwdriver:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.lock: threading.Lock = threading.Lock()

    def lift(self) -> None:
        sleep(0.5)
        self.lock.acquire()

    def put(self) -> None:
        sleep(0.5)
        self.lock.release()


class Doctor(threading.Thread):
    def __init__(self, id: int, left_screwdriver: Screwdriver, right_screwdriver: Screwdriver) -> None:
        super().__init__()
        self.id: int = id
        self.left_screwdriver: Screwdriver = left_screwdriver
        self.right_screwdriver: Screwdriver = right_screwdriver

    def run(self) -> None:
        self.left_screwdriver.lift()
        self.right_screwdriver.lift()
        sleep(1.25)
        print(f"Doctor {self.id}: BLAST!")
        self.left_screwdriver.put()
        self.right_screwdriver.put()


def main() -> None:
    count_of_doctors: int = 5
    screwdrivers: list[Screwdriver] = [Screwdriver(i) for i in range(count_of_doctors)]
    doctors: list[Doctor] = [Doctor(i + 9, screwdrivers[i], screwdrivers[i + 1]) for i in range(count_of_doctors - 1)]
    last_doctor: Doctor = Doctor(count_of_doctors - 1 + 9, screwdrivers[count_of_doctors - 1], screwdrivers[0])

    for doctor in doctors:
        doctor.start()
    for doctor_thread in doctors:
        doctor_thread.join()
    last_doctor.start()

if __name__ == '__main__':
    main()
