import csv
import os

"""
Focus: Safe File I/O and Custom Exception Handling.
"""

def manage_files():
    filename = "demo.csv"
    
    # 1. Writing with Context Manager (Safe handling)
    data = [["ID", "Name"], [1, "Python"], [2, "Core"]]
    
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print(f"File '{filename}' created successfully.")

        # 2. Reading and Clean-up
        if os.path.exists(filename):
            with open(filename, mode='r') as f:
                print("Content preview:", f.readline().strip())
            
            os.remove(filename) # Clean up after demo
            print("File cleaned up.")

    except (IOError, OSError) as e:
        print(f"Error handling file operations: {e}")

if __name__ == "__main__":
    manage_files()