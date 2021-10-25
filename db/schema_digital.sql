DROP TABLE IF EXISTS manufacturers;
CREATE TABLE manufacturers (
    manufacturer_id INTEGER,
    name TEXT NOT NULL,
    PRIMARY KEY (manufacturer_id)
);

DROP TABLE IF EXISTS parameters;
CREATE TABLE parameters (
    parameter_id INTEGER,
    name TEXT NOT NULL,
    comment TEXT NULL,
    PRIMARY KEY (parameter_id)
);

DROP TABLE IF EXISTS firmwares;
CREATE TABLE firmwares (
    firmware_id INTEGER,
    name TEXT NOT NULL,
    PRIMARY KEY (firmware_id)
);

DROP TABLE IF EXISTS types;
CREATE TABLE types (
    type_id INTEGER,
    name TEXT NOT NULL,
    PRIMARY KEY (type_id)
);

DROP TABLE IF EXISTS models;
CREATE TABLE models (
    model_id INTEGER,
    type_id INTEGER NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (model_id),
    FOREIGN KEY (type_id) REFERENCES types(type_id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);

DROP TABLE IF EXISTS devices;
CREATE TABLE devices (
    device_id INTEGER,
    model_id INTEGER NOT NULL,
    firmware_id INTEGER NOT NULL,
    parameter_id INTEGER NOT NULL,
    sn TEXT UNIQUE NOT NULL,
    tei TEXT UNIQUE NOT NULL,
    password TEXT NULL,
    comment TEXT NULL,
    PRIMARY KEY (device_id),
    FOREIGN KEY (model_id) REFERENCES models(model_id),
    FOREIGN KEY (firmware_id) REFERENCES firmwares(firmware_id),
    FOREIGN KEY (parameter_id) REFERENCES parameters(parameter_id)
);

DROP TABLE IF EXISTS bsi_cards;
CREATE TABLE bsi_cards (
    bsi_card_id INTEGER,
    issi TEXT UNIQUE NOT NULL,
    opta TEXT UNIQUE NOT NULL,
    PRIMARY KEY (bsi_card_id)
);

DROP TABLE IF EXISTS units;
CREATE TABLE units(
    device_id INTEGER,
    bsi_card_id INTEGER,
    callsign TEXT,
    PRIMARY KEY (device_id, bsi_card_id),
    FOREIGN KEY (device_id) REFERENCES devices(device_id),
    FOREIGN KEY (bsi_card_id) REFERENCES bsi_cards(bsi_card_id)
);
