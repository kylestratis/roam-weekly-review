import sys
import datetime


def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def custom_strftime(fmt, t):
    return t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))


def next_week():
    today = datetime.date.today()
    #    last_monday = today - datetime.timedelta(days=-today.weekday(), weeks=1)
    last_monday = today - datetime.timedelta(days=today.weekday())
    sunday = last_monday + datetime.timedelta(days=6)
    return [
        custom_strftime("%B {S}, %Y", last_monday),
        custom_strftime("%B {S}, %Y", sunday),
    ]


def generate_template():
    week = next_week()
    template = """
# What did I do this week?
  - {{{{[[query]]: {{and: [[DONE]] {{not: [[query]]}} {{between: [[{first_day}]][[{last_day}]]}}}}}}}}
# Review Questions
  - How many high-impact items (priority projects, articles, videos, courses, etc.) on my to-do list was I able to completely close out?
  - What do I want to accomplish in the week ahead?
  - What adjustments do I need to make to ensure I reach my goals?
  - What am I struggling with right now?
  - What do I want to learn by the end of this week?
  - What is one thing I will try that will get me out of my comfort zone?
  - Who can I reach out to for help this week?
# Post-Review Retrospective
  - What went well this week?
  - What could be adjusted?
  - What should I stop doing?
  - What should I start doing?
    """.format(
        first_day=week[0], last_day=week[1]
    )
    return template


s = generate_template()
sys.stdout.write(s)
