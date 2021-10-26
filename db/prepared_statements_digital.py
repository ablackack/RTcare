from enum import Enum


class DbDigitalStatements(Enum):
    SELECT_BSI_CARDS = 'SELECT * FROM bsi_cards'
    SELECT_BSI_CARD_BY_ID = 'SELECT * FROM bsi_cards WHERE bsi_card_id = ?'
    ADD_BSI_CARD = 'INSERT INTO bsi_cards (opta, issi) VALUES (?, ?)'
    UPDATE_BSI_CARD = 'UPDATE bsi_cards SET opta = ?, issi = ? WHERE bsi_card_id = ?'
    DELETE_BSI_CARD = 'DELETE FROM bsi_cards WHERE bsi_card_id = ?'

    SELECT_MANUFACTURERS = 'SELECT * FROM manufacturers'
    SELECT_MANUFACTURER_BY_ID = 'SELECT * FROM manufacturers WHERE manufacturer_id = ?'
    ADD_MANUFACTURER = 'INSERT INTO manufacturers (name) VALUES (?)'
    UPDATE_MANUFACTURER = 'UPDATE manufacturers SET name = ? WHERE manufacturer_id = ?'
    DELETE_MANUFACTURER = 'DELETE FROM manufacturers WHERE manufacturer_id = ?'

    SELECT_FIRMWARES = 'SELECT * FROM firmwares'
    SELECT_FIRMWARE_BY_ID = 'SELECT * FROM firmwares WHERE firmware_id = ?'
    ADD_FIRMWARE = 'INSERT INTO firmwares (name) VALUES (?)'
    UPDATE_FIRMWARE = 'UPDATE firmwares SET name = ? WHERE firmware_id = ?'
    DELETE_FIRMWARE = 'DELETE FROM firmwares WHERE firmware_id = ?'

    SELECT_TYPES = 'SELECT * FROM types'
    SELECT_TYPE_BY_ID = 'SELECT * FROM types WHERE type_id = ?'
    ADD_TYPE = 'INSERT INTO types (name) VALUES (?)'
    UPDATE_TYPE = 'UPDATE types SET name = ? WHERE type_id = ?'
    DELETE_TYPE = 'DELETE FROM types WHERE type_id = ?'

    SELECT_PARAMETERS = 'SELECT * FROM parameters'
    SELECT_PARAMETER_BY_ID = 'SELECT * FROM parameters WHERE parameter_id = ?'
    ADD_PARAMETER = 'INSERT INTO parameters (name, comment) VALUES (?, ?)'
    UPDATE_PARAMETER = 'UPDATE parameters SET name = ?, comment = ? WHERE parameter_id = ?'
    DELETE_PARAMETER = 'DELETE FROM parameters WHERE parameter_id = ?'

    SELECT_MODELS = 'SELECT * FROM models'
    SELECT_MODEL_BY_ID = 'SELECT * FROM models WHERE model_id = ?'
    ADD_MODEL = 'INSERT INTO models (type_id, manufacturer_id, name) VALUES (?, ?, ?)'
    UPDATE_MODEL = 'UPDATE models SET type_id = ?, manufacturer_id = ?, name = ? WHERE model_id = ?'
    DELETE_MODEL = 'DELETE FROM models WHERE model_id = ?'

