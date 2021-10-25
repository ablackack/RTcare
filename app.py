import glob
import json
import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

from db.db_connection_handler import DbConnectionHandler as dbHandler
from db.prepared_statements_digital import DbDigitalStatements as digStatement

app = Flask(__name__)
app.config['SECRET_KEY'] = 'veryimportantsecretkey'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/digital')
def digital_overview():
    return render_template('digital/overview.html')


@app.route('/digital/bsi_cards/show', methods=('GET', 'POST'))
def show_bsi_card():
    conn = dbHandler.get_connection_for_digital()
    bsi_cards = conn.execute(digStatement.SELECT_BSI_CARDS.value).fetchall()

    if request.method == 'POST':
        opta = request.form['opta']
        issi = request.form['issi']

        if not opta and not issi:
            flash('Both values are required')
        else:
            try:
                conn.execute(digStatement.ADD_BSI_CARD.value, (opta, issi))
                conn.commit()
                conn.close()

                return redirect(url_for('show_bsi_card'))
            except sqlite3.IntegrityError:
                flash('This card is already present in the database. Maybe you made a typo?')
                return render_template('digital/show_bsi_cards.html', bsi_cards=bsi_cards)

    return render_template('digital/show_bsi_cards.html', bsi_cards=bsi_cards)


@app.route('/digital/bsi_cards/edit/<int:id>', methods=('GET', 'POST'))
def edit_bsi_card(id):
    conn = dbHandler.get_connection_for_digital()
    bsi_card = conn.execute(digStatement.SELECT_BSI_CARD_BY_ID.value, (id,)).fetchone()

    if not bsi_card:
        abort(404)
    else:
        if request.method == 'POST':
            opta = request.form['opta']
            issi = request.form['issi']

            if not opta and not issi:
                flash('Both values are required')
            else:
                conn.execute(digStatement.UPDATE_BSI_CARD.value, (opta, issi, id))
                conn.commit()
                conn.close()

                return redirect(url_for('show_bsi_card'))

    return render_template('digital/edit_bsi_card.html', bsi_card=bsi_card)


@app.route('/digital/bsi_cards/delete/<int:id>', methods=('POST',))
def delete_bsi_card(id):
    conn = dbHandler.get_connection_for_digital()
    bsi_card = conn.execute(digStatement.SELECT_BSI_CARD_BY_ID.value, (id,)).fetchone()
    conn.execute(digStatement.DELETE_BSI_CARD.value, (id,))
    conn.commit()
    conn.close()
    flash('BSI card {} was successfully deleted'.format(bsi_card['opta']), category='info')

    return redirect(url_for('show_bsi_card'))


if __name__ == '__main__':
    app.run()
