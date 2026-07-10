import psutil

#CPU Usage
def get_cpu():
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

#RAM Usage
def get_ram():
    ram = psutil.virtual_memory()
    return f"RAM Usage: {ram.percent}%"

#Battery an Charging Status
def get_battery():
    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information is unavailable."

    status = "Charging" if battery.power_plugged else "Not Charging"

    return f"Battery: {battery.percent}% ({status})"




"""
psutil.cpu_percent(interval=1)
    -Measures the CPU usage over a period of 1 second.
    -Returns the percentage of CPU currently being used.

interval=1
    -Waits for 1 second before calculating the CPU usage.
    -Provides a more accurate reading.

return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"
    -Returns the CPU usage as a formatted string.
    -Example:
        CPU Usage: 23.5%

ram = psutil.virtual_memory()
    -Retrieves information about the computer's RAM.
    -Returns an object containing:
        total
        available
        used
        free
        percent

ram.percent
    -Returns the percentage of RAM currently in use.

return f"RAM Usage: {ram.percent}%"
    -Returns the RAM usage as a formatted string.
    -Example:
        RAM Usage: 61%

battery = psutil.sensors_battery()
    -Retrieves battery information from the system.
    -Returns None if the computer has no battery.

battery.power_plugged
    -Returns True if the charger is connected.
    -Returns False if the laptop is running on battery power.

status = "Charging" if battery.power_plugged else "Not Charging"
    -Uses a ternary operator.
    -If the charger is connected:
        status = "Charging"
    -Otherwise:
        status = "Not Charging"

battery.percent
    -Returns the current battery percentage.

return f"Battery: {battery.percent}% ({status})"
    -Returns the battery percentage and charging status.
    -Example:
        Battery: 82% (Charging)
        Battery: 47% (Not Charging)


Flow

            Import psutil
                    ↓
    Receive CPU/RAM/Battery request
                    ↓
    Read system information
                    ↓
    Get CPU percentage
                    ↓
    Get RAM percentage
                    ↓
    Get battery information
                    ↓
    Check if battery exists
                    ↓
    Determine charging status
                    ↓
    Return formatted result

==============================
Common psutil Methods & Attributes
==============================

.cpu_percent()
    - A psutil function ,Measures the current CPU usage.
    - Returns the CPU usage as a percentage.

.virtual_memory()
    - Retrieves information about the computer's RAM.
    - Returns an object containing:
        total
        available
        used
        free
        percent

.sensors_battery()
    - Retrieves battery information from the system.
    - Returns a battery object.
    - Returns None if the computer has no battery.

.percent
    - An attribute (property), not a function.
    - Returns a percentage value.
    - Meaning depends on the object.

    Examples:
        ram.percent
            -> Percentage of RAM currently being used.
        battery.percent
            -> Current battery level.

.power_plugged
    - An attribute of the battery object.
    - Indicates whether the charger is connected.
    Returns:
        True  -> Laptop is charging (plugged in)
        False -> Laptop is running on battery power

"""