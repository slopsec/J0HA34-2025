test_data = [
    "able", "about", "above", "accept", "account", "across", "act", "add", "after", "again",
    "against", "age", "air", "all", "allow", "almost", "alone", "along", "already", "also",
    "always", "am", "among", "amount", "and", "animal", "another", "answer", "any", "appear",
    "area", "arm", "around", "arrive", "art", "ask", "at", "attack", "author", "away",
    "baby", "back", "bad", "bag", "ball", "bank", "base", "be", "bear", "beat",
    "beautiful", "because", "become", "bed", "before", "begin", "behind", "believe", "below", "best",
    "better", "between", "big", "bill", "bird", "bit", "black", "blood", "blue", "board",
    "body", "book", "both", "box", "boy", "break", "bring", "brother", "build", "business",
    "but", "buy", "by", "call", "can", "capital", "car", "care", "carry", "case",
    "cat", "cause", "center", "century", "certain", "chair", "chance", "change", "charge", "check",
    "child", "choose", "church", "city", "class", "clear", "close", "cold", "college", "color",
    "come", "common", "company", "compare", "complete", "computer", "condition", "consider", "continue", "control",
    "cost", "could", "country", "course", "cover", "create", "crime", "cross", "cry", "culture",
    "cup", "current", "cut", "dark", "data", "day", "dead", "deal", "death", "decide",
    "deep", "degree", "develop", "die", "difference", "different", "difficult", "dinner", "direction", "discover",
    "do", "doctor", "dog", "door", "down", "draw", "dream", "drive", "drop", "dry",
    "during", "each", "early", "east", "easy", "eat", "education", "effect", "effort", "eight",
    "either", "else", "end", "energy", "enjoy", "enough", "enter", "entire", "environment", "especially",
    "establish", "even", "evening", "event", "ever", "every", "everyone", "everything", "example", "experience",
    "eye", "face", "fact", "fall", "family", "far", "farm", "fast", "father", "fear",
    "feel", "feeling", "few", "field", "fight", "figure", "fill", "film", "final", "find",
    "fine", "finger", "finish", "fire", "first", "fish", "five", "floor", "follow", "food",
    "foot", "for", "force", "form", "forward", "four", "free", "friend", "from", "front"
]



# air
# class
# from



def binary_search(array, key):
    # Testing only
    runs = 0

    # Search space boundaries (left and right)
    left = 0
    right = len(array) - 1

    # The process repeats for as long as there is something
    # Between left and right
    # In this case it means left <= right
    while left <= right:
        runs +=1 # testing only
        # Select a middle point
        mid = (left + right) // 2

        # 3 possibilites
        # Matching: return the index
        if array[mid] == key:
            print(runs, "runs") # testing only
            return mid
        
        # Non-match, adjust according to above/below
        if array[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    print(runs, "runs") # testing only
    return -1

def main():
    print(binary_search(test_data, "air"))
    print(binary_search(test_data, "class"))
    print(binary_search(test_data, "from"))
    print(binary_search(test_data, "zebra"))

if __name__ == "__main__":
    main()