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
# zebra

# The list needs to be sorted!
def binary_search(list_ref, search_term):
    # Testing only
    runs = 0

    # Track the start point and end point
    start = 0
    end = len(list_ref) - 1

    while start <= end:
        # Testing
        runs+=1

        # Mid point (start + end) / 2 truncated
        midpoint = (start + end) // 2

        # If midpoint matches
        if list_ref[midpoint] == search_term:
            print("runs:", runs)
            return midpoint
        
        # If search term is greater than midpoint
        # Set start to element after midpoint
        # Mirror logic with end point if search term
        # is lower
        if list_ref[midpoint] > search_term:
            end = midpoint - 1
        else:
            start = midpoint + 1

    # If nothing found return -1
    print("runs:", runs)
    return - 1

    # For comparison
    def linear_search(list_ref, search_term):
        for index, item in enumerate(list_ref):
            if item == search_term:
                return index
        return -1


def main():
    # Test runs
    words = ['air', 'class', 'from', 'zebra']

    for w in words:
        print(w, "position:", binary_search(test_data, w))
        

        
if __name__ == "__main__":
    main()
