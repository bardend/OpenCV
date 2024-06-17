from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para recibir y procesar el JSON enviado desde el programa de captura
@app.route('/update_frame', methods=['POST'])
def update_frame():
    try:
        # Obtener el JSON enviado desde el programa de captura
        frame_json = request.json
        
        # Imprimir cada par clave-valor del JSON recibido en la consola del servidor
        print("Pares clave-valor del JSON recibido:")
        for key, value in frame_json.items():
            print(f" {key} : {value},")
        
        # Aquí puedes procesar el JSON según tus necesidades
        # Por ejemplo, podrías guardar los datos en una base de datos o realizar algún tipo de análisis

        # Devolver el número 3 como respuesta
        return jsonify({"numero": 3}), 200
    except Exception as e:
        # Imprimir detalles sobre el error
        print(f"Error al procesar JSON: {e}")
        return jsonify({"error": "Error al procesar JSON"}), 400

if __name__ == '__main__':
    # Iniciar el servidor Flask
    app.run(debug=True)

