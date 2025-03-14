def sort_dates(dates):
    day = []
    month = []
    year = []
    date = []
    sorted_date = []

    for i in dates:
        i = i.split("-")
        month.append(i[0])
        day.append(i[1])
        year.append(i[2])

    for i in range(len(day)):
        date.append((int(year[i]), int(month[i]), int(day[i])))
    sorted_dates = sorted(date)

    year.clear()
    day.clear()
    month.clear()

    for i in sorted_dates:
        i = list(i)
        year.append(i[0])
        month.append(i[1])
        day.append(i[2])

    for i in range(len(year)):
        sorted_date.append(f"{month[i]}-{day[i]}-{year[i]}")
    formatted_dates = [f"{str(month).zfill(2)}-{str(day).zfill(2)}-{year}" for year, month, day in sorted_dates]
    return formatted_dates
    

