import multiprocessing
from autocut import main

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main.main()
