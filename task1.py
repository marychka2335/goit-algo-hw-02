import queue
import random
import time

class Request:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Заявка {self.id}"

def generate_request(request_queue):
    id = random.randint(1, 1000)
    request = Request(id)
    request_queue.put(request)
    print(f"Створено заявку: {request}")

def process_request(request_queue):
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється заявка: {request}")
        time.sleep(random.uniform(1, 3))
        print(f"Заявка {request.id} оброблена.")
    else:
        print("Черга пуста.")

def main_loop(max_requests=10):
    request_queue = queue.Queue()
    requests_generated = 0
    try:
        while requests_generated < max_requests:
            generate_request(request_queue)
            process_request(request_queue)
            requests_generated += 1
            time.sleep(random.uniform(0.5, 2))
    except KeyboardInterrupt:
        print("Вихід з програми.")
    print(f"Обробка завершена після {requests_generated} заявок.")

if __name__ == "__main__":
    main_loop()
