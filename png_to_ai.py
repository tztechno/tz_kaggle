from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

# PNGファイルを開きます
png_file = "input.png"
img = Image.open(png_file)

# 新しいAIファイルを作成します
ai_file = "output.ai"
c = canvas.Canvas(ai_file, pagesize=letter)

# PNG画像をAIファイルに描画します
c.drawImage(ImageReader(img), x=100, y=100, width=img.width, height=img.height)

# AIファイルを保存します
c.showPage()
c.save()

print(f"{png_file} を {ai_file} に変換しました。")
