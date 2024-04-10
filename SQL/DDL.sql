CREATE TABLE Members (
	memberID INT PRIMARY KEY,
	firstName VARCHAR(255),
	lastName VARCHAR(255),
	Country VARCHAR(255),
	Province VARCHAR(255),
	City VARCHAR(255),
	streetName VARCHAR(255),
	streetNumber INT,
	phoneNumber VARCHAR(255),
	emailAddress VARCHAR (255),
	dateOfBirth DATE
	);
	
	CREATE TABLE MemberGoals (
		goalID INT PRIMARY KEY,
    	memberID INT,
    	goalType VARCHAR(255),
    	goalValue VARCHAR(255),
		goalTime TIME,
    	FOREIGN KEY (memberID) REFERENCES Members(memberID)
);

CREATE TABLE PersonalizedDashboards (
    dashboardID INT PRIMARY KEY,
    exerciseRoutine TEXT,
    fitnessAchievement TEXT,
    healthStatistics TEXT,
    progressNotes TEXT,
    memberID INT,
    FOREIGN KEY (MemberID) REFERENCES Members(memberID)
);
	
	CREATE TABLE Trainers (
		trainerID INT PRIMARY KEY,
		firstName VARCHAR(255),
		lastName VARCHAR(255),
		phoneNumber VARCHAR(255),
		availableTimeSlots TEXT

	
	);
	

	CREATE TABLE AdministrativeStaff (
    staffID INT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    dateOfBirth DATE
    
);

	CREATE TABLE Classes (
		classID INT PRIMARY KEY,
    	className VARCHAR(255),
    	trainerID INT,
    	classTime DATE,
    	duration INT,
		staffID INT,
    	FOREIGN KEY (trainerID) REFERENCES Trainers(trainerID)
		FOREIGN KEY (staffID) REFERENCES AdministrativeStaff(staffID)
);
	
	
	CREATE TABLE ClassRegistrations (
    classID INT,
    memberID INT,
    PRIMARY KEY (classID, memberID),
    FOREIGN KEY (classID) REFERENCES Classes(classID),
    FOREIGN KEY (memberID) REFERENCES Members(memberID)
);

CREATE TABLE PersonalTrainingSessions (
    sessionID INT PRIMARY KEY,
    memberID INT,
    trainerID INT,
    sessionTime DATE,
    duration INT,
    FOREIGN KEY (memberID) REFERENCES Members(memberID),
    FOREIGN KEY (trainerID) REFERENCES Trainers(trainerID)
);


CREATE TABLE RoomBookings (
    bookingID INT PRIMARY KEY,
    roomID INT,
    bookingTime DATE,
    duration INT,
	staffID INT,
	FOREIGN KEY (staffID) REFERENCES AdministrativeStaff(staffID)
   
);
	
	
CREATE TABLE EquipmentMaintenance (
    maintenanceID INT PRIMARY KEY,
    equipmentID INT,
    maintenanceDate DATE,
    details TEXT,
	staffID INT,
	FOREIGN KEY (staffID) REFERENCES AdministrativeStaff(staffID)
    
);
	
CREATE TABLE Billing (
    billID INT PRIMARY KEY,
    memberID INT,
    amount DECIMAL(10,2),
    billDate DATE,
    isPaid BIT DEFAULT CAST(0 AS BIT),
    FOREIGN KEY (memberID) REFERENCES Members(memberID)
);

