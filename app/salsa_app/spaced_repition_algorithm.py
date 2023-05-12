def spaced_repetition(form):
    
    # handles if item has no histroy by replacing with zero
    easiness_factor = int(form.cleaned_data['easiness_factor_remembering'] or 0)
    repetition = int(form.cleaned_data['repetition'] or 0)
    interval = int(form.cleaned_data['interval'] or 0)
    quality = int(form.cleaned_data['difficulty_remembering'])

    smallest_repition_minutes = 5
    minutes_in_a_day = 1440
    smallest_repition_days =  smallest_repition_minutes/ minutes_in_a_day
    
    if quality < 2:
        repetition = smallest_repition_days
    else:
        repetition += 1

    easiness_factor = max(1.3, easiness_factor + 0.1 - (4 - quality) * (0.08 + (4 - quality) * 0.02))

    if repetition == 1:
        interval = 1
    elif repetition == 2:
        interval = 6
    else:
        interval = round(interval * easiness_factor)

    return interval, easiness_factor, repetition
