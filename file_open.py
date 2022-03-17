import re


class File:

    def read_employees(self, filename):

        with open(filename, mode='r') as f:
            employee_dic = {}

            for line in self.drop_blank_lines(f):
                day_array = []

                try:
                    (name, all_schedules) = line.split('=')
                except ValueError:
                    print('Invalid input format')
                else:
                    if name in employee_dic.keys():
                        raise Exception('Error: repeated employee name')

                    for x in all_schedules.split(","):
                        day_schedule = re.match(r'(?P<Day>[A-Za-z]+)(?P<Start>\d+:\d+)-(?P<End>\d+:\d+)', x)
                        group_day = day_schedule.groupdict()
                        day_array.append(group_day)

                    employee_dic[name] = day_array

        return employee_dic

    @staticmethod
    def drop_blank_lines(f):
        for lin in f:
            line = lin.rstrip()
            if line:
                yield line
