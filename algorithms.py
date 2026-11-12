def bubble_sort(data, key):
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if str(arr[j][key]).lower() > str(arr[j + 1][key]).lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def selection_sort(data, key):
    arr = data.copy()

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if str(arr[j][key]).lower() < str(arr[min_index][key]).lower():
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def merge_sort(data, key):
    if len(data) <= 1:
        return data.copy()

    middle = len(data) // 2
    left = merge_sort(data[:middle], key)
    right = merge_sort(data[middle:], key)

    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if str(left[i][key]).lower() <= str(right[j][key]).lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def linear_search(data, search_text):
    search_text = search_text.lower()

    for question in data:
        if search_text in question["question"].lower():
            return question

    return None


def binary_search(data, search_text):
    arr = sorted(data, key=lambda item: item["question"].lower())
    search_text = search_text.lower()

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        current = arr[mid]["question"].lower()

        if current == search_text:
            return arr[mid]
        elif current < search_text:
            low = mid + 1
        else:
            high = mid - 1

    return None