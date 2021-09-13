#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    return (a+b+c)/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    degre_normal = angle_degs + angle_mins/60 + angle_secs/3600
    return (degre_normal/360)*2*math.pi


def to_degrees(angle_rads: float) -> tuple:
    degrees = math.degrees(angle_rads)
    degree_minutes = (degrees % 1) * 60
    degree_secondes = (degree_minutes % 1) * 60
    return degrees - degree_minutes, degree_minutes - degree_secondes, degree_secondes


def to_celsius(temperature: float) -> float:
    return (temperature - 32)/(9/5)


def to_farenheit(temperature: float) -> float:
    return (temperature * (9/5)) + 32


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
