from flask import Flask, Response, render_template, request, jsonify
import cv2
import numpy as np
import imageio
from queue import Queue
import os  # Importe a biblioteca os para manipulação de arquivos e diretórios

app = Flask(__name__)

# Variáveis de controle de gravação
recording = False
recording_frames = Queue()

def gen_frames():
    global recording_frames
    cap = cv2.VideoCapture("http://192.168.2.151:81/stream", cv2.CAP_FFMPEG)
    cap.set(cv2.CAP_PROP_FPS, 24)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Ajuste o tamanho do buffer de vídeo

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Sem frame de vídeo")
            break

        # Codifique o frame como JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Se estiver gravando, adicione o frame à fila
        if recording:
            recording_frames.put(frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_recording', methods=['POST'])
def start_recording():
    global recording, recording_frames
    recording = True
    recording_frames = Queue()  # Limpa a fila quando inicia a gravação
    return jsonify({'status': 'Recording started'})

@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    global recording
    recording = False
    return jsonify({'status': 'Recording stopped'})

@app.route('/download_recording')
def download_recording():
    if recording_frames.qsize() > 0:
        # Crie o diretório 'static' se não existir
        directory = 'static'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Crie o arquivo de vídeo usando a biblioteca imageio
        video_path = 'static/recording.mp4'
        writer = imageio.get_writer(video_path, fps=24)

        while not recording_frames.empty():
            frame = np.frombuffer(recording_frames.get(), dtype=np.uint8)
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            writer.append_data(frame)

        writer.close()

        return jsonify({'status': 'Recording downloaded'})
    else:
        return jsonify({'status': 'No frames to download'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
