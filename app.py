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


# Digital
@app.route('/digital')
def digital_overview():
    return render_template('digital/overview.html')


# Digital - BSI cards
@app.route('/digital/bsi_cards/show', methods=('GET', 'POST'))
def show_bsi_cards():
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

                return redirect(url_for('show_bsi_cards'))
            except sqlite3.IntegrityError:
                flash('This card is already present in the database. Maybe you made a typo?')
                return render_template('digital/bsi_cards/show.html', bsi_cards=bsi_cards)

    return render_template('digital/bsi_cards/show.html', bsi_cards=bsi_cards)


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

                return redirect(url_for('show_bsi_cards'))

    return render_template('digital/bsi_cards/edit.html', bsi_card=bsi_card)


@app.route('/digital/bsi_cards/delete/<int:id>', methods=('POST',))
def delete_bsi_card(id):
    conn = dbHandler.get_connection_for_digital()
    bsi_card = conn.execute(digStatement.SELECT_BSI_CARD_BY_ID.value, (id,)).fetchone()
    conn.execute(digStatement.DELETE_BSI_CARD.value, (id,))
    conn.commit()
    conn.close()
    flash('BSI card {} was successfully deleted'.format(bsi_card['opta']), category='info')

    return redirect(url_for('show_bsi_cards'))


# Digital - Manufacturer
@app.route('/digital/manufacturers/show', methods=('GET', 'POST'))
def show_manufacturers():
    conn = dbHandler.get_connection_for_digital()
    manufacturers = conn.execute(digStatement.SELECT_MANUFACTURERS.value).fetchall()

    if request.method == 'POST':
        name = request.form['name']

        if not name:
            flash('Value is required')
        else:
            try:
                conn.execute(digStatement.ADD_MANUFACTURER.value, (name,))
                conn.commit()
                conn.close()

                return redirect(url_for('show_manufacturers'))
            except sqlite3.IntegrityError:
                flash('This manufacturer is already present in the database. Maybe you made a typo?')
                return render_template('digital/manufacturers/show.html', manufacturers=manufacturers)

    return render_template('digital/manufacturers/show.html', manufacturers=manufacturers)


@app.route('/digital/manufacturers/edit/<int:id>', methods=('GET', 'POST'))
def edit_manufacturer(id):
    conn = dbHandler.get_connection_for_digital()
    manufacturer = conn.execute(digStatement.SELECT_MANUFACTURER_BY_ID.value, (id,)).fetchone()

    if not manufacturer:
        abort(404)
    else:
        if request.method == 'POST':
            name = request.form['name']

            if not name:
                flash('Value is required')
            else:
                conn.execute(digStatement.UPDATE_MANUFACTURER.value, (name, id))
                conn.commit()
                conn.close()

                return redirect(url_for('show_manufacturers'))

    return render_template('digital/manufacturers/edit.html', manufacturer=manufacturer)


@app.route('/digital/manufacturers/delete/<int:id>', methods=('POST',))
def delete_manufacturer(id):
    conn = dbHandler.get_connection_for_digital()
    manufacturer = conn.execute(digStatement.SELECT_MANUFACTURER_BY_ID.value, (id,)).fetchone()
    conn.execute(digStatement.DELETE_MANUFACTURER.value, (id,))
    conn.commit()
    conn.close()
    flash('Manufacturer {} was successfully deleted'.format(manufacturer['name']), category='info')

    return redirect(url_for('show_manufacturers'))


# Digital - Firmware
@app.route('/digital/firmwares/show', methods=('GET', 'POST'))
def show_firmwares():
    conn = dbHandler.get_connection_for_digital()
    firmwares = conn.execute(digStatement.SELECT_FIRMWARES.value).fetchall()

    if request.method == 'POST':
        name = request.form['name']

        if not name:
            flash('Value is required')
        else:
            try:
                conn.execute(digStatement.ADD_FIRMWARE.value, (name,))
                conn.commit()
                conn.close()

                return redirect(url_for('show_firmwares'))
            except sqlite3.IntegrityError:
                flash('This firmware is already present in the database. Maybe you made a typo?')
                return render_template('digital/firmwares/show.html', firmwares=firmwares)

    return render_template('digital/firmwares/show.html', firmwares=firmwares)


