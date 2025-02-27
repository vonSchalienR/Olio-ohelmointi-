class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        title = self.name.split(":")[-1].strip()
        return f"Present: {title} ({self.weight}g)"

book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
print("The producer of the present:")
print("The name of the present:", book.name)
print("The weight of the present:", book.weight)
print(book)
