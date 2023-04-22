def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    sent_in_spanish_list = sentence.split()
    gen_eng = (words[word_span] for word_span in sent_in_spanish_list)
    sent_in_eng_list = [next(gen_eng) for i in range(len(sent_in_spanish_list))]
    return " ".join(sent_in_eng_list)


#print(translate("el gato esta en la casa"))


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#prime_generator = (n for n in range(10 ** 10) if is_prime(n))
#for prime_number in prime_generator:
    #print(prime_number)


def first_prime_over(n):
    gen_prime = (i for i in range(n * n) if is_prime(i))
    for prime_num in gen_prime:
        if prime_num > n:
            return prime_num


#print(first_prime_over(1000000))

def parse_ranges(ranges_string):
    """:Todo: make string to list, each range to a list - still in string
    :Todo: figure first and second numbers and enter to a list
    :Todo: make generator that pruduce only numbers in the ranges """
    """
    :Fuction: it take ranges of numbers in string like: "1-2,4-4,8-10" and genrate a genertor that will produce
    numbers in these ranges.
    :param1 - ranges_string: string of ranges like above
    :type param1 - string_ranges: string
    :return: generator that produce the numbers in type int, of the ranges of param1
    :rtype: generator"""
    list_of_ranges_in_string = ranges_string.split(",")
    gen_list_of_two_nums = ([int(range_string.split("-")[0]),int(range_string.split("-")[1])] for
                            range_string in list_of_ranges_in_string)
    #list_of_numbers = [[int(range_string.split("-")[0]), int(range_string.split("-")[1])] for range_string in
                       #list_of_ranges_in_string]
    final_gen = (num for start, stop in gen_list_of_two_nums for num in range(start, (stop + 1)))
    #gen_ranges = (i for list_of_two_nums in list_of_numbers for i in range(list_of_two_nums[0], (list_of_two_nums[1]) + 1))
    return final_gen

#print(list(parse_ranges("0-0,4-8,20-21,43-45")))

def get_fibo():
    """
    :Function: generate a generator of fibonachi
    :return: generator that gives fibonachi numbers
    :rtype: generator
    :Todo: dezine the generator to produce
    """
    first = 0
    sec = 1
    yield first
    yield sec
    while True:
        sum = first + sec
        yield sum
        first = sec
        sec = sum


#fibo = get_fibo()
#for i in range(90):
    #print(next(fibo))


def gen_secs():
    sec = 0
    while sec < 60:
        yield sec
        sec += 1
        if sec == 60:
            sec = 0

def gen_minutes():
    min = 0
    while min < 60:
        yield min
        min += 1
        if min == 60:
            min = 0

def gen_hours():
    hour = 0
    while hour < 24:
        yield hour
        hour += 1
        if hour == 24:
            hour = 0
def gen_time():
    num_of_sec = 0
    corrent_sec = 0
    corrent_min = 0
    corrent_hours = 0
    secs = gen_secs()
    mins = gen_minutes()
    hours = gen_hours()
    while True:
        corrent_sec = next(secs)
        if num_of_sec % 60 == 0:
            corrent_min = next(mins)
        #for num3 in range((num_of_sec // 3600) % 24):
        if num_of_sec % 3600 == 0:
            corrent_hours = next(hours)
        if corrent_hours < 10:
            number_of_hours_str = f"0{corrent_hours}"
        else:
           number_of_hours_str = str(corrent_hours)
        if corrent_min < 10:
            number_of_mins_str = f"0{corrent_min}"
        else:
            number_of_mins_str = str(corrent_min)
        if corrent_sec < 10:
            number_of_secs_str = f"0{corrent_sec}"
        else:
            number_of_secs_str = str(corrent_sec)
        yield f"{number_of_hours_str}:{number_of_mins_str}:{number_of_secs_str}"
        num_of_sec += 1


