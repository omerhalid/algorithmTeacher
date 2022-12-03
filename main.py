import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Algorithm Information")
        self.geometry("400x200")

        self.label = tk.Label(self, text="Select an algorithm:")
        self.label.pack()

        self.algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
        self.selected_algorithm = tk.StringVar(self)
        self.selected_algorithm.set(self.algorithms[0])

        self.algorithm_menu = tk.OptionMenu(self, self.selected_algorithm, *self.algorithms)
        self.algorithm_menu.pack()

        self.button = tk.Button(self, text="Show Information", command=self.show_info)
        self.button.pack()

        self.description_label = tk.Label(self, text="")
        self.description_label.pack()

        self.configure(bg="#f0f0f0")
        self.label.configure(bg="#f0f0f0")
        self.algorithm_menu.configure(bg="#ffffff")
        self.button.configure(bg="#ffffff")
        self.description_label.configure(bg="#f0f0f0")

    def show_info(self):
        algorithm = self.selected_algorithm.get()
        if algorithm == "Bubble Sort":
            message = "Bubble sort repeatedly compares adjacent elements and swaps them if they are in the wrong order."
        elif algorithm == "Selection Sort":
            message = "Selection sort divides the input list into a sorted and unsorted sublist, and repeatedly selects the minimum element from the unsorted sublist and appends it to the sorted sublist."
        elif algorithm == "Insertion Sort":
            message = "Insertion sort takes elements from the list one by one and inserts them in their correct position into a new sorted list."
        elif algorithm == "Merge Sort":
            message = "Merge sort is a divide and conquer algorithm that uses recursive calls to continuously split the input list into smaller sublists until the base case (a list of length 1 or 0) is reached."
        elif algorithm == "Quick Sort":
            message = "Quick sort uses partitioning to divide the input list into smaller sublists and then recursively sorts the sublists until the base case (a list of length 1 or 0) is reached."

        self.description_label.configure(text=message)

if __name__ == "__main__":
    app = App()
    app.mainloop()
