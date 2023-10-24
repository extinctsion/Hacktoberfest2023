#include "calendar.h"

class Calendar
{
private:
    int day;
    int month;
    int year;

public:
    Calendar(int d, int m, int y)
    {
        year = max(1, y);

        month = max(1, m);
        month = min(m, 12);

        day = max(1, d);
        day = min(d, getDaysInMonth(month, year));
    }

    // Function to add a certain number of days to the date
    Calendar addDays(int daysToAdd)
    {
        int day = this->day;
        int month = this->month;
        int year = this->year;

        day += daysToAdd;

        while (day > getDaysInMonth(month, year))
        {
            day -= getDaysInMonth(month, year);
            month++;

            if (month > 12)
            {
                month = 1;
                year++;
            }
        }

        return Calendar(day, month, year);
    }

    // Function to get the number of days in the current month
    int getDaysInMonth(int month, int year) const
    {
        static const int daysInMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int days = daysInMonth[month];

        if (isLeapYear(year) && month == 2)
        {
            days++;
        }

        return days;
    }

    // Function to check if the year is a leap year
    bool isLeapYear(int year) const
    {
        if (year % 4 != 0)
        {
            return false;
        }
        if (year % 100 != 0)
        {
            return true;
        }
        return (year % 400 == 0);
    }

    string monthName(int m)
    {
        m = max(1, m);
        m = min(m, 12);

        static const string names[] = {
            "nothing",
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        };

        return names[m];
    }

    // Function to display the date
    string formatDate()
    {
        return monthName(month) + " " + to_string(day) + ", " + to_string(year);
    }
};
