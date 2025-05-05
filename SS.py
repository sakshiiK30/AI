import matplotlib.pyplot as plt
import matplotlib.animation as animation

def selection_sort_visual(arr, bar_rects, text, ax):
    n = len(arr)
    def update(frame):
        i, j, min_idx = frame
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)
            rect.set_color('skyblue')
        if i < n:
            bar_rects[min_idx].set_color('red')  # current minimum
            bar_rects[j].set_color('yellow')     # element being compared
            bar_rects[i].set_color('green')      # current sorted position
        text.set_text(f"Comparing index {j} and min index {min_idx}")

    frames = []
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            frames.append((i, j, min_idx))
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        frames.append((i, i, i))  # reflect the swap

    ani = animation.FuncAnimation(fig, update, frames=frames, repeat=False, blit=False, interval=600)
    plt.show()

# ---- Input from user ----
arr = []
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(n):
    val = int(input(f"Element {i+1}: "))
    arr.append(val)

# ---- Setup plot ----
fig, ax = plt.subplots()
ax.set_title("Selection Sort Visualization")
bar_rects = ax.bar(range(len(arr)), arr, color='skyblue')
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
ax.set_ylim(0, max(arr) * 1.1)

selection_sort_visual(arr.copy(), bar_rects, text, ax)

OUTPUT:
Enter the number of elements: 5
Enter the elements:
Element 1: 34
Element 2: 77
Element 3: 56
Element 4: 98
Element 5: 29
