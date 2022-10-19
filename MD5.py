import hashlib
import multiprocessing
import threading


def decrypt(start, end, md5hash):
    print(f"Thread {start} -> {end} has begun")
    result = 0
    while start != end:
        start = str(start).zfill(10)
        result = hashlib.md5(b'start')
        if result == md5hash:
            print(f"{start}: {result}")
        start = int(start) + 1



class MD5:

    def __init__(self, start, end, md5hash):
        processors = multiprocessing.cpu_count()
        for processor in range(processors):
            thread = threading.Thread(target=decrypt, args=(start, end, md5hash))
            thread.start()


# MD5(1, 100, "6eb5cefde6fcb8463cea70880a44eb98")

start = "50"
result = hashlib.md5(b'start')
print(result)