@app.route('/digital/firmwares/edit/<int:id>', methods=('GET', 'POST'))
def edit_firmware(id):
    conn = dbHandler.get_connection_for_digital()
    firmware = conn.execute(digStatement.SELECT_FIRMWARE_BY_ID.value, (id,)).fetchone()

    if not firmware:
        abort(404)
    else:
        if request.method == 'POST':
            name = request.form['name']

            if not name:
                flash('Value is required')
            else:
                conn.execute(digStatement.UPDATE_FIRMWARE.value, (name, id))
                conn.commit()
                conn.close()

                return redirect(url_for('show_firmwares'))

    return render_template('digital/firmwares/edit.html', firmware=firmware)


@app.route('/digital/firmwares/delete/<int:id>', methods=('POST',))
def delete_firmware(id):
    conn = dbHandler.get_connection_for_digital()
    firmware = conn.execute(digStatement.SELECT_FIRMWARE_BY_ID.value, (id,)).fetchone()
    conn.execute(digStatement.DELETE_FIRMWARE.value, (id,))
    conn.commit()
    conn.close()
    flash('Manufacturer {} was successfully deleted'.format(firmware['name']), category='info')

    return redirect(url_for('show_firmwares'))


# Digital - Type
@app.route('/digital/types/show', methods=('GET', 'POST'))
def show_types():
    conn = dbHandler.get_connection_for_digital()
    types = conn.execute(digStatement.SELECT_TYPES.value).fetchall()

    if request.method == 'POST':
        name = request.form['name']

        if not name:
            flash('Value is required')
        else:
            try:
                conn.execute(digStatement.ADD_TYPE.value, (name,))
                conn.commit()
                conn.close()

                return redirect(url_for('show_types'))
            except sqlite3.IntegrityError:
                flash('This type is already present in the database. Maybe you made a typo?')
                return render_template('digital/types/show.html', types=types)

    return render_template('digital/types/show.html', types=types)


@app.route('/digital/types/edit/<int:id>', methods=('GET', 'POST'))
def edit_type(id):
    conn = dbHandler.get_connection_for_digital()
    type = conn.execute(digStatement.SELECT_TYPE_BY_ID.value, (id,)).fetchone()

    if not type:
        abort(404)
    else:
        if request.method == 'POST':
            name = request.form['name']

            if not name:
                flash('Value is required')
            else:
                conn.execute(digStatement.UPDATE_TYPE.value, (name, id))
                conn.commit()
                conn.close()

                return redirect(url_for('show_types'))

    return render_template('digital/types/edit.html', type=type)


@app.route('/digital/types/delete/<int:id>', methods=('POST',))
def delete_type(id):
    conn = dbHandler.get_connection_for_digital()
    type = conn.execute(digStatement.SELECT_TYPE_BY_ID.value, (id,)).fetchone()
    conn.execute(digStatement.DELETE_TYPE.value, (id,))
    conn.commit()
    conn.close()
    flash('Type {} was successfully deleted'.format(type['name']), category='info')

    return redirect(url_for('show_types'))


# Digital - Parameters
@app.route('/digital/parameters/show', methods=('GET', 'POST'))
def show_parameters():
    conn = dbHandler.get_connection_for_digital()
    parameters = conn.execute(digStatement.SELECT_PARAMETERS.value).fetchall()

    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']

        if not name and not comment:
            flash('Both values are required')
        else:
            try:
                conn.execute(digStatement.ADD_PARAMETER.value, (name, comment))
                conn.commit()
                conn.close()

                return redirect(url_for('show_parameters'))
            except sqlite3.IntegrityError:
                flash('This parameter is already present in the database. Maybe you made a typo?')
                return render_template('digital/parameters/show.html', parameters=parameters)

    return render_template('digital/parameters/show.html', parameters=parameters)


@app.route('/digital/parameters/edit/<int:id>', methods=('GET', 'POST'))
def edit_parameter(id):
    conn = dbHandler.get_connection_for_digital()
    parameter = conn.execute(digStatement.SELECT_PARAMETER_BY_ID.value, (id,)).fetchone()

    if not parameter:
        abort(404)
    else:
        if request.method == 'POST':
            name = request.form['name']
            comment = request.form['comment']

            if not name:
                flash('Both values are required')
            else:
                conn.execute(digStatement.UPDATE_PARAMETER.value, (name, comment, id))
                conn.commit()
                conn.close()

                return redirect(url_for('show_parameters'))

    return render_template('digital/parameters/edit.html', parameter=parameter)


