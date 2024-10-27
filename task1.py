import queue
import random
import time

class Request:
    def __init__(self, id):
        self.id = id
    
    def __str__(self):
        return f"Заявка {self.id}"

def generate_request(queue):
    id = random.randint(1, 1000)
    request = Request(id)
    queue.put(request)
    print(f"Створено заявку: {request}")

def process_request(queue):
    if not queue.empty():
        request = queue.get()
        print(f"Обробляється заявка: {request}")
        time.sleep(random.uniform(1, 3))  
        print(f"Заявка {request.id} оброблена.")
    else:
        print("Черга пуста.")

def main_loop():
    queue = queue.Queue()
    try:
        while True:
            generate_request(queue)
            process_request(queue)
            time.sleep(random.uniform(0.5, 2))
    except KeyboardInterrupt:
        print("Вихід з програми.")

if __name__ == "__main__":
    main_loop()
