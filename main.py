from flask import Flask
app = Flask(__name__)
@app.get("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>Lab Điện toán đám mây - PaaS</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f3f6fb;
                display: flex;
                justify-content: center;
                padding-top: 100px;
            }
            .box {
                background: white;
                padding: 35px 50px;
                border-radius: 12px;
                box-shadow: 0 4px 15px #ddd;
            }
            h1 { color: #1f5fbf; }
            .ok { color: green; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>LAB ĐIỆN TOÁN ĐÁM MÂY</h1>
            <h2>Mô hình PaaS - Render</h2>
            <p>Sinh viên: HOÀNG THỊ XUÂN THỊNH</p>
            <p>MSSV: 2324802010131</p>
            <p>Ngôn ngữ: Python - Flask</p>
            <p class="ok">Ứng dụng hoạt động thành công!</p>
        </div>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(port=8081)