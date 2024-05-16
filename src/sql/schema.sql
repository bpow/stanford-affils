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
