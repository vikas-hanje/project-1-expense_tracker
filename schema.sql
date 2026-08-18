CREATE DATABASE Expenses_DB;

USE Expenses_DB; 

CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Expenses (
    ExpenseID INT PRIMARY KEY AUTO_INCREMENT,
    Amount DECIMAL(10,2) NOT NULL,
    Description VARCHAR(255) NOT NULL,
    Expense_Date DATE NOT NULL DEFAULT (CURRENT_DATE), 
    CategoryID INT,
    CONSTRAINT fk_Categories
        FOREIGN KEY (CategoryID)
        REFERENCES Categories(CategoryID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);