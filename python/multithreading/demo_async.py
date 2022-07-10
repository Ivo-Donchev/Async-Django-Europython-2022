import time
import threading


def func(thread_idx):
    print(f'Thread {thread_idx} started')
    time.sleep(1)
    print(f'Thread {thread_idx} finished')


def main():
    threads = []

    for i in range(1, 5):
        thread = threading.Thread(
            target=lambda: func(i)
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
