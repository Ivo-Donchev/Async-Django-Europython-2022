import multiprocessing


def func(process_idx):
    """
    A dummy loop to simulate heavy CPU usage
    """
    total_iterations = 100000000
    step = total_iterations / 10

    for i in range(1, total_iterations):
        if i % step == 0:
            print(f'Process {process_idx} reached {(i / step) * 10} %')

        pass


def main():
    processes = []

    for i in range(1, 5):
        process = multiprocessing.Process(
            target=lambda: func(i)
        )
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


if __name__ == '__main__':
    main()
