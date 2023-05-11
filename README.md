# Cinema Hall Ticket Booking System

This repository contains code for a Cinema Hall ticket booking management system using Python and concepts of OOP.
Upon running, there will be an opening message "Welcome to Star Sineplex, Rajshahi"
1. VIEW ALL SHOWS TODAY
2. VIEW AVAILABLE SEATS
3. BOOK TICKETS
4. EXIT

And an prompt will be shown to let user choose among four options shown above.
If the user choose 1, he'll see something like this:

SHOW ID                              SHOW NAME                              SHOW TIME
-------------------------------------------------------------------------------------
ae123                                BLACK ADAM                              12:00 AM
bc245                                SPIDER-MAN                              03:00 PM
zp785                                INCEPTION                               06:00 PM
-------------------------------------------------------------------------------------

If the user choose option 2, he'll be prompt to enter show id, upon entering show id, the terminal will show something like this:

AVAILABLE SEATS ARE SHOWN BELOW
[N.B: XX MEANS ALREADY BOOKED SEAT(S)]

SHOW ID: bc245     ||     SHOW NAME: SPIDER-MAN     || TIME: 03:00 PM
----------------------------------------------------------------------
A1               A2               A3               A4               A5
B1               B2               B3               B4               B5
C1               C2               C3               C4               C5
D1               D2               D3               D4               D5
E1               E2               E3               E4               E5
----------------------------------------------------------------------

Upon choosing option 3, the user can enter show id, if the id matches the terminal will show him the movie name and time of the show. Then user has to enter his name and phone number to book show. He can choose any number of seats he want, and upon entering he'll book the show, and purchase information will be shown.

--------------------PURCHASE INFORMATION-------------------------
CUSTOMER NAME: yu                         PHONE NUMBER: 99
SHOW NAME: SPIDER-MAN                         TIME: 03:00 PM
HALL NO: A10
3 BOOKED SEATS ARE: D4 D3 D2

Upon entering option 4, user can quit the application.
