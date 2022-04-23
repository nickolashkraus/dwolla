# [Dwolla](https://www.dwolla.com)

[![Travis CI](https://img.shields.io/travis/com/NickolasHKraus/dwolla)](https://travis-ci.org/NickolasHKraus/dwolla)
[![Codecov](https://img.shields.io/codecov/c/github/NickolasHKraus/dwolla)](https://codecov.io/gh/NickolasHKraus/dwolla)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/NickolasHKraus/dwolla/blob/master/LICENSE)

Solution for the technical interview project

## Installation

Make a virtualenv:

```bash
mkvirtualenv dwolla
```

**Note**: The `dwolla` Python Package uses Python 3.7.

Install `dwolla`:

```bash
cd <path/to/dwolla>
pip install -e .
```

## Usage

Set an environment variable for the API key:

```bash
export API_KEY=1337
```

To create an API key, follow the steps [here](https://openweathermap.org/appid).

Use the `--help` option for a full list of possible commands:

```bash
dwolla weather --help
```

**Examples:**

Get the current weather data by city name:

```bash
dwolla weather --name Chicago
```

Get the current weather data by city id:

```bash
dwolla weather --id 4887442
```

Get the current weather data by geographic coordinates:

```bash
dwolla weather --coordinates 41.506149 -87.635597
```

Get the current weather data by ZIP code:

```bash
dwolla weather --zip 60611
```

## Technical Exercise Candidate Instructions

As part of your interview, we request that you complete a technical exercise. The exercise should take roughly an evening to complete.

**Instructions:**

1. Complete the problem in the language of your choosing.
2. Upload your solution to [GitHub](https://github.com/).
3. Use [TravisCI](https://travis-ci.org/) to show your tests pass.

**Your solution will be evaluated on:**

* Completeness (does it work?)
* Quality of all code

**Questions:**

* Send any questions to liz@dwolla.com.

## Grabbing the Weather

Using the OpenWeatherMap API at http://openweathermap.org/current, create a program that prompts for a city name and returns the current temperature for the city.

**Example Output:**

```bash
Where are you? Chicago IL
Chicago weather:
65 degrees Fahrenheit
```

Brian P. Hogan. Exercises for Programmers, P1.0 The Pragmatic Bookshelf, LLC.
