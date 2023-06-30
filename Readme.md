# Akabac (Assistance Kit Allowing Bamboo Automatic Clocking)
Quick and dirty CLI script to automate BambooHR clocking task.

# Installation
## Requirements
- `hatch` is the [project manager](https://github.com/pypa/hatch) used for the Akabac project.

- A browser `firefox` or `chrome` are supported.

## Usage
- Login to Bamboohr interface on the prefered browser, for example `firefox`
- `hatch run python akabac.py --browser firefox`

This will register all working day of the month with `9:00-12:00` and `13:00-18:00` time period.

If you want to specify the time range you can use the argument `--time-range` and specify `"start-end"` (format: `HH:MM`)

You can except some out of office days (days off, strikes...) with `--except-days` (format: YYYY-MM-DD)

# Manual
```
usage: akabac.py [-h] --browser browser [--time-range TIME_RANGE TIME_RANGE] [--except-days EXCEPT_DAYS [EXCEPT_DAYS ...]]

Clock for the current month (use it at the end of the month)

options:
  -h, --help            show this help message and exit
  --browser browser     Browser used to get the cookie jar.
  --time-range TIME_RANGE TIME_RANGE
                        Time range of the clock in.
  --except-days EXCEPT_DAYS [EXCEPT_DAYS ...]
                        days to except in the registration. (format YYYY-MM-DD)
```