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
    Calendar(int d, int m, int y);

    // Function to add a certain number of days to the date
    Calendar addDays(int daysToAdd);

    // Function to get the number of days in the current month
    int getDaysInMonth(int month, int year) const;

    // Function to check if the year is a leap year
    bool isLeapYear(int year) const;

    // Function to return the name of the given month
    string monthName(int m);

    // Function to display the date
    string formatDate();
};