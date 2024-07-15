def exhaust_memory():
    try:
        memory_hog = []
        while True:
            # Allocate a large block of memory in each iteration
            memory_hog.append(' ' * 10**6)  # Allocate 1 MB of memory
    except MemoryError:
        print("Memory exhausted!")

if __name__ == "__main__":
    exhaust_memory()
