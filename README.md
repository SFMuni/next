# Next MUNI

A Python script to fetch and display the next Muni train arrival times for a specific stop using the SFMTA API.

## Features
- Displays the next train arrival times for a specified stop.
- Shows route information, direction, and estimated arrival times.
- Simple setup and usage.

## Requirements
- Python 3.7+
- An SFMTA Developer API key (sign up [here](https://511.org/developers)).

## Installation
1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/SFMuni/next.git
   cd next
   python next.py
   ```

The sample output should look something like this: 

```bash
Upcoming Muni trains for stop ID 12345:
Route: N-Judah, Direction: Outbound, Arrival in: 5 minutes
Route: N-Judah, Direction: Outbound, Arrival in: 15 minutes
Route: N-Judah, Direction: Outbound, Arrival in: 25 minutes
```

## How to Find a Stop ID

Visit the [SFMTA Muni Map](https://www.sfmta.com/maps/muni-service-map) or use Google Maps to find your stop. Look for the stop's unique ID near the schedule or signage.

## Author 

Michael Mendy 
