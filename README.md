# Prettify JSON

This program is for turning shitty code in json files to pretty view

# Quickstart

Example of script launch on Linux, Python 3.x:

```#!bash

$ python pprint_json.py <path to file>

To launch on Windows, Python 3.x:

Press "Win+R", write cmd and press "Enter". Go to path to pprint_json using "cd". Then use the same command like in previous example with Linux:

> python pprint_json.py <path to file>

# Output example

[
    {
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1,
        "Cells": {
            "global_id": 14371450,
            "Name": "Ароматный Мир",
            "IsNetObject": "да",
            "OperatingCompany": "Ароматный Мир",
            "TypeService": "реализация продовольственных товаров",
            "AdmArea": "Западный административный округ",
            "District": "район Кунцево",
            "Address": "улица Академика Павлова, дом 10",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "WorkingHours": [
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "понедельник"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "вторник"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "среда"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "четверг"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "пятница"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "суббота"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "воскресенье"
                }
            ],
            "ClarificationOfWorkingHours": null,
            "geoData": {
                "type": "Point",
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ]
            }
        }
    }
]

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
