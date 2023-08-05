import time


def get_current_time():
    today = int(time.time())
    return today


def has_passed_given_days(target_time, days_to_check=10):
    if target_time is None:
        return True

    seconds_in_day = 86400
    seconds_passed = days_to_check * seconds_in_day

    current_time = get_current_time()
    time_ago = current_time - seconds_passed

    return target_time <= time_ago


def merge_and_sum_objects(*objects):
    result = {}
    for obj in objects:
        for key, value in obj.items():
            result[key] = result.get(key, 0) + value
    return result


def multiply_object_values(obj, multiplier):
    for key, value in obj.items():
        if isinstance(value, int) or isinstance(value, float):
            obj[key] = value * multiplier
    return obj


def camel_case_text_to_normal(text):
    return text[0].upper() + text[1:].replace('_', ' ').title()


def object_to_text_column(obj):
    normalized_text_sorted = [[camel_case_text_to_normal(name), value] for name, value in obj.items()]
    normalized_text_sorted.sort()
    text_column = '\n'.join([f'{name}: {value}' for name, value in normalized_text_sorted])
    return text_column
