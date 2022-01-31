# Telegram TimeTable Bot
__image, overview and description__

## Technologies
[![python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=Python)](https://github.com/python)
[![docker](https://img.shields.io/badge/Docker-000000?style=for-the-badge&logo=Docker)](https://www.docker.com)
[![django](https://img.shields.io/badge/Django-000000?style=for-the-badge&logo=Django)](https://github.com/django/django)


[![telegram](https://img.shields.io/badge/Aiogram-000000?style=for-the-badge&logo=Telegram)](https://github.com/aiogram)
[![pdfschedule](https://img.shields.io/badge/PDFSchedule-000000?style=for-the-badge&logo=Adobe&logoColor=red)](https://github.com/jwodder/schedule)


![postgresql](https://img.shields.io/badge/PostgreSQL-000000?style=for-the-badge&logo=PostgreSQL)
![nginx](https://img.shields.io/badge/Nginx-000000?style=for-the-badge&logo=Nginx&logoColor=green)

## Install App

```bash
git clone git@github.com:shaggy-axel/timetable_bot.git
cd timetable_bot
cat env_sample > .env
# change values in `.env`
docker-compose up -d
```

## How does it work

```
the logic is this:
1. CLIENT | User adds an event
2. CLIENT | The user adds the time when the event will be executed

3. SERVER | An event is created, the time of the events is added to the timetable
               |__ in view: Event get or create (user=request.user, ...)
                  |__ save timetable_updated_date and username to variables
               |
4. SERVER | Updates the change time of the user's timetable
               |__ {user.username}_{timetable_updated_date}.yml is created
                  |__ in view services.create_yml_for_user(user)
               |__ Runs pdfschedule {username}_{timetable_updated_date}.yml
               |__ Remove yml file
               |__ Renders a new "{username}_{timetable_updated_date}.pdf" referenced
                                    "/users/{username}/timetable"
```

## Yaml TimeTable Settings Format
------------------------------------------------
__`name`__ <br>
   **(optional)** The __(possibly multiline)__ text to display in the event's box on
   the schedule
------------------------------------------------
__`days`__ <br>
   The days of the week on which the event occurs, specified as a string of one
   or more of the following abbreviations in any order (optionally with
   intervening whitespace and/or commas):
------------------------------------------------

   |Abbreviation                        |Day
   |------------------------------------|----------
   |`Su` or `Sun`                       |Sunday
   |`M` or `Mo` or `Mon`                |Monday
   |`T` or `Tu` or `Tue`                |Tuesday
   |`W` or `We` or `Wed`                |Wednesday
   |`H` or `R` or `Th` or `Thu`         |Thursday
   |`F` or `Fr` or `Fri`                |Friday
   |`Sa` or `Sat`                       |Saturday
   ------------------------------------------------
   Case is significant.  Unknown abbreviations are ignored.
------------------------------------------------
__`time`__ <br>
   The start & end times of the event in the format `HH:MM - HH:MM`.  Times
   are specified in 24-hour format, the minutes being optional (and optionally
   separated from the hour by a colon or period).
------------------------------------------------
__`color`__ <br>
   *(optional)* The background color of the event's box, given as six
   hexadecimal digits.  The default background color is either grey or, if
   `--color` is in effect, taken from a small palette of basic colors based
   on the event's index.
------------------------------------------------


## Documentation
1. [API]()
2. [Models]()
