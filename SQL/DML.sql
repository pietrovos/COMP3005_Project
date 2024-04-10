-- Inserting data into Members
INSERT INTO Members VALUES 
(1, 'John', 'Doe', 'USA', 'California', 'Los Angeles', 'Main St', 123, '123-456-7890', 'johndoe@email.com', '1980-01-01'),
(2, 'Jane', 'Smith', 'Canada', 'Ontario', 'Toronto', 'Queen St', 456, '234-567-8901', 'janesmith@email.com', '1990-02-02');

-- Inserting data into MemberGoals
INSERT INTO MemberGoals VALUES 
(1, 1, 'Weight Loss', '5kg', '12:00:00'),
(2, 2, 'Muscle Gain', '10kg', '15:00:00');

-- Inserting data into PersonalizedDashboards
INSERT INTO PersonalizedDashboards VALUES 
(1, 'Routine A', 'Achievement B', 'Stats C', 'Notes D', 1),
(2, 'Routine E', 'Achievement F', 'Stats G', 'Notes H', 2);

-- Inserting data into Trainers
INSERT INTO Trainers VALUES 
(1, 'Emily', 'Johnson', '345-678-9012', 'Available most afternoons'),
(2, 'Michael', 'Brown', '456-789-0123', 'Available mornings and evenings');

-- Inserting data into AdministrativeStaff
INSERT INTO AdministrativeStaff VALUES 
(1, 'Alice', 'Williams', '1975-03-03'),
(2, 'David', 'Jones', '1985-04-04');

-- Inserting data into Classes
INSERT INTO Classes VALUES 
(1, 'Yoga Basics', 1, '2024-04-15', 60, 1),
(2, 'Advanced Cardio', 2, '2024-04-16', 90, 2);

-- Inserting data into ClassRegistrations
INSERT INTO ClassRegistrations VALUES 
(1, 1),
(2, 2);

-- Inserting data into PersonalTrainingSessions
INSERT INTO PersonalTrainingSessions VALUES 
(1, 1, 1, '2024-05-01', 60),
(2, 2, 2, '2024-05-02', 90);

-- Inserting data into RoomBookings
INSERT INTO RoomBookings VALUES 
(1, 101, '2024-06-01', 120, 1),
(2, 102, '2024-06-02', 150, 2);

-- Inserting data into EquipmentMaintenance
INSERT INTO EquipmentMaintenance VALUES 
(1, 501, '2024-07-01', 'Routine checkup', 1),
(2, 502, '2024-07-02', 'Repair required', 2);

-- Inserting data into Billing
INSERT INTO Billing VALUES 
(1, 1, 100.00, '2024-08-01', CAST(0 AS BIT)),
(2, 2, 200.00, '2024-08-02', CAST(0 AS BIT));