@app.route('/digital/parameters/delete/<int:id>', methods=('POST',))
def delete_parameter(id):
    conn = dbHandler.get_connection_for_digital()
    parameter = conn.execute(digStatement.SELECT_PARAMETER_BY_ID.value, (id,)).fetchone()
    conn.execute(digStatement.DELETE_PARAMETER.value, (id,))
    conn.commit()
    conn.close()
    flash('Parameter {} was successfully deleted'.format(parameter['name']), category='info')

    return redirect(url_for('show_parameters'))


# Digital - Model
@app.route('/digital/models/show', methods=('GET', 'POST'))
def show_models():
    conn = dbHandler.get_connection_for_digital()
    models = conn.execute(digStatement.SELECT_MODELS.value).fetchall()
    types = conn.execute(digStatement.SELECT_TYPES.value).fetchall()
    manufacturers = conn.execute(digStatement.SELECT_MANUFACTURERS.value).fetchall()
    model_dict = {}

    for model in models:
        type_id = model['type_id']
        manufacturer_id = model['manufacturer_id']

        type = conn.execute(digStatement.SELECT_TYPE_BY_ID.value, (type_id,)).fetchone()
        manufacturer = conn.execute(digStatement.SELECT_MANUFACTURER_BY_ID.value, (manufacturer_id,)).fetchone()

        model_option_dict = {'type': type, 'manufacturer': manufacturer}
        model_dict[model] = model_option_dict

    if request.method == 'POST':
        req_type_id = request.form['type_id']
        req_manufacturer_id = request.form['manufacturer_id']
        req_name = request.form['name']

        if not req_type_id and not req_manufacturer_id and not req_name:
            flash('All values are required')
        else:
            try:
                conn.execute(digStatement.ADD_MODEL.value, (req_type_id, req_manufacturer_id, req_name))
                conn.commit()
                conn.close()

                return redirect(url_for('show_models'))
            except sqlite3.IntegrityError:
                flash('This model is already present in the database. Maybe you made a typo?')
                return render_template('digital/parameters/show.html', model_dict=model_dict,
                                       manufacturers=manufacturers, types=types)

    return render_template('digital/models/show.html', model_dict=model_dict, manufacturers=manufacturers, types=types)


@app.route('/digital/models/edit/<int:id>', methods=('GET', 'POST'))
def edit_model(id):
    conn = dbHandler.get_connection_for_digital()
    model = conn.execute(digStatement.SELECT_MODEL_BY_ID.value, (id,)).fetchone()
    type = conn.execute(digStatement.SELECT_TYPE_BY_ID.value, (model['type_id'],))
    manufacturer = conn.execute(digStatement.SELECT_MANUFACTURER_BY_ID.value, (model['manufacturer_id'],))
    db_types = conn.execute(digStatement.SELECT_TYPES.value).fetchall()
    db_manufacturers = conn.execute(digStatement.SELECT_MANUFACTURERS.value).fetchall()

    if not model:
        abort(404)
    else:
        if request.method == 'POST':
            req_name = request.form['name']
            req_type_id = request.form['type_id']
            req_manufacturer_id = request.form['manufacturer_id']

            if not req_name and not req_type_id and not req_manufacturer_id:
                flash('All values are required')
            else:
                conn.execute(digStatement.UPDATE_MODEL.value, (req_type_id, req_manufacturer_id, req_name, id))
                conn.commit()
                conn.close()

                return redirect(url_for('show_models'))

    return render_template('digital/models/edit.html', db_types=db_types, db_manufacturers=db_manufacturers,
                           model=model, type=type, manufacturer=manufacturer)


@app.route('/digital/models/delete/<int:id>', methods=('POST',))
def delete_model(id):
    conn = dbHandler.get_connection_for_digital()
    model = conn.execute(digStatement.SELECT_MODEL_BY_ID.value, (id,)).fetchone()
    conn.execute(digStatement.DELETE_MODEL.value, (id,))
    conn.commit()
    conn.close()
    flash('Model {} was successfully deleted'.format(model['name']), category='info')

    return redirect(url_for('show_models'))


if __name__ == '__main__':
    app.run()
