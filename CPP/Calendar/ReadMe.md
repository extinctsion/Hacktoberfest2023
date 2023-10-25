# Calendar Class
In order to use this class in your `main.cpp` file, use this Syntax

```cpp
Calendar myDate(25, 10, 2023); // Initialize with a date (day, month, year)
cout << myDate.formatDate() << "\n";

int daysToAdd = 15;
Calendar newDate = myDate.addDays(daysToAdd); // Add 15 days
cout << myDate.formatDate() << "\n";
cout << newDate.formatDate() << "\n";
```

We can compile the `main.cpp` file by
```
$ g++ .\main.cpp .\Calendar\calendar.cpp
```

And, we would get the following output
```
October 25, 2023
October 25, 2023
November 9, 2023
```