# 24/7895	789.2024.1


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        expediente = request.form['expediente']
        procedimiento = request.form['procedimiento']
        nombre = request.form['nombre']
        nie = request.form['nie']
        nig = request.form['nig']
        
        # Extraer partes del expediente
        expediente_parts = expediente.split('/')
        expediente_year = expediente_parts[0][:2]
        expediente_num = expediente_parts[1]

        # Generar identificador
        identificador = f"ES_EA0020406_2024_EXP_{expediente_year}{expediente_num}"

        # Generar código procedimiento
        expediente_year_code = expediente_year
        expediente_num_code = expediente_num.zfill(7)
        codigo_procedimiento = f"380020{expediente_year_code}{expediente_num_code} DEVOLUCION"
        codigo_procedimiento_2 = f"380020{expediente_year_code}{expediente_num_code}"

        # Extraer parte del procedimiento para número
        procedimiento_parts = procedimiento.split('.')
        procedimiento_num = procedimiento_parts[0]
        procedimiento_num_padded = procedimiento_num.zfill(7)
        
        # Determinar unidad orgánica o juzgado
        ultimo_numero = procedimiento_parts[2]
        unidad_organica = {
            '1': 'J00000214',
            '2': 'J00000209',
            '3': 'J00000211',
            '4': 'J00000206'
        }.get(ultimo_numero, '')

        # Generar asunto
        asunto = f"REMISION EXPEDIENTE PAB {procedimiento_num} {procedimiento_parts[1]} - EXTRANJERIA {codigo_procedimiento_2}"

        # Generar texto personalizado
        texto_personalizado = (
            f"PAB {procedimiento}\n"
            f"EXTRANJERIA {codigo_procedimiento_2}\n"
            f"EXTRANJERO {nombre}\n"
            f"NIE {nie}"
        )

        return render_template('index.html',
                               expediente=expediente,
                               procedimiento=procedimiento,
                               nombre=nombre,
                               nie=nie,
                               nig=nig,
                               identificador=identificador,
                               codigo_procedimiento=codigo_procedimiento,
                               procedimiento_num_padded=procedimiento_num_padded,
                               asunto=asunto,
                               unidad_organica=unidad_organica,
                               texto_personalizado=texto_personalizado)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
