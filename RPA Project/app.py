from flask import Flask, request, render_template, redirect, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

UPLOAD_FOLDER = r"C:\Users\SURANJANA\Documents\Dataset"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect('/')
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect('/')
    
    # Check file name
    if file.filename != 'employee.xlsx':
        flash('Error: File must be named "employee.xlsx"')
        return redirect('/')
    
    try:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        flash('File successfully uploaded!')
    except Exception as e:
        flash(f'Error: {str(e)}')
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