def gen_time_not_good():
    count_to_sixty_sec = -1
    count_to_sixty_min = 0
    count_twenty_four_hours = 0
    seconds = gen_secs()
    minutes = gen_minutes()
    hours = gen_hours()
    day = 1
    while True:
        next(seconds)
        count_to_sixty_sec += 1
        if count_to_sixty_sec == 60:
            count_to_sixty_min += 1
            next(minutes)
            count_to_sixty_sec = 0
        if count_to_sixty_min == 60:
            count_twenty_four_hours += 1
            next(hours)
            count_to_sixty_min = 0
        if count_twenty_four_hours == 24:
            count_twenty_four_hours = 0
            day += 1
        if count_twenty_four_hours < 10:
            number_of_hours_str = f"0{count_twenty_four_hours}"
        else:
          number_of_hours_str = str(count_twenty_four_hours)
        if count_to_sixty_min < 10:
            number_of_mins_str = f"0{count_to_sixty_min}"
        else:
            number_of_mins_str = str(count_to_sixty_min)
        if count_to_sixty_sec < 10:
            number_of_secs_str = f"0{count_to_sixty_sec}"
        else:
            number_of_secs_str = str(count_to_sixty_sec)
        yield f"{number_of_hours_str}:{number_of_mins_str}:{number_of_secs_str}"


def gen_years(start=2023):
    while True:
        yield start
        start += 1


def gen_months():
    month = 1
    while month < 13:
        yield month
        month += 1
        if month == 13:
            month = 1


def gen_days(month, years):
    day = 1
    leap_year = False
    if years % 4 == 0:
        if years % 100 == 0 and years % 400 != 0:
            leap_year = False
        else:
            leap_year = True
    if month in [1, 3, 5, 7, 8, 10, 12]:
        while day < 32:
            yield day
            day += 1
            if day == 32:
                day = 1
    if month in [4, 6, 9, 11]:
        while day < 31:
            yield day
            day += 1
            if day == 31:
                day = 1
    if month == 2:
        if leap_year:
            while day < 30:
                yield day
                day += 1
                if day == 30:
                    day = 1
        else:
            while day < 29:
                yield day
                day += 1
                if day == 29:
                    day = 1


def gen_date():
    num_of_sec = 0
    current_day = 1
    current_month = 1
    current_year = 2023
    days = gen_days(current_month, current_year)
    months = gen_months()
    years = gen_years(current_year)
    time = gen_time()
    next(days)
    next(months)
    next(years)
    while True:
        current_time = next(time)
        if num_of_sec % 86400 == 0 and num_of_sec > 0:
            current_day = next(days)
            if current_day == 1 and current_time == "00:00:00":
                current_month = next(months)
                days = gen_days(current_month, current_year)
                next(days)
                if current_month == 1 and current_day == 1 and time == "00:00:00":
                    current_year = next(years)
                    days = gen_days(current_month, current_year)
                    next(days)
        if current_day < 10:
            current_day_str = f"0{current_day}"
        else:
           current_day_str = str(current_day)
        if current_month < 10:
            current_month_str = f"0{current_month}"
        else:
            current_month_str = str(current_month)
        yield f"{current_day_str}:{current_month_str}:{current_year}  {current_time}"
        num_of_sec += 1


def gen_date1():
    time = gen_time_not_good()
    count_days = 1
    count_months = 1
    count_years = 2023
    leap_year = False
    days = gen_days(count_months, leap_year)
    months = gen_months()
    years = gen_years()
    while True:
        current_time = next(time)
        if current_time == "00:00:00":
            count_days += 1
            next(days)
        if count_months in [1, 3, 5, 7, 8, 10, 12] and count_days == 31:
            count_months += 1
            count_days = 0
            next(months)
        if count_months in [4, 6, 9, 11] and count_days == 30:
            count_months += 1
            count_days = 0
            next(months)
        if count_years % 4 == 0:
            if count_years % 100 == 0 and count_years % 400 != 0:
                leap_year = False
            else:
                leap_year = True
        if count_months == 2 and leap_year and count_days == 29:
            count_months += 1
            count_days = 0
            next(months)
        if count_months == 2 and not leap_year and count_days == 28:
            count_months += 1
            count_days = 0
            next(months)
        if count_months == 13:
            count_years += 1
            next(years)
            count_months = 1
        if count_days < 10:
            number_of_days_str = f"0{count_days}"
        else:
            number_of_days_str = str(count_days)
        if count_months < 10:
            number_of_months_str = f"0{count_months}"
        else:
            number_of_months_str = str(count_months)
        yield f"{number_of_days_str}:{number_of_months_str}:{count_years}  {current_time}"


date = gen_date()
for i in range(86400 + 1):
    next(date)
print(next(date))

#days = gen_years()
#for i in range(9):
 #   print(next(days))