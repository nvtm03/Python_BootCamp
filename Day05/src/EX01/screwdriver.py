from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory, jsonify
import os
import sys
import requests

app = Flask(__name__)
app.secret_key = 'my_secret_key'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3', 'ogg', 'wav'}


os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    """Проверяет, имеет ли файл допустимое расширение."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        flash('File successfully uploaded')
        return redirect(url_for('index'))
    else:
        flash('Non-audio file detected')
        return redirect(url_for('index'))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    try:
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        flash(f'File {filename} successfully deleted')
    except Exception as e:
        flash(f'Error deleting file {filename}: {str(e)}')
    return redirect(url_for('index'))


@app.route('/files', methods=['GET'])
def list_files():
    """Возвращает список загруженных файлов в формате JSON."""
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files)


def run_server():
    app.run(port=8888)


def upload_file_cli(file_path):
    """Загружает аудиофайл на сервер."""
    url = 'http://127.0.0.1:8888/upload'
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print("File successfully uploaded")
        else:
            print("Failed to upload file")


def list_files_cli():
    """Получает и выводит список загруженных файлов."""
    url = 'http://127.0.0.1:8888/files'
    response = requests.get(url)
    if response.status_code == 200:
        print("List of uploaded files:")
        files = response.json()
        for file in files:
            print(file)
    else:
        print("Failed to retrieve file list.")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'upload' and len(sys.argv) == 3:
            if allowed_file(sys.argv[2]):
                upload_file_cli(sys.argv[2])
            else:
                print("Non-audio file detected.")
        elif command == 'list':
            list_files_cli()
        else:
            print("Invalid command or missing file path.")
    else:
        run_server()