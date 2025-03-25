CREATE TABLE People (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name NVARCHAR(100) NOT NULL,
    age INT CHECK (age >= 0) -- Ensure age is non-negative
);

CREATE TABLE Vehicle (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plate NVARCHAR(100) UNIQUE NOT NULL, -- Unique vehicle plate
    color NVARCHAR(100),
    vehicle_type ENUM('ô tô', 'xe máy'), -- Define vehicle type
    id_people INT,
    FOREIGN KEY (id_people) REFERENCES People(id) ON DELETE CASCADE
);

-- Sub-table for cars
CREATE TABLE Oto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vehicle_id INT UNIQUE, -- Link to Vehicle table
    seat INT,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle(id) ON DELETE CASCADE
);

-- Sub-table for motorcycles
CREATE TABLE XeMay (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vehicle_id INT UNIQUE, -- Link to Vehicle table
    type NVARCHAR(100), -- Type of motorcycle (automatic, manual, electric...)
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle(id) ON DELETE CASCADE
);

CREATE TABLE Accounts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_people INT NOT NULL,
    display_name NVARCHAR(100),
    userName NVARCHAR(100) UNIQUE NOT NULL,
    passWord NVARCHAR(255) NOT NULL, -- Store hashed password
    FOREIGN KEY (id_people) REFERENCES People(id) ON DELETE CASCADE
);

CREATE TABLE Street (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name NVARCHAR(100),
    tdtdxm INT,
    tdtdot INT
);

CREATE TABLE Violation (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_street INT,
    plate_vehicle NVARCHAR(100),
    name NVARCHAR(50),
    date DATE,
    time DATETIME,
    mucPhat INT,
    FOREIGN KEY (id_street) REFERENCES Street(id)
);

-- Sample data insertion for People
INSERT INTO People (name, age) VALUES
(N'Nguyễn Văn A', 30),
(N'Trần Thị B', 25),
(N'Lê Văn C', 40),
(N'Phạm Văn D', 22),
(N'Hoàng Thị E', 35),
(N'Đặng Văn F', 28),
(N'Vũ Thị G', 32),
(N'Bùi Văn H', 27),
(N'Đỗ Thị I', 45),
(N'Ngô Văn J', 38);

-- Sample data insertion for Accounts
INSERT INTO Accounts (id_people, display_name, userName, passWord) VALUES
(1, N'Nguyễn Văn A', 'nguyenvana', 'hashed_password_1'),
(2, N'Trần Thị B', 'tranthib', 'hashed_password_2'),
(3, N'Lê Văn C', 'levanc', 'hashed_password_3'),
(4, N'Phạm Văn D', 'phamvand', 'hashed_password_4'),
(5, N'Hoàng Thị E', 'hoangthie', 'hashed_password_5'),
(6, N'Đặng Văn F', 'dangvanf', 'hashed_password_6'),
(7, N'Vũ Thị G', 'vuthig', 'hashed_password_7'),
(8, N'Bùi Văn H', 'buivanh', 'hashed_password_8'),
(9, N'Đỗ Thị I', 'dothii', 'hashed_password_9'),
(10, N'Ngô Văn J', 'ngovanj', 'hashed_password_10');

-- Sample data insertion for Vehicle
INSERT INTO Vehicle (plate, color, vehicle_type, id_people) VALUES
('30A-12345', N'Đỏ', 'ô tô', 1),
('29B-67890', N'Xanh', 'ô tô', 2),
('31C-11122', N'Trắng', 'xe máy', 3),
('32D-33445', N'Đen', 'xe máy', 4),
('33E-55667', N'Bạc', 'ô tô', 5),
('34F-77889', N'Xám', 'xe máy', 6),
('35G-99000', N'Vàng', 'ô tô', 7),
('36H-11223', N'Cam', 'xe máy', 8),
('37I-44556', N'Xanh dương', 'ô tô', 9),
('38J-77889', N'Hồng', 'xe máy', 10);

-- Sample data insertion for Oto
INSERT INTO Oto (vehicle_id, seat) VALUES
(1, 5),
(2, 7),
(5, 4),
(7, 5),
(9, 7);

-- Sample data insertion for XeMay
INSERT INTO XeMay (vehicle_id, type) VALUES
(3, N'tay ga'),
(4, N'số'),
(6, N'điện'),
(8, N'số'),
(5, N'tay ga');

-- Sample data insertion for Street
INSERT INTO Street (name, tdtdxm, tdtdot) VALUES
(N'Trần Duy Hưng', 50, 60),
(N'Nguyễn Trãi', 40, 50),
(N'Láng Hạ', 45, 55),
(N'Phạm Hùng', 50, 70),
(N'Xuân Thủy', 35, 45),
(N'Kim Mã', 50, 60),
(N'Giải Phóng', 40, 50),
(N'Lê Văn Lương', 45, 55),
(N'Cầu Giấy', 50, 60),
(N'Hoàng Quốc Việt', 35, 45);

-- Sample data insertion for Violation
INSERT INTO Violation (id_street, plate_vehicle, name, date, time, mucPhat) VALUES
(1, '30A-12345', N'Vượt quá tốc độ', '2025-03-01', '2025-03-01 08:30:00', 500000),
(2, '29B-67890', N'Vượt quá tốc độ', '2025-03-02', '2025-03-02 09:15:00', 300000),
(3, '31C-11122', N'Vượt quá tốc độ', '2025-03-03', '2025-03-03 10:00:00', 200000),
(4, '32D-33445', N'Vượt quá tốc độ', '2025-03-04', '2025-03-04 14:45:00', 400000),
(5, '33E-55667', N'Vượt quá tốc độ', '2025-03-05', '2025-03-05 16:30:00', 600000),
(6, '34F-77889', N'Vượt quá tốc độ', '2025-03-06', '2025-03-06 18:00:00', 250000),
(7, '35G-99000', N'Vượt quá tốc độ', '2025-03-07', '2025-03-07 07:15:00', 550000),
(8, '36H-11223', N'Vượt quá tốc độ', '2025-03-08', '2025-03-08 12:20:00', 450000),
(9, '37I-44556', N'Vượt quá tốc độ', '2025-03-09', '2025-03-09 15:10:00', 300000),
(10, '38J-77889', N'Vượt quá tốc độ', '2025-03-10', '2025-03-10 20:05:00', 400000);