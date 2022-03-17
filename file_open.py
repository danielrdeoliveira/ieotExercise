import re


class File:
    """ Class to handle the reading of the txt file.
        its methods are one for the reading itself (read_employees) - a classmethod that
        receives the filename and a staticmethod to discard the blank lines while reading the file.
    """

    @classmethod
    def read_employees(cls, filename):
        """ Method opens txt file in reading mode and iterates through the lines;
        an '=' sign should separate the name from the hours - it's tested;
        it also tests if the name already exists in the dict (duplicated names);
        finally, a regex is run in order to generate the array of dicts for the days and hours worked.
        named groups: Day, Start and End.
        :param filename: the name of the txt.file
        :return: a dictionary with the employees as keys and an array for the worked hours as the values
        """

        with open(filename, mode='r') as f:
            employee_dic = {}

            for line in cls.drop_blank_lines(f):
                day_array = []

                try:
                    (name, all_schedules) = line.split('=')
                except ValueError:
                    print("Invalid input format: = sign")
                else:
                    if name in employee_dic.keys():
                        raise Exception("Error: repeated employee name")

                    for x in all_schedules.split(","):
                        try:
                            day_schedule = re.match(r'(?P<Day>[A-Za-z]+)(?P<Start>\d+:\d+)-(?P<End>\d+:\d+)', x)
                            group_day = day_schedule.groupdict()
                            day_array.append(group_day)
                        except ValueError:
                            print("Invalid input format: Day, Start or End")

                    employee_dic[name] = day_array

        return employee_dic

    @staticmethod
    def drop_blank_lines(f):
        """ Static method that simply discards the blank lines from the .txt file
        It works with a generator
        :param f: .txt file
        :return: array of the non-blank lines content
        """
        for lin in f:
            line = lin.rstrip()
            if line:
                yield line
