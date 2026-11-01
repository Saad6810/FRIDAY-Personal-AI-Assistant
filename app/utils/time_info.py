import datetime


def get_time_information() -> str:
    """"Return a few lines of text: day name, date, month, year, and time (24h)."""
    now = datetime.datetime.now()
    return(
        f"Current Real-time Informaton:\n"
        f"Day: {now.strftime('%A')}\n"
        f"Date: {now.strftime('%d')}\n"
        f"Month: {now.strftime('%B')}\n"
        f"Year: {now.strftime('%Y')}\n"
        f"Time: {now.strftime('%H')} hours, {now.strftime('%M')} minutes, {now.strftime('%S')} seconds\n"
    )