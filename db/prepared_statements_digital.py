from enum import Enum


class DbDigitalStatements(Enum):
    SELECT_BSI_CARDS = 'SELECT * FROM bsi_cards'
    SELECT_BSI_CARD_BY_ID = 'SELECT * FROM bsi_cards WHERE bsi_card_id = ?'
    ADD_BSI_CARD = 'INSERT INTO bsi_cards (opta, issi) VALUES (?, ?)'
    UPDATE_BSI_CARD = 'UPDATE bsi_cards SET opta = ?, issi = ? WHERE bsi_card_id = ?'
    DELETE_BSI_CARD = 'DELETE FROM bsi_cards WHERE bsi_card_id = ?'

