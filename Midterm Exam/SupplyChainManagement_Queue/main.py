from ui.console_interface import ConsoleInterface

def main():
    warehouse_capacity = 10  # You can change this value as needed
    ui = ConsoleInterface(warehouse_capacity)
    ui.run()

if __name__ == "__main__":
    main()