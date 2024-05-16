PRAGMA foreign_keys = OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS affiliations (
    id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL UNIQUE,
    coordinator TEXT,
    coordinator_email TEXT,
    status TEXT,
    type TEXT,
    family TEXT,
    members TEXT,
    approvers TEXT,
    clinvar_submitter_ids TEXT,
    PRIMARY KEY (id)
);
INSERT INTO affiliations VALUES (
    10000, 'Interface Admin', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL
);
INSERT INTO affiliations VALUES (
    10001, 'KCNQ1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL
);
COMMIT;
