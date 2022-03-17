from datetime import datetime


class Employee:
    """ Class for the employee;
        it receives the name and array of dicts for the hours worked.
        Its methods are the calculation of the payments and verification of the hours

        In order to assist the calculation, some interval edges are established (datetime),
        a dictionary converting the days into numbers
        and a dictionary for the wages, transformed to hours (divided by 60),
        from 1 to 6, referencing, respectively, the intervals 1, 2 and 3 for Monday to Friday
        and 1, 2 and 3 for Saturday and Sunday.
    """

    name = None
    payment = None
    interval_edge_1 = datetime(year=1900, month=1, day=1, hour=9, minute=1)
    interval_edge_2 = datetime(year=1900, month=1, day=1, hour=18, minute=1)
    days_dict = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4, "SA": 5, "SU": 6}
    wages = {"W1": 25 / 60, "W2": 15 / 60, "W3": 20 / 60, "W4": 30 / 60, "W5": 20 / 60, "W6": 25 / 60}

    def __init__(self, name, hours_worked):
        self.name = name
        self.hours_worked = hours_worked
        self.payment = self.calculate_payment()

    def calculate_payment(self):
        """
        After passing a validation that the hours are in the correct form,
        a calculation of the payment will be made iterating through the array of worked hours,
        associating it with the intervals and wages(converted to minutes).

        :return: it returns an integer, round (2 decimals)
        representing the payment the employee should receive.
        """
        self.validate_hours()

        aux_pay = 0

        for day_hours in self.hours_worked:

            day_start = datetime.strptime(day_hours["Start"], "%H:%M")
            day_end = datetime.strptime(day_hours["End"], "%H:%M")

            if self.days_dict[day_hours["Day"]] < 5:
                v1, v2, v3 = self.wages["W1"], self.wages["W2"], self.wages["W3"]
            else:
                v1, v2, v3 = self.wages["W4"], self.wages["W5"], self.wages["W6"]

            if day_start < self.interval_edge_1:
                if day_end < self.interval_edge_1:
                    aux_pay = aux_pay + (day_end - day_start).seconds / 60 * v1
                else:
                    aux_pay = aux_pay + (self.interval_edge_1 - day_start).seconds / 60 * v1
                    if day_end < self.interval_edge_2:
                        aux_pay = aux_pay + (day_end - self.interval_edge_1).seconds / 60 * v2
                    else:
                        aux_pay = aux_pay + 120 * v2
                        aux_pay = aux_pay + (day_end - self.interval_edge_2).seconds / 60 * v3
            elif day_start < self.interval_edge_2:
                if day_end < self.interval_edge_2:
                    aux_pay = aux_pay + (day_end - day_start).seconds / 60 * v2
                else:
                    aux_pay = aux_pay + (self.interval_edge_2 - day_start).seconds / 60 * v2
                    aux_pay = aux_pay + (day_end - self.interval_edge_2).seconds / 60 * v3
            else:
                aux_pay = aux_pay + (day_end - day_start).seconds / 60 * v3

        return round(aux_pay, 2)

    def validate_hours(self):
        """
        method designed to validate the array of hours worked.
        checks if the array is null;
        if, in a given day, the schedule ends before it starts;
        if, in a given day, the schedule starts at 00:00 (min should be 00:01).
        if any problems are found, an exception is raised.
        :return: nothing.
        """

        if self.hours_worked == "":
            raise Exception("Invalid hours")

        for day_hours in self.hours_worked:

            day_start = datetime.strptime(day_hours["Start"], '%H:%M')
            day_end = datetime.strptime(day_hours["End"], '%H:%M')

            if day_end < day_start:
                raise Exception("Schedule error for {} on {}".format(self.name, day_hours["Day"]))

            if day_start.hour == 0 and day_start.minute == 0:
                raise Exception("Schedule must begin after 00:00h")
