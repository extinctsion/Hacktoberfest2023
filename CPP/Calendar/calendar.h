#ifndef CALENDAR_H
#define CALENDAR_H

#include <string>

using namespace std;

class Calendar
{
private:
    int day;
    int month;
    int year;

public:
    // Constructor to initialize Calendar object with given Date, Month and Year
    Calendar(int, int, int);

    // Function to add a certain number of days to the date
    Calendar addDays(int);

    // Function to get the number of days in the current month
    int getDaysInMonth(int, int) const;

    // Function to check if the year is a leap year
    bool isLeapYear(int) const;

    // Function to return the name of the given month
    string monthName(int);

    // Function to display the date
    string formatDate();
};

#endif // CALENDAR_H