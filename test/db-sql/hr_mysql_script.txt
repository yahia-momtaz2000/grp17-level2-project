
-- ********************************************************************
-- Create the REGIONS table to hold region information for locations
-- HR.LOCATIONS table has a foreign key to this table.

CREATE TABLE regions (
    region_id INT PRIMARY KEY,
    region_name VARCHAR(25)
);

-- ********************************************************************
-- Create the COUNTRIES table to hold country information for customers
-- and company locations.
-- OE.CUSTOMERS table and HR.LOCATIONS have a foreign key to this table.

CREATE TABLE countries (
    country_id CHAR(2) PRIMARY KEY,
    country_name VARCHAR(40),
    region_id INT,
    CONSTRAINT countr_reg_fk FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

-- ********************************************************************
-- Create the LOCATIONS table to hold address information for company departments.
-- HR.DEPARTMENTS has a foreign key to this table.

CREATE TABLE locations (
    location_id INT PRIMARY KEY,
    street_address VARCHAR(40),
    postal_code VARCHAR(12),
    city VARCHAR(30) NOT NULL,
    state_province VARCHAR(25),
    country_id CHAR(2),
    CONSTRAINT loc_c_id_fk FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- ********************************************************************
-- Create the DEPARTMENTS table to hold company department information.
-- HR.EMPLOYEES and HR.JOB_HISTORY have a foreign key to this table.

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(30) NOT NULL,
    manager_id INT,
    location_id INT,
    CONSTRAINT dept_loc_fk FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- ********************************************************************
-- Create the JOBS table to hold the different names of job roles within the company.
-- HR.EMPLOYEES has a foreign key to this table.

CREATE TABLE jobs (
    job_id VARCHAR(10) PRIMARY KEY,
    job_title VARCHAR(35) NOT NULL,
    min_salary DECIMAL(10,2),
    max_salary DECIMAL(10,2)
);

-- ********************************************************************
-- Create the EMPLOYEES table to hold the employee personnel
-- information for the company.
-- HR.EMPLOYEES has a self referencing foreign key to this table.

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(25) NOT NULL,
    email VARCHAR(25) NOT NULL,
    phone_number VARCHAR(20),
    hire_date DATE NOT NULL,
    job_id VARCHAR(10) NOT NULL,
    salary DECIMAL(10,2),
    commission_pct DECIMAL(4,2),
    manager_id INT,
    department_id INT,
    CONSTRAINT emp_dept_fk FOREIGN KEY (department_id) REFERENCES departments(department_id),
    CONSTRAINT emp_job_fk FOREIGN KEY (job_id) REFERENCES jobs(job_id),
    CONSTRAINT emp_manager_fk FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

-- ********************************************************************
-- Create the JOB_HISTORY table to hold the history of jobs that
-- employees have held in the past.
-- HR.JOBS, HR_DEPARTMENTS, and HR.EMPLOYEES have a foreign key to this table.

CREATE TABLE job_history (
    employee_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    job_id VARCHAR(10) NOT NULL,
    department_id INT,
    CONSTRAINT jhist_date_interval CHECK (end_date > start_date),
    PRIMARY KEY (employee_id, start_date),
    CONSTRAINT jhist_job_fk FOREIGN KEY (job_id) REFERENCES jobs(job_id),
    CONSTRAINT jhist_emp_fk FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);




































-- Prompt ******  Creating EMP_DETAILS_VIEW view ...

CREATE OR REPLACE VIEW emp_details_view AS
SELECT
  e.employee_id,
  e.job_id,
  e.manager_id,
  e.department_id,
  d.location_id,
  l.country_id,
  e.first_name,
  e.last_name,
  e.salary,
  e.commission_pct,
  d.department_name,
  j.job_title,
  l.city,
  l.state_province,
  c.country_name,
  r.region_name
FROM
  employees e
  JOIN departments d ON e.department_id = d.department_id
  JOIN jobs j ON j.job_id = e.job_id
  JOIN locations l ON d.location_id = l.location_id
  JOIN countries c ON l.country_id = c.country_id
  JOIN regions r ON c.region_id = r.region_id;























-- Populating REGIONS table
INSERT INTO regions (region_id, region_name) VALUES 
    (1, 'Europe'),
    (2, 'Americas'),
    (3, 'Asia'),
    (4, 'Middle East and Africa');

-- Populating COUNTRIES table
INSERT INTO countries (country_id, country_name, region_id) VALUES 
    ('IT', 'Italy', 1),
    ('JP', 'Japan', 3),
    ('US', 'United States of America', 2),
    ('CA', 'Canada', 2),
    ('CN', 'China', 3),
    ('IN', 'India', 3),
    ('AU', 'Australia', 3),
    ('ZW', 'Zimbabwe', 4),
    ('SG', 'Singapore', 3),
    ('UK', 'United Kingdom', 1),
    ('FR', 'France', 1),
    ('DE', 'Germany', 1),
    ('ZM', 'Zambia', 4),
    ('EG', 'Egypt', 4),
    ('BR', 'Brazil', 2),
    ('CH', 'Switzerland', 1),
    ('NL', 'Netherlands', 1),
    ('MX', 'Mexico', 2),
    ('KW', 'Kuwait', 4),
    ('DK', 'Denmark', 1),
    ('HK', 'HongKong', 3),
    ('NG', 'Nigeria', 4),
    ('AR', 'Argentina', 2),
    ('BE', 'Belgium', 1);

-- Populating LOCATIONS table
INSERT INTO locations (location_id, street_address, postal_code, city, state_province, country_id) VALUES 
    (1000, '1297 Via Cola di Rie', '00989', 'Roma', NULL, 'IT'),
    (1100, '93091 Calle della Testa', '10934', 'Venice', NULL, 'IT'),
    (1200, '2017 Shinjuku-ku', '1689', 'Tokyo', 'Tokyo Prefecture', 'JP'),
    (1300, '9450 Kamiya-cho', '6823', 'Hiroshima', NULL, 'JP'),
    (1400, '2014 Jabberwocky Rd', '26192', 'Southlake', 'Texas', 'US'),
    (1500, '2011 Interiors Blvd', '99236', 'South San Francisco', 'California', 'US'),
    (1600, '2007 Zagora St', '50090', 'South Brunswick', 'New Jersey', 'US'),
    (1700, '2004 Charade Rd', '98199', 'Seattle', 'Washington', 'US'),
    (1800, '147 Spadina Ave', 'M5V 2L7', 'Toronto', 'Ontario', 'CA'),
    (1900, '6092 Boxwood St', 'YSW 9T2', 'Whitehorse', 'Yukon', 'CA'),
    (2000, '40-5-12 Laogianggen', '190518', 'Beijing', NULL, 'CN'),
    (2100, '1298 Vileparle (E)', '490231', 'Bombay', 'Maharashtra', 'IN'),
    (2200, '12-98 Victoria Street', '2901', 'Sydney', 'New South Wales', 'AU'),
    (2300, '198 Clementi North', '540198', 'Singapore', NULL, 'SG'),
    (2400, '8204 Arthur St', NULL, 'London', NULL, 'UK'),
    (2500, 'Magdalen Centre, The Oxford Science Park', 'OX9 9ZB', 'Oxford', 'Oxford', 'UK'),
    (2600, '9702 Chester Road', '09629850293', 'Stretford', 'Manchester', 'UK'),
    (2700, 'Schwanthalerstr. 7031', '80925', 'Munich', 'Bavaria', 'DE'),
    (2800, 'Rua Frei Caneca 1360', '01307-002', 'Sao Paulo', 'Sao Paulo', 'BR'),
    (2900, '20 Rue des Corps-Saints', '1730', 'Geneva', 'Geneve', 'CH'),
    (3000, 'Murtenstrasse 921', '3095', 'Bern', 'BE', 'CH'),
    (3100, 'Pieter Breughelstraat 837', '3029SK', 'Utrecht', 'Utrecht', 'NL'),
    (3200, 'Mariano Escobedo 9991', '11932', 'Mexico City', 'Distrito Federal', 'MX');

-- Populating DEPARTMENTS table


INSERT INTO departments (department_id, department_name, manager_id, location_id) VALUES 
    (10, 'Administration', 200, 1700),
    (20, 'Marketing', 201, 1800),
    (30, 'Purchasing', 114, 1700),
    (40, 'Human Resources', 203, 2400),
    (50, 'Shipping', 121, 1500),
    (60, 'IT', 103, 1400),
    (70, 'Public Relations', 204, 2700),
    (80, 'Sales', 145, 2500),
    (90, 'Executive', 100, 1700),
    (100, 'Finance', 108, 1700),
    (110, 'Accounting', 205, 1700),
    (120, 'Treasury', NULL, 1700),
    (130, 'Corporate Tax', NULL, 1700),
    (140, 'Control And Credit', NULL, 1700),
    (150, 'Shareholder Services', NULL, 1700),
    (160, 'Benefits', NULL, 1700),
    (170, 'Manufacturing', NULL, 1700),
    (180, 'Construction', NULL, 1700),
    (190, 'Contracting', NULL, 1700),
    (200, 'Operations', NULL, 1700),
    (210, 'IT Support', NULL, 1700),
    (220, 'NOC', NULL, 1700),
    (230, 'IT Helpdesk', NULL, 1700),
    (240, 'Government Sales', NULL, 1700),
    (250, 'Retail Sales', NULL, 1700),
    (260, 'Recruiting', NULL, 1700),
    (270, 'Payroll', NULL, 1700);











INSERT INTO jobs VALUES 
        ( 'AD_PRES'
        , 'President'
        , 20000
        , 40000
        );
INSERT INTO jobs VALUES 
        ( 'AD_VP'
        , 'Administration Vice President'
        , 15000
        , 30000
        );

INSERT INTO jobs VALUES 
        ( 'AD_ASST'
        , 'Administration Assistant'
        , 3000
        , 6000
        );

INSERT INTO jobs VALUES 
        ( 'FI_MGR'
        , 'Finance Manager'
        , 8200
        , 16000
        );

INSERT INTO jobs VALUES 
        ( 'FI_ACCOUNT'
        , 'Accountant'
        , 4200
        , 9000
        );

INSERT INTO jobs VALUES 
        ( 'AC_MGR'
        , 'Accounting Manager'
        , 8200
        , 16000
        );

INSERT INTO jobs VALUES 
        ( 'AC_ACCOUNT'
        , 'Public Accountant'
        , 4200
        , 9000
        );
INSERT INTO jobs VALUES 
        ( 'SA_MAN'
        , 'Sales Manager'
        , 10000
        , 20000
        );

INSERT INTO jobs VALUES 
        ( 'SA_REP'
        , 'Sales Representative'
        , 6000
        , 12000
        );

INSERT INTO jobs VALUES 
        ( 'PU_MAN'
        , 'Purchasing Manager'
        , 8000
        , 15000
        );

INSERT INTO jobs VALUES 
        ( 'PU_CLERK'
        , 'Purchasing Clerk'
        , 2500
        , 5500
        );

INSERT INTO jobs VALUES 
        ( 'ST_MAN'
        , 'Stock Manager'
        , 5500
        , 8500
        );
INSERT INTO jobs VALUES 
        ( 'ST_CLERK'
        , 'Stock Clerk'
        , 2000
        , 5000
        );

INSERT INTO jobs VALUES 
        ( 'SH_CLERK'
        , 'Shipping Clerk'
        , 2500
        , 5500
        );

INSERT INTO jobs VALUES 
        ( 'IT_PROG'
        , 'Programmer'
        , 4000
        , 10000
        );

INSERT INTO jobs VALUES 
        ( 'MK_MAN'
        , 'Marketing Manager'
        , 9000
        , 15000
        );

INSERT INTO jobs VALUES 
        ( 'MK_REP'
        , 'Marketing Representative'
        , 4000
        , 9000
        );

INSERT INTO jobs VALUES 
        ( 'HR_REP'
        , 'Human Resources Representative'
        , 4000
        , 9000
        );

INSERT INTO jobs VALUES 
        ( 'PR_REP'
        , 'Public Relations Representative'
        , 4500
        , 10500
        );

-- Prompt ******  Populating EMPLOYEES table ....

INSERT INTO employees VALUES 
        ( 100
        , 'Steven'
        , 'King'
        , 'SKING'
        , '515.123.4567'
        , STR_TO_DATE('17-JUN-1987', '%d-%b-%Y')
        , 'AD_PRES'
        , 24000
        , NULL
        , NULL
        , 90
        );



INSERT INTO employees VALUES 
        ( 101
        , 'Neena'
        , 'Kochhar'
        , 'NKOCHHAR'
        , '515.123.4568'
        , STR_TO_DATE('21-SEP-1989', '%d-%b-%Y')
        , 'AD_VP'
        , 17000
        , NULL
        , 100
        , 90
        );

INSERT INTO employees VALUES 
        ( 102
        , 'Lex'
        , 'De Haan'
        , 'LDEHAAN'
        , '515.123.4569'
        , STR_TO_DATE('13-JAN-1993', '%d-%b-%Y')
        , 'AD_VP'
        , 17000
        , NULL
        , 100
        , 90
        );

INSERT INTO employees VALUES 
        ( 103
        , 'Alexander'
        , 'Hunold'
        , 'AHUNOLD'
        , '590.423.4567'
        , STR_TO_DATE('03-JAN-1990', '%d-%b-%Y')
        , 'IT_PROG'
        , 9000
        , NULL
        , 102
        , 60
        );

INSERT INTO employees VALUES 
        ( 104
        , 'Bruce'
        , 'Ernst'
        , 'BERNST'
        , '590.423.4568'
        , STR_TO_DATE('21-MAY-1991', '%d-%b-%Y')
        , 'IT_PROG'
        , 6000
        , NULL
        , 103
        , 60
        );

INSERT INTO employees VALUES 
        ( 105
        , 'David'
        , 'Austin'
        , 'DAUSTIN'
        , '590.423.4569'
        , STR_TO_DATE('25-JUN-1997', '%d-%b-%Y')
        , 'IT_PROG'
        , 4800
        , NULL
        , 103
        , 60
        );

INSERT INTO employees VALUES 
        ( 106
        , 'Valli'
        , 'Pataballa'
        , 'VPATABAL'
        , '590.423.4560'
        , STR_TO_DATE('05-FEB-1998', '%d-%b-%Y')
        , 'IT_PROG'
        , 4800
        , NULL
        , 103
        , 60
        );

INSERT INTO employees VALUES 
        ( 107
        , 'Diana'
        , 'Lorentz'
        , 'DLORENTZ'
        , '590.423.5567'
        , STR_TO_DATE('07-FEB-1999', '%d-%b-%Y')
        , 'IT_PROG'
        , 4200
        , NULL
        , 103
        , 60
        );

INSERT INTO employees VALUES 
        ( 108
        , 'Nancy'
        , 'Greenberg'
        , 'NGREENBE'
        , '515.124.4569'
        , STR_TO_DATE('17-AUG-1994', '%d-%b-%Y')
        , 'FI_MGR'
        , 12000
        , NULL
        , 101
        , 100
        );

INSERT INTO employees VALUES 
        ( 109
        , 'Daniel'
        , 'Faviet'
        , 'DFAVIET'
        , '515.124.4169'
        , STR_TO_DATE('16-AUG-1994', '%d-%b-%Y')
        , 'FI_ACCOUNT'
        , 9000
        , NULL
        , 108
        , 100
        );

INSERT INTO employees VALUES 
        ( 110
        , 'John'
        , 'Chen'
        , 'JCHEN'
        , '515.124.4269'
        , STR_TO_DATE('28-SEP-1997', '%d-%b-%Y')
        , 'FI_ACCOUNT'
        , 8200
        , NULL
        , 108
        , 100
        );

INSERT INTO employees VALUES 
        ( 111
        , 'Ismael'
        , 'Sciarra'
        , 'ISCIARRA'
        , '515.124.4369'
        , STR_TO_DATE('30-SEP-1997', '%d-%b-%Y')
        , 'FI_ACCOUNT'
        , 7700
        , NULL
        , 108
        , 100
        );

INSERT INTO employees VALUES 
        ( 112
        , 'Jose Manuel'
        , 'Urman'
        , 'JMURMAN'
        , '515.124.4469'
        , STR_TO_DATE('07-MAR-1998', '%d-%b-%Y')
        , 'FI_ACCOUNT'
        , 7800
        , NULL
        , 108
        , 100
        );

INSERT INTO employees VALUES 
        ( 113
        , 'Luis'
        , 'Popp'
        , 'LPOPP'
        , '515.124.4567'
        , STR_TO_DATE('07-DEC-1999', '%d-%b-%Y')
        , 'FI_ACCOUNT'
        , 6900
        , NULL
        , 108
        , 100
        );

INSERT INTO employees VALUES 
        ( 114
        , 'Den'
        , 'Raphaely'
        , 'DRAPHEAL'
        , '515.127.4561'
        , STR_TO_DATE('07-DEC-1994', '%d-%b-%Y')
        , 'PU_MAN'
        , 11000
        , NULL
        , 100
        , 30
        );

INSERT INTO employees VALUES 
        ( 115
        , 'Alexander'
        , 'Khoo'
        , 'AKHOO'
        , '515.127.4562'
        , STR_TO_DATE('18-MAY-1995', '%d-%b-%Y')
        , 'PU_CLERK'
        , 3100
        , NULL
        , 114
        , 30
        );

INSERT INTO employees VALUES 
        ( 116
        , 'Shelli'
        , 'Baida'
        , 'SBAIDA'
        , '515.127.4563'
        , STR_TO_DATE('24-DEC-1997', '%d-%b-%Y')
        , 'PU_CLERK'
        , 2900
        , NULL
        , 114
        , 30
        );

INSERT INTO employees VALUES 
        ( 117
        , 'Sigal'
        , 'Tobias'
        , 'STOBIAS'
        , '515.127.4564'
        , STR_TO_DATE('24-JUL-1997', '%d-%b-%Y')
        , 'PU_CLERK'
        , 2800
        , NULL
        , 114
        , 30
        );

INSERT INTO employees VALUES 
        ( 118
        , 'Guy'
        , 'Himuro'
        , 'GHIMURO'
        , '515.127.4565'
        , STR_TO_DATE('15-NOV-1998', '%d-%b-%Y')
        , 'PU_CLERK'
        , 2600
        , NULL
        , 114
        , 30
        );

INSERT INTO employees VALUES 
        ( 119
        , 'Karen'
        , 'Colmenares'
        , 'KCOLMENA'
        , '515.127.4566'
        , STR_TO_DATE('10-AUG-1999', '%d-%b-%Y')
        , 'PU_CLERK'
        , 2500
        , NULL
        , 114
        , 30
        );

INSERT INTO employees VALUES 
        ( 120
        , 'Matthew'
        , 'Weiss'
        , 'MWEISS'
        , '650.123.1234'
        , STR_TO_DATE('18-JUL-1996', '%d-%b-%Y')
        , 'ST_MAN'
        , 8000
        , NULL
        , 100
        , 50
        );

INSERT INTO employees VALUES 
        ( 121
        , 'Adam'
        , 'Fripp'
        , 'AFRIPP'
        , '650.123.2234'
        , STR_TO_DATE('10-APR-1997', '%d-%b-%Y')
        , 'ST_MAN'
        , 8200
        , NULL
        , 100
        , 50
        );

INSERT INTO employees VALUES 
        ( 122
        , 'Payam'
        , 'Kaufling'
        , 'PKAUFLIN'
        , '650.123.3234'
        , STR_TO_DATE('01-MAY-1995', '%d-%b-%Y')
        , 'ST_MAN'
        , 7900
        , NULL
        , 100
        , 50
        );

INSERT INTO employees VALUES 
        ( 123
        , 'Shanta'
        , 'Vollman'
        , 'SVOLLMAN'
        , '650.123.4234'
        , STR_TO_DATE('10-OCT-1997', '%d-%b-%Y')
        , 'ST_MAN'
        , 6500
        , NULL
        , 100
        , 50
        );

INSERT INTO employees VALUES 
        ( 124
        , 'Kevin'
        , 'Mourgos'
        , 'KMOURGOS'
        , '650.123.5234'
        , STR_TO_DATE('16-NOV-1999', '%d-%b-%Y')
        , 'ST_MAN'
        , 5800
        , NULL
        , 100
        , 50
        );

INSERT INTO employees VALUES 
        ( 125
        , 'Julia'
        , 'Nayer'
        , 'JNAYER'
        , '650.124.1214'
        , STR_TO_DATE('16-JUL-1997', '%d-%b-%Y')
        , 'ST_CLERK'
        , 3200
        , NULL
        , 120
        , 50
        );

INSERT INTO employees VALUES 
        ( 126
        , 'Irene'
        , 'Mikkilineni'
        , 'IMIKKILI'
        , '650.124.1224'
        , STR_TO_DATE('28-SEP-1998', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2700
        , NULL
        , 120
        , 50
        );

INSERT INTO employees VALUES 
        ( 127
        , 'James'
        , 'Landry'
        , 'JLANDRY'
        , '650.124.1334'
        , STR_TO_DATE('14-JAN-1999', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2400
        , NULL
        , 120
        , 50
        );

INSERT INTO employees VALUES 
        ( 128
        , 'Steven'
        , 'Markle'
        , 'SMARKLE'
        , '650.124.1434'
        , STR_TO_DATE('08-MAR-2000', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2200
        , NULL
        , 120
        , 50
        );

INSERT INTO employees VALUES 
        ( 129
        , 'Laura'
        , 'Bissot'
        , 'LBISSOT'
        , '650.124.5234'
        , STR_TO_DATE('20-AUG-1997', '%d-%b-%Y')
        , 'ST_CLERK'
        , 3300
        , NULL
        , 121
        , 50
        );

INSERT INTO employees VALUES 
        ( 130
        , 'Mozhe'
        , 'Atkinson'
        , 'MATKINSO'
        , '650.124.6234'
        , STR_TO_DATE('30-OCT-1997', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2800
        , NULL
        , 121
        , 50
        );

INSERT INTO employees VALUES 
        ( 131
        , 'James'
        , 'Marlow'
        , 'JAMRLOW'
        , '650.124.7234'
        , STR_TO_DATE('16-FEB-1999', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2500
        , NULL
        , 121
        , 50
        );

INSERT INTO employees VALUES 
        ( 132
        , 'TJ'
        , 'Olson'
        , 'TJOLSON'
        , '650.124.8234'
        , STR_TO_DATE('10-APR-1999', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2100
        , NULL
        , 121
        , 50
        );

INSERT INTO employees VALUES 
        ( 133
        , 'Jason'
        , 'Mallin'
        , 'JMALLIN'
        , '650.127.1934'
        , STR_TO_DATE('14-JUN-1996', '%d-%b-%Y')
        , 'ST_CLERK'
        , 3300
        , NULL
        , 122
        , 50
        );

INSERT INTO employees VALUES 
        ( 134
        , 'Michael'
        , 'Rogers'
        , 'MROGERS'
        , '650.127.1834'
        , STR_TO_DATE('26-AUG-1998', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2900
        , NULL
        , 122
        , 50
        );

INSERT INTO employees VALUES 
        ( 135
        , 'Ki'
        , 'Gee'
        , 'KGEE'
        , '650.127.1734'
        , STR_TO_DATE('12-DEC-1999', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2400
        , NULL
        , 122
        , 50
        );

INSERT INTO employees VALUES 
        ( 136
        , 'Hazel'
        , 'Philtanker'
        , 'HPHILTA'
        , '650.127.1634'
        , STR_TO_DATE('06-FEB-2000', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2200
        , NULL
        , 122
        , 50
        );

INSERT INTO employees VALUES 
        ( 137
        , 'Renske'
        , 'Ladwig'
        , 'RLADWIG'
        , '650.121.1234'
        , STR_TO_DATE('14-JUL-1997', '%d-%b-%Y')
        , 'ST_CLERK'
        , 3600
        , NULL
        , 123
        , 50
        );

INSERT INTO employees VALUES 
        ( 138
        , 'Stephen'
        , 'Stiles'
        , 'SSTILES'
        , '650.121.2034'
        , STR_TO_DATE('26-OCT-1997', '%d-%b-%Y')
        , 'ST_CLERK'
        , 3200
        , NULL
        , 123
        , 50
        );

INSERT INTO employees VALUES 
        ( 139
        , 'John'
        , 'Seo'
        , 'JSEO'
        , '650.121.2019'
        , STR_TO_DATE('12-FEB-1998', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2700
        , NULL
        , 123
        , 50
        );

INSERT INTO employees VALUES 
        ( 140
        , 'Joshua'
        , 'Patel'
        , 'JPATEL'
        , '650.121.1834'
        , STR_TO_DATE('06-APR-1996', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2500
        , NULL
        , 123
        , 50
        );

INSERT INTO employees VALUES 
        ( 141
        , 'Trenna'
        , 'Rajs'
        , 'TRAJS'
        , '650.121.8009'
        , STR_TO_DATE('17-OCT-1995', '%d-%b-%Y')
        , 'ST_CLERK'
        , 3500
        , NULL
        , 124
        , 50
        );

INSERT INTO employees VALUES 
        ( 142
        , 'Curtis'
        , 'Davies'
        , 'CDAVIES'
        , '650.121.2994'
        , STR_TO_DATE('29-JAN-1997', '%d-%b-%Y')
        , 'ST_CLERK'
        , 3100
        , NULL
        , 124
        , 50
        );

INSERT INTO employees VALUES 
        ( 143
        , 'Randall'
        , 'Matos'
        , 'RMATOS'
        , '650.121.2874'
        , STR_TO_DATE('15-MAR-1998', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2600
        , NULL
        , 124
        , 50
        );

INSERT INTO employees VALUES 
        ( 144
        , 'Peter'
        , 'Vargas'
        , 'PVARGAS'
        , '650.121.2004'
        , STR_TO_DATE('09-JUL-1998', '%d-%b-%Y')
        , 'ST_CLERK'
        , 2500
        , NULL
        , 124
        , 50
        );

INSERT INTO employees VALUES 
        ( 145
        , 'John'
        , 'Russell'
        , 'JRUSSEL'
        , '011.44.1344.429268'
        , STR_TO_DATE('01-OCT-1996', '%d-%b-%Y')
        , 'SA_MAN'
        , 14000
        , 0.4
        , 100
        , 80
        );

INSERT INTO employees VALUES 
        ( 146
        , 'Karen'
        , 'Partners'
        , 'KPARTNER'
        , '011.44.1344.467268'
        , STR_TO_DATE('05-JAN-1997', '%d-%b-%Y')
        , 'SA_MAN'
        , 13500
        , 0.3
        , 100
        , 80
        );

INSERT INTO employees VALUES 
        ( 147
        , 'Alberto'
        , 'Errazuriz'
        , 'AERRAZUR'
        , '011.44.1344.429278'
        , STR_TO_DATE('10-MAR-1997', '%d-%b-%Y')
        , 'SA_MAN'
        , 12000
        , 0.3
        , 100
        , 80
        );

INSERT INTO employees VALUES 
        ( 148
        , 'Gerald'
        , 'Cambrault'
        , 'GCAMBRAU'
        , '011.44.1344.619268'
        , STR_TO_DATE('15-OCT-1997', '%d-%b-%Y')
        , 'SA_MAN'
        , 11000
        , 0.3
        , 100
        , 80
        );

INSERT INTO employees VALUES 
        ( 149
        , 'Eleni'
        , 'Zlotkey'
        , 'EZLOTKEY'
        , '011.44.1344.429018'
        , STR_TO_DATE('29-JAN-1998', '%d-%b-%Y')
        , 'SA_MAN'
        , 10500
        , 0.2
        , 100
        , 80
        );

INSERT INTO employees VALUES 
        ( 150
        , 'Peter'
        , 'Tucker'
        , 'PTUCKER'
        , '011.44.1344.129268'
        , STR_TO_DATE('30-JAN-1997', '%d-%b-%Y')
        , 'SA_REP'
        , 10000
        , 0.3
        , 145
        , 80
        );

INSERT INTO employees VALUES 
        ( 151
        , 'David'
        , 'Bernstein'
        , 'DBERNSTE'
        , '011.44.1344.345268'
        , STR_TO_DATE('24-MAR-1997', '%d-%b-%Y')
        , 'SA_REP'
        , 9500
        , 0.25
        , 145
        , 80
        );

INSERT INTO employees VALUES 
        ( 152
        , 'Peter'
        , 'Hall'
        , 'PHALL'
        , '011.44.1344.478968'
        , STR_TO_DATE('20-AUG-1998', '%d-%b-%Y')
        , 'SA_REP'
        , 9000
        , 0.25
        , 145
        , 80
        );

INSERT INTO employees VALUES 
        ( 153
        , 'Christopher'
        , 'Olsen'
        , 'COLSEN'
        , '011.44.1344.498718'
        , STR_TO_DATE('30-MAR-1999', '%d-%b-%Y')
        , 'SA_REP'
        , 8000
        , 0.2
        , 145
        , 80
        );

INSERT INTO employees VALUES 
        ( 154
        , 'Nanette'
        , 'Cambrault'
        , 'NCAMBRAU'
        , '011.44.1344.987668'
        , STR_TO_DATE('09-DEC-1998', '%d-%b-%Y')
        , 'SA_REP'
        , 7500
        , 0.2
        , 145
        , 80
        );

INSERT INTO employees VALUES 
        ( 155
        , 'Oliver'
        , 'Tuvault'
        , 'OTUVAULT'
        , '011.44.1344.486508'
        , STR_TO_DATE('23-NOV-1997', '%d-%b-%Y')
        , 'SA_REP'
        , 7000
        , 0.15
        , 145
        , 80
        );

INSERT INTO employees VALUES 
        ( 156
        , 'Janette'
        , 'King'
        , 'JKING'
        , '011.44.1345.429268'
        , STR_TO_DATE('30-JAN-1998', '%d-%b-%Y')
        , 'SA_REP'
        , 10000
        , 0.35
        , 146
        , 80
        );

INSERT INTO employees VALUES 
        ( 157
        , 'Patrick'
        , 'Sully'
        , 'PSULLY'
        , '011.44.1345.929268'
        , STR_TO_DATE('04-MAR-1996', '%d-%b-%Y')
        , 'SA_REP'
        , 9500
        , 0.35
        , 146
        , 80
        );

INSERT INTO employees VALUES 
        ( 158
        , 'Allan'
        , 'McEwen'
        , 'AMCEWEN'
        , '011.44.1345.829268'
        , STR_TO_DATE('01-AUG-1996', '%d-%b-%Y')
        , 'SA_REP'
        , 9000
        , 0.35
        , 146
        , 80
        );

INSERT INTO employees VALUES 
        ( 159
        , 'Lindsey'
        , 'Smith'
        , 'LSMITH'
        , '011.44.1345.729268'
        , STR_TO_DATE('10-MAR-1997', '%d-%b-%Y')
        , 'SA_REP'
        , 8000
        , 0.3
        , 146
        , 80
        );

INSERT INTO employees VALUES 
        ( 160
        , 'Louise'
        , 'Doran'
        , 'LDORAN'
        , '011.44.1345.629268'
        , STR_TO_DATE('15-DEC-1999', '%d-%b-%Y')
        , 'SA_REP'
        , 7500
        , 0.3
        , 146
        , 80
        );

INSERT INTO employees VALUES 
        ( 161
        , 'Sarath'
        , 'Sewall'
        , 'SSEWALL'
        , '011.44.1345.929072'
        , STR_TO_DATE('03-AUG-1998', '%d-%b-%Y')
        , 'SA_REP'
        , 7000
        , 0.25
        , 146
        , 80
        );

INSERT INTO employees VALUES 
        ( 162
        , 'Clara'
        , 'Vishney'
        , 'CVISHNEY'
        , '011.44.1346.129268'
        , STR_TO_DATE('11-NOV-1997', '%d-%b-%Y')
        , 'SA_REP'
        , 10500
        , 0.25
        , 147
        , 80
        );

INSERT INTO employees VALUES 
        ( 163
        , 'Danielle'
        , 'Greene'
        , 'DGREENE'
        , '011.44.1346.229268'
        , STR_TO_DATE('19-MAR-1999', '%d-%b-%Y')
        , 'SA_REP'
        , 9500
        , 0.15
        , 147
        , 80
        );

INSERT INTO employees VALUES 
        ( 164
        , 'Mattea'
        , 'Marvins'
        , 'MMARVINS'
        , '011.44.1346.329268'
        , STR_TO_DATE('24-SEP-1998', '%d-%b-%Y')
        , 'SA_REP'
        , 7200
        , 0.1
        , 147
        , 80
        );

INSERT INTO employees VALUES 
        ( 165
        , 'David'
        , 'Lee'
        , 'DLEE'
        , '011.44.1346.529268'
        , STR_TO_DATE('23-FEB-1997', '%d-%b-%Y')
        , 'SA_REP'
        , 6800
        , 0.1
        , 147
        , 80
        );

INSERT INTO employees VALUES 
        ( 166
        , 'Sundar'
        , 'Ande'
        , 'SANDE'
        , '011.44.1346.629268'
        , STR_TO_DATE('24-MAR-2000', '%d-%b-%Y')
        , 'SA_REP'
        , 6400
        , 0.1
        , 147
        , 80
        );

INSERT INTO employees VALUES 
        ( 167
        , 'Amit'
        , 'Banda'
        , 'ABANDA'
        , '011.44.1346.729268'
        , STR_TO_DATE('21-APR-1996', '%d-%b-%Y')
        , 'SA_REP'
        , 6200
        , 0.1
        , 147
        , 80
        );

INSERT INTO employees VALUES 
        ( 168
        , 'Lisa'
        , 'Ozer'
        , 'LOZER'
        , '011.44.1343.929268'
        , STR_TO_DATE('11-MAR-1997', '%d-%b-%Y')
        , 'SA_REP'
        , 11500
        , 0.25
        , 148
        , 80
        );

INSERT INTO employees VALUES 
        ( 169
        , 'Harrison'
        , 'Bloom'
        , 'HBLOOM'
        , '011.44.1343.829268'
        , STR_TO_DATE('23-MAR-1999', '%d-%b-%Y')
        , 'SA_REP'
        , 10000
        , 0.2
        , 148
        , 80
        );

INSERT INTO employees VALUES 
        ( 170
        , 'Tayler'
        , 'Fox'
        , 'TFOX'
        , '011.44.1343.729268'
        , STR_TO_DATE('24-JAN-1998', '%d-%b-%Y')
        , 'SA_REP'
        , 9600
        , 0.2
        , 148
        , 80
        );

INSERT INTO employees VALUES 
        ( 171
        , 'William'
        , 'Smith'
        , 'WSMITH'
        , '011.44.1343.629268'
        , STR_TO_DATE('23-FEB-1996', '%d-%b-%Y')
        , 'SA_REP'
        , 7400
        , 0.15
        , 148
        , 80
        );

INSERT INTO employees VALUES 
        ( 172
        , 'Elizabeth'
        , 'Bates'
        , 'EBATES'
        , '011.44.1343.529268'
        , STR_TO_DATE('24-MAR-1999', '%d-%b-%Y')
        , 'SA_REP'
        , 7300
        , 0.15
        , 148
        , 80
        );

INSERT INTO employees VALUES 
        ( 173
        , 'Sundita'
        , 'Kumar'
        , 'SKUMAR'
        , '011.44.1343.329268'
        , STR_TO_DATE('21-APR-1998', '%d-%b-%Y')
        , 'SA_REP'
        , 6100
        , 0.1
        , 148
        , 80
        );

INSERT INTO employees VALUES 
        ( 174
        , 'Ellen'
        , 'Abel'
        , 'EABEL'
        , '011.44.1644.429267'
        , STR_TO_DATE('11-MAY-1996', '%d-%b-%Y')
        , 'SA_REP'
        , 11000
        , 0.3
        , 149
        , NULL
        );

INSERT INTO employees VALUES 
        ( 175
        , 'Alyssa'
        , 'Hutton'
        , 'AHUTTON'
        , '011.44.1644.429266'
        , STR_TO_DATE('19-MAR-1997', '%d-%b-%Y')
        , 'SA_REP'
        , 8800
        , 0.25
        , 149
        , 80
        );

INSERT INTO employees VALUES 
        ( 176
        , 'Jonathon'
        , 'Taylor'
        , 'JTAYLOR'
        , '011.44.1644.429265'
        , STR_TO_DATE('24-MAR-1998', '%d-%b-%Y')
        , 'SA_REP'
        , 8600
        , 0.2
        , 149
        , 80
        );

INSERT INTO employees VALUES 
        ( 177
        , 'Jack'
        , 'Livingston'
        , 'JLIVINGS'
        , '011.44.1644.429264'
        , STR_TO_DATE('23-APR-1999', '%d-%b-%Y')
        , 'SA_REP'
        , 8400
        , 0.2
        , 149
        , 80
        );

INSERT INTO employees VALUES 
        ( 178
        , 'Kimberely'
        , 'Grant'
        , 'KGRANT'
        , '011.44.1644.429263'
        , STR_TO_DATE('24-MAY-1999', '%d-%b-%Y')
        , 'SA_REP'
        , 7000
        , 0.15
        , 149
        , 80
        );

INSERT INTO employees VALUES 
        ( 179
        , 'Charles'
        , 'Johnson'
        , 'CJOHNSON'
        , '011.44.1644.429262'
        , STR_TO_DATE('04-JAN-2000', '%d-%b-%Y')
        , 'SA_REP'
        , 6200
        , 0.1
        , 149
        , 80
        );

INSERT INTO employees VALUES 
        ( 180
        , 'Winston'
        , 'Taylor'
        , 'WTAYLOR'
        , '650.507.9876'
        , STR_TO_DATE('24-JAN-1998', '%d-%b-%Y')
        , 'SH_CLERK'
        , 3200
        , NULL
        , 120
        , 50
        );

INSERT INTO employees VALUES 
        ( 181
        , 'Jean'
        , 'Fleaur'
        , 'JFLEAUR'
        , '650.507.9877'
        , STR_TO_DATE('23-FEB-1998', '%d-%b-%Y')
        , 'SH_CLERK'
        , 3100
        , NULL
        , 120
        , 50
        );

INSERT INTO employees VALUES 
        ( 182
        , 'Martha'
        , 'Sullivan'
        , 'MSULLIVA'
        , '650.507.9878'
        , STR_TO_DATE('21-JUN-1999', '%d-%b-%Y')
        , 'SH_CLERK'
        , 2500
        , NULL
        , 120
        , 50
        );

INSERT INTO employees VALUES 
        ( 183
        , 'Girard'
        , 'Geoni'
        , 'GGEONI'
        , '650.507.9879'
        , STR_TO_DATE('03-FEB-1998', '%d-%b-%Y')
        , 'SH_CLERK'
        , 2800
        , NULL
        , 120
        , 50
        );

INSERT INTO employees VALUES 
        ( 184
        , 'Nandita'
        , 'Sarchand'
        , 'NSARCHAN'
        , '650.509.1876'
        , STR_TO_DATE('27-JAN-1998', '%d-%b-%Y')
        , 'SH_CLERK'
        , 4200
        , NULL
        , 121
        , 50
        );

INSERT INTO employees VALUES 
        ( 185
        , 'Alexis'
        , 'Bull'
        , 'ABULL'
        , '650.509.2876'
        , STR_TO_DATE('20-FEB-1998', '%d-%b-%Y')
        , 'SH_CLERK'
        , 4100
        , NULL
        , 121
        , 50
        );

INSERT INTO employees VALUES 
        ( 186
        , 'Julia'
        , 'Dellinger'
        , 'JDELLING'
        , '650.509.3876'
        , STR_TO_DATE('24-JUN-1999', '%d-%b-%Y')
        , 'SH_CLERK'
        , 3400
        , NULL
        , 121
        , 50
        );

INSERT INTO employees VALUES 
        ( 187
        , 'Anthony'
        , 'Cabrio'
        , 'ACABRIO'
        , '650.509.4876'
        , STR_TO_DATE('07-FEB-1997', '%d-%b-%Y')
        , 'SH_CLERK'
        , 3000
        , NULL
        , 121
        , 50
        );

INSERT INTO employees VALUES 
        ( 188
        , 'Kelly'
        , 'Chung'
        , 'KCHUNG'
        , '650.505.1876'
        , STR_TO_DATE('14-JUN-1999', '%d-%b-%Y')
        , 'SH_CLERK'
        , 3800
        , NULL
        , 122
        , 50
        );

INSERT INTO employees VALUES 
        ( 189
        , 'Jennifer'
        , 'Dilly'
        , 'JDILLY'
        , '650.505.2876'
        , STR_TO_DATE('13-AUG-1999', '%d-%b-%Y')
        , 'SH_CLERK'
        , 3600
        , NULL
        , 122
        , 50
        );

INSERT INTO employees VALUES 
        ( 190
        , 'Timothy'
        , 'Gates'
        , 'TGATES'
        , '650.505.3876'
        , STR_TO_DATE('11-JUL-1997', '%d-%b-%Y')
        , 'SH_CLERK'
        , 2900
        , NULL
        , 122
        , 50
        );

INSERT INTO employees VALUES 
        ( 191
        , 'Randall'
        , 'Perkins'
        , 'RPERKINS'
        , '650.505.4876'
        , STR_TO_DATE('19-DEC-1999', '%d-%b-%Y')
        , 'SH_CLERK'
        , 2500
        , NULL
        , 122
        , 50
        );

INSERT INTO employees VALUES 
        ( 192
        , 'Sarah'
        , 'Bell'
        , 'SBELL'
        , '650.501.1876'
        , STR_TO_DATE('04-FEB-1996', '%d-%b-%Y')
        , 'SH_CLERK'
        , 4000
        , NULL
        , 123
        , 50
        );

INSERT INTO employees VALUES 
        ( 193
        , 'Britney'
        , 'Everett'
        , 'BEVERETT'
        , '650.501.2876'
        , STR_TO_DATE('03-MAR-1997', '%d-%b-%Y')
        , 'SH_CLERK'
        , 3900
        , NULL
        , 123
        , 50
        );

INSERT INTO employees VALUES 
        ( 194
        , 'Samuel'
        , 'McCain'
        , 'SMCCAIN'
        , '650.501.3876'
        , STR_TO_DATE('01-JUL-1998', '%d-%b-%Y')
        , 'SH_CLERK'
        , 3200
        , NULL
        , 123
        , 50
        );

INSERT INTO employees VALUES 
        ( 195
        , 'Vance'
        , 'Jones'
        , 'VJONES'
        , '650.501.4876'
        , STR_TO_DATE('17-AUG-1999', '%d-%b-%Y')
        , 'SH_CLERK'
        , 2800
        , NULL
        , 123
        , 50
        );

INSERT INTO employees VALUES 
        ( 196
        , 'Alana'
        , 'Walsh'
        , 'AWALSH'
        , '650.507.9811'
        , STR_TO_DATE('24-APR-1998', '%d-%b-%Y')
        , 'SH_CLERK'
        , 3100
        , NULL
        , 124
        , 50
        );

INSERT INTO employees VALUES 
        ( 197
        , 'Kevin'
        , 'Feeney'
        , 'KFEENEY'
        , '650.507.9822'
        , STR_TO_DATE('23-MAY-1998', '%d-%b-%Y')
        , 'SH_CLERK'
        , 3000
        , NULL
        , 124
        , 50
        );

INSERT INTO employees VALUES 
        ( 198
        , 'Donald'
        , 'OConnell'
        , 'DOCONNEL'
        , '650.507.9833'
        , STR_TO_DATE('21-JUN-1999', '%d-%b-%Y')
        , 'SH_CLERK'
        , 2600
        , NULL
        , 124
        , 50
        );

INSERT INTO employees VALUES 
        ( 199
        , 'Douglas'
        , 'Grant'
        , 'DGRANT'
        , '650.507.9844'
        , STR_TO_DATE('13-JAN-2000', '%d-%b-%Y')
        , 'SH_CLERK'
        , 2600
        , NULL
        , 124
        , 50
        );

INSERT INTO employees VALUES 
        ( 200
        , 'Jennifer'
        , 'Whalen'
        , 'JWHALEN'
        , '515.123.4444'
        , STR_TO_DATE('17-SEP-1987', '%d-%b-%Y')
        , 'AD_ASST'
        , 4400
        , NULL
        , 101
        , 10
        );

INSERT INTO employees VALUES 
        ( 201
        , 'Michael'
        , 'Hartstein'
        , 'MHARTSTE'
        , '515.123.5555'
        , STR_TO_DATE('17-FEB-1996', '%d-%b-%Y')
        , 'MK_MAN'
        , 13000
        , NULL
        , 100
        , 20
        );

INSERT INTO employees VALUES 
        ( 202
        , 'Pat'
        , 'Fay'
        , 'PFAY'
        , '603.123.6666'
        , STR_TO_DATE('17-AUG-1997', '%d-%b-%Y')
        , 'MK_REP'
        , 6000
        , NULL
        , 201
        , 20
        );

INSERT INTO employees VALUES 
        ( 203
        , 'Susan'
        , 'Mavris'
        , 'SMAVRIS'
        , '515.123.7777'
        , STR_TO_DATE('07-JUN-1994', '%d-%b-%Y')
        , 'HR_REP'
        , 6500
        , NULL
        , 101
        , 40
        );

INSERT INTO employees VALUES 
        ( 204
        , 'Hermann'
        , 'Baer'
        , 'HBAER'
        , '515.123.8888'
        , STR_TO_DATE('07-JUN-1994', '%d-%b-%Y')
        , 'PR_REP'
        , 10000
        , NULL
        , 101
        , 70
        );

INSERT INTO employees VALUES 
        ( 205
        , 'Shelley'
        , 'Higgins'
        , 'SHIGGINS'
        , '515.123.8080'
        , STR_TO_DATE('07-JUN-1994', '%d-%b-%Y')
        , 'AC_MGR'
        , 12000
        , NULL
        , 101
        , 110
        );

INSERT INTO employees VALUES 
        ( 206
        , 'William'
        , 'Gietz'
        , 'WGIETZ'
        , '515.123.8181'
        , STR_TO_DATE('07-JUN-1994', '%d-%b-%Y')
        , 'AC_ACCOUNT'
        , 8300
        , NULL
        , 205
        , 110
        );

















-- Prompt ******  Populating JOB_HISTORY table ....

INSERT INTO job_history
VALUES (102
       , STR_TO_DATE('13-JAN-1993', '%d-%b-%Y')
       , STR_TO_DATE('24-JUL-1998', '%d-%b-%Y')
       , 'IT_PROG'
       , 60);

INSERT INTO job_history
VALUES (101
       , STR_TO_DATE('21-SEP-1989', '%d-%b-%Y')
       , STR_TO_DATE('27-OCT-1993', '%d-%b-%Y')
       , 'AC_ACCOUNT'
       , 110);

INSERT INTO job_history
VALUES (101
       , STR_TO_DATE('28-OCT-1993', '%d-%b-%Y')
       , STR_TO_DATE('15-MAR-1997', '%d-%b-%Y')
       , 'AC_MGR'
       , 110);

INSERT INTO job_history
VALUES (201
       , STR_TO_DATE('17-FEB-1996', '%d-%b-%Y')
       , STR_TO_DATE('19-DEC-1999', '%d-%b-%Y')
       , 'MK_REP'
       , 20);

INSERT INTO job_history
VALUES  (114
        , STR_TO_DATE('24-MAR-1998', '%d-%b-%Y')
        , STR_TO_DATE('31-DEC-1999', '%d-%b-%Y')
        , 'ST_CLERK'
        , 50
        );

INSERT INTO job_history
VALUES  (122
        , STR_TO_DATE('01-JAN-1999', '%d-%b-%Y')
        , STR_TO_DATE('31-DEC-1999', '%d-%b-%Y')
        , 'ST_CLERK'
        , 50
        );

INSERT INTO job_history
VALUES  (200
        , STR_TO_DATE('17-SEP-1987', '%d-%b-%Y')
        , STR_TO_DATE('17-JUN-1993', '%d-%b-%Y')
        , 'AD_ASST'
        , 90
        );

INSERT INTO job_history
VALUES  (176
        , STR_TO_DATE('24-MAR-1998', '%d-%b-%Y')
        , STR_TO_DATE('31-DEC-1998', '%d-%b-%Y')
        , 'SA_REP'
        , 80
        );

INSERT INTO job_history
VALUES  (176
        , STR_TO_DATE('01-JAN-1999', '%d-%b-%Y')
        , STR_TO_DATE('31-DEC-1999', '%d-%b-%Y')
        , 'SA_MAN'
        , 80
        );

INSERT INTO job_history
VALUES  (200
        , STR_TO_DATE('01-JUL-1994', '%d-%b-%Y')
        , STR_TO_DATE('31-DEC-1998', '%d-%b-%Y')
        , 'AC_ACCOUNT'
        , 90
        );



















-- Create Indexes

CREATE INDEX emp_department_ix ON employees (department_id);
CREATE INDEX emp_job_ix ON employees (job_id);
CREATE INDEX emp_manager_ix ON employees (manager_id);
CREATE INDEX emp_name_ix ON employees (last_name, first_name);

CREATE INDEX dept_location_ix ON departments (location_id);

CREATE INDEX jhist_job_ix ON job_history (job_id);
CREATE INDEX jhist_employee_ix ON job_history (employee_id);
CREATE INDEX jhist_department_ix ON job_history (department_id);

CREATE INDEX loc_city_ix ON locations (city);
CREATE INDEX loc_state_province_ix ON locations (state_province);
CREATE INDEX loc_country_ix ON locations (country_id);


















ALTER TABLE regions
MODIFY COLUMN region_id INT COMMENT 'Primary key of regions table';

ALTER TABLE regions
MODIFY COLUMN region_name VARCHAR(255) COMMENT 'Names of regions. Locations are in the countries of these regions';

ALTER TABLE locations
MODIFY COLUMN location_id INT COMMENT 'Primary key of locations table';

ALTER TABLE locations
MODIFY COLUMN street_address VARCHAR(255) COMMENT 'Street address of an office, warehouse, or production site of a company. Contains building number and street name';

ALTER TABLE locations
MODIFY COLUMN postal_code VARCHAR(20) COMMENT 'Postal code of the location of an office, warehouse, or production site of a company';

ALTER TABLE locations
MODIFY COLUMN city VARCHAR(255) COMMENT 'A not null column that shows city where an office, warehouse, or production site of a company is located';

ALTER TABLE locations
MODIFY COLUMN state_province VARCHAR(255) COMMENT 'State or Province where an office, warehouse, or production site of a company is located';


ALTER TABLE departments
MODIFY COLUMN department_id INT COMMENT 'Primary key column of departments table';

ALTER TABLE departments
MODIFY COLUMN department_name VARCHAR(255) COMMENT 'A not null column that shows name of a department. Administration, Marketing, Purchasing, Human Resources, Shipping, IT, Executive, Public Relations, Sales, Finance, and Accounting. ';

ALTER TABLE departments
MODIFY COLUMN manager_id INT COMMENT 'Manager_id of a department. Foreign key to employee_id column of employees table. The manager_id column of the employee table references this column';

ALTER TABLE departments
MODIFY COLUMN location_id INT COMMENT 'Location id where a department is located. Foreign key to location_id column of locations table';

ALTER TABLE job_history
MODIFY COLUMN employee_id INT COMMENT 'A not null column in the complex primary key employee_id+start_date. Foreign key to employee_id column of the employee table';

ALTER TABLE job_history
MODIFY COLUMN start_date DATE COMMENT 'A not null column in the complex primary key employee_id+start_date. Must be less than the end_date of the job_history table. (enforced by constraint jhist_date_interval)';

ALTER TABLE job_history
MODIFY COLUMN end_date DATE COMMENT 'Last day of the employee in this job role. A not null column. Must be greater than the start_date of the job_history table. (enforced by constraint jhist_date_interval)';

ALTER TABLE job_history
MODIFY COLUMN department_id INT COMMENT 'Department id in which the employee worked in the past; foreign key to department_id column in the departments table';


ALTER TABLE countries
MODIFY COLUMN country_name VARCHAR(255) COMMENT 'Country name';

ALTER TABLE countries
MODIFY COLUMN region_id INT COMMENT 'Region ID for the country. Foreign key to region_id column in the departments table';

ALTER TABLE jobs
MODIFY COLUMN job_title VARCHAR(255) COMMENT 'A not null column that shows job title, e.g. AD_VP, FI_ACCOUNTANT';

ALTER TABLE jobs
MODIFY COLUMN min_salary DECIMAL(10, 2) COMMENT 'Minimum salary for a job title';

ALTER TABLE jobs
MODIFY COLUMN max_salary DECIMAL(10, 2) COMMENT 'Maximum salary for a job title';

ALTER TABLE employees
MODIFY COLUMN employee_id INT COMMENT 'Primary key of employees table';

ALTER TABLE employees
MODIFY COLUMN first_name VARCHAR(255) COMMENT 'First name of the employee. A not null column.';

ALTER TABLE employees
MODIFY COLUMN last_name VARCHAR(255) COMMENT 'Last name of the employee. A not null column.';

ALTER TABLE employees
MODIFY COLUMN email VARCHAR(255) COMMENT 'Email id of the employee';

ALTER TABLE employees
MODIFY COLUMN phone_number VARCHAR(20) COMMENT 'Phone number of the employee; includes country code and area code';

ALTER TABLE employees
MODIFY COLUMN hire_date DATE COMMENT 'Date when the employee started on this job. A not null column.';

ALTER TABLE employees
MODIFY COLUMN salary DECIMAL(10, 2) COMMENT 'Monthly salary of the employee. Must be greater than zero (enforced by constraint emp_salary_min)';

ALTER TABLE employees
MODIFY COLUMN commission_pct DECIMAL(4, 2) COMMENT 'Commission percentage of the employee; Only employees in sales department eligible for commission percentage';

ALTER TABLE employees
MODIFY COLUMN manager_id INT COMMENT 'Manager id of the employee; has same domain as manager_id in departments table. Foreign key to employee_id column of employees table. (useful for reflexive joins and CONNECT BY query)';

ALTER TABLE employees
MODIFY COLUMN department_id INT COMMENT 'Department id where employee works; foreign key to department_id column of the departments table';