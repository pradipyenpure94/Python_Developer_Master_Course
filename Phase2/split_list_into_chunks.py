"""Split list into chunks."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 4

if chunk_size > 0:
    chunks = []
    index = 0

    while index < len(numbers):
        chunks.append(numbers[index:index + chunk_size])
        index += chunk_size

    print(f"Numbers List Chunks: {chunks}")
else:
    print("Chunk size must be greater than zero.")
