import zipfile
import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <div style="text-align: center; font-family: Tahoma; margin-top: 50px;">
        <h1>مرحباً بك في مشروع بطاقة آية الأسبوع للقرآن الكريم</h1>
        <p>السيرفر جاهز لإنشاء وتحميل بطاقة المحفظة الرقمية.</p>
        <a href="/download" style="padding: 10px 20px; background: #143228; color: white; text-decoration: none; border-radius: 5px;">تحميل البطاقة الرقمية</a>
    </div>
    '''

@app.route('/download')
def download_pass():
    filename = "quran_ayah.pkpass"
    
    # ننشئ ملف مضغوط بامتداد pkpass يحتوي على ملف البيانات
    with zipfile.ZipFile(filename, 'w') as zipf:
        zipf.write('pass.json')
    
    return send_file(filename, as_attachment=True, mimetype='application/vnd.apple.pkpass')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)