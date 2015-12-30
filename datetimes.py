# coding=utf-8
from datetime import timedelta


def helper(d, i, inc):
    while d.weekday() != i:
        d += timedelta(days=inc)
    return d.replace(hour=0, minute=0, second=0, microsecond=0)



def find_days(st, end, d1, d2):
    if st > end or st == end:
        raise ValueError("Start must be before end")
    else:
        _st, _end = helper(st, d1, inc=-1), helper(end, d2, 1)
        secs = (_end - _st).total_seconds() // 86400
        if st.weekday() == d2:
            yield st
        for i in range(int(secs / 7) + 1):
            if st <= _st <= end:
                yield _st
                nxt = _st + timedelta(days=1)
                if nxt <= end:
                    yield nxt
            _st += timedelta(days=7)
    if _st <= end:
        yield _st




def business_days(date, days):
    if days == 0:
        return date
    day = date.weekday()
    if day in {5, 6}:
        date += timedelta(days=7 - day)
        days -= 1
    date += timedelta(days=days / 5 * 7)
    return date + timedelta(days=days % 5)


