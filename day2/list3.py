def get_passing_scores(score_list, threshold):
    return [i for i in score_list if i >= threshold]

print(get_passing_scores([55, 90, 82, 30], 70))


celsius = [0, 10, 20, 30, 40]

fahrenheit = [(c*9/5) + 32 for c in celsius]

print(fahrenheit)

raw_data = [" 10 ", " 20", "30 ", "ERROR", " 40"]

clean_numbers = [int(i.strip()) for i in raw_data if i.strip() != "ERROR"]

print(clean_numbers)

words = ["apple", "hi", "banana"]

def largerwords(words):
    return [word for word in words if len(word) > 3]

print(largerwords(words))