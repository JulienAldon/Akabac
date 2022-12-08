# Bamboo-auto-clocker
Quick and dirty CLI script to automate BambooHR clocking task.

# How to use it ?
**Step 01**: Connect to BambooHR interface (to set your cookie).

**Step 02**: Install hatch on your system

**Step 03**: Activate the environment

```sh
hatch shell
```

**Step 04**: Clock for the whole month using the following command.
```sh
python bamboo_auto_clocker.py --browser <your-browser>
```
`<your-browser>` being the browser you used at `Step 01`

This will register all working day of the month with `9:00-12:00` and `13:00-18:00` time period.

If you want to specify the time range you can use the argument `--time-range` and specify `"start-end"` (format: `HH:MM`)

# When to use it ?
At the end of the month. Else some date may not be registered

# What it doesn't do
Off days and Hollidays, you'll need to suppress them manually in the BambooHR interface.

# Usage
```
bamboo_auto_clocker.py [-h] --browser browser [--time-range TIME_RANGE TIME_RANGE]
```