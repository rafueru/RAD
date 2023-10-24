CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT,
    state TEXT,
    phone TEXT,
    email TEXT,
    experience TEXT,
    skills TEXT,
    linkedIn TEXT,
    employment_status TEXT,
    salary_expectation REAL,
    other_info TEXT
);

CREATE TABLE IF NOT EXISTS recruiters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    filter_city TEXT,
    filter_state TEXT,
    filter_salary REAL,
    filter_area TEXT,
    contact TEXT,
    status TEXT
);

