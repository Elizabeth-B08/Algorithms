
# -----------------------------
# Main Program
# -----------------------------
def main():

    dataset_sizes = [100, 1000, 10000]

    print("\nSorting Algorithms Performance Comparison")
    print("-" * 55)

    results = []

    for size in dataset_sizes:

        # Generate random dataset
        data = [random.randint(1, 100000) for _ in range(size)]

        # Test Merge Sort
        merge_time = test_algorithm(merge_sort, data)

        # Test Bubble Sort
        bubble_time = test_algorithm(bubble_sort, data)

        # Store results
        results.append((size, merge_time, bubble_time))

    # Print results table
    print(f"{'Dataset Size':<15}{'Merge Sort (s)':<20}{'Bubble Sort (s)':<20}")
    print("-" * 55)

    for size, merge_time, bubble_time in results:
        print(f"{size:<15}{merge_time:<20.6f}{bubble_time:<20.6f}")

    print("\nTesting Complete.")


# Run program
if __name__ == "__main__":
    main()