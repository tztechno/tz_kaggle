test_audio_paths = [str(TEST / f"{aid}.mp3") for aid in test["id"].values]

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
unique_numbers = {x for x in numbers}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

fruits = ['apple', 'banana', 'cherry']
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}


