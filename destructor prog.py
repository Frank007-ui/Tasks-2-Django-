class TempStorage:
    def __init__(self):
        print("Temporary storage created.")
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Item added: {item}")

    def show_items(self):
        print("Current Items:", self.items)

    def __del__(self):
        print("Destructor called....., clearing temporary storage.")
        self.items.clear()
        print("Storage cleared. Object deleted.")



store = TempStorage()

store.add_item("Python")
store.add_item("Django")
store.add_item("AI")
store.add_item("ML")
store.add_item("Cloud")

store.show_items()

del store

print("Program End.")
