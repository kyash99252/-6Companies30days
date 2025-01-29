class Solution:
    def findHighAccessEmployees(self, access_times: list[list[str]]) -> list[str]:
        employee_times = {}
        for employee, time in access_times:
            if employee not in employee_times:
                employee_times[employee] = []
            employee_times[employee].append(int(time))

        high_access_employees = []
        for employee, times in employee_times.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i+2] - times[i] < 100:
                    high_access_employees.append(employee)
                    break
        return high_access_employees