# app.py
import sys

def main():
    name = "World"
    print(f'Hello, {name}!')
    sys.stdout.flush()  # Ensure stdout buffer is flushed

if __name__ == "__main__":
    main()

