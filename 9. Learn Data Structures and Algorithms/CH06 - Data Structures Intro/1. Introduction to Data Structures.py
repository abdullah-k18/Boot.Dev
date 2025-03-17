def count_marketers(job_titles):
    count = 0
    title = "marketer"
    for i in range(len(job_titles)):
        if (title in job_titles[i]) or (title.upper() in job_titles[i]) or (title.title() in job_titles[i]):
            count += 1
    return count
