******Health and Fitness Club Management System******
- This Python script provides a comprehensive management system for a Health and Fitness Club. It interfaces with a PostgreSQL database to handle various operations related to members, trainers, room bookings, maintenance, classes, and billing.

***Features***
- Member Management: Register new members, update member profiles, view member dashboards.
- Training Session Management: Schedule training sessions with trainers.
- Trainer Management: Set availability for trainers and view member profiles.
- Room Booking Management: Add and update room bookings, and view booking information.
- Equipment Maintenance Management: Add and update maintenance records.
- Class Schedule Management: Add and update class schedules.
- Billing and Payment Processing: Add billing records, process payments, and view all billing records.

***Installation***
1. Ensure you have Python installed on your system.
2. Install psycopg2 package using pip:
3. Set up a PostgreSQL database named COMP3005_project.

***Database Setup***
1. Create the necessary tables in your PostgreSQL database using the DDL (Data Definition Language) scripts provided in the SQL directory on GitHub. 
2. Populate the tables with initial data using the DML (Data Manipulation Language) scripts provided in the SQL directory on GitHub.

***Database Configuration***
- Ensure the PostgreSQL database is set up with the required schema. The script connects to the database with the following default credentials:

- dbname: COMP3005_project
- user: postgres
- password: istanbul1958
- host: localhost
- port: 5432
- These credentials can be modified in the connect_to_db function within the script.

***Contributions***
- Pietro Adamvoski

***Video***
- https://www.youtube.com/watch?v=LrnTo0-lZQ4
  

