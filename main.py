# main.py

    # TERMINAL:
# 1-)  cd "...\Case__Advertisement_Machine-Learning"
# 2-)  python -m venv venv
# 3-)  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# 4-)  .\venv\Scripts\Activate
# 5-)  pip install fastapi uvicorn pillow


from fastapi import FastAPI, File, UploadFile, Form, HTTPException, APIRouter
from fastapi.responses import Response, RedirectResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = FastAPI(
    title="Reklam Görseli Oluşturma API",
    description="Bu API, kullanıcılara yükledikleri görseller ve metinler kullanılarak dinamik reklam görselleri oluşturma imkanı sağlar.",
)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


FONT_PATH = "PlayfairDisplay-SemiBold.ttf"

@app.post("/create-ad/", summary="Reklam Görseli Oluştur",
          description="Yüklenen görsel ve logo ile birlikte renk, punchline ve buton metni kullanarak reklam görseli oluşturur.")
async def create_ad(
    image: UploadFile = File(..., description="Reklam için ana görsel."),
    logo: UploadFile = File(..., description="Reklamda kullanılacak logo."),
    color_hex: str = Form(..., description="Punchline ve buton için renk kodu (hex formatında)."),
    punchline: str = Form(..., description="Reklamda gösterilecek punchline metni."),
    button_text: str = Form(..., description="Buton üzerinde görünecek metin.")
):
    try:
        image_content = await image.read()
        logo_content = await logo.read()
        image = Image.open(BytesIO(image_content)).convert("RGBA")
        logo = Image.open(BytesIO(logo_content)).convert("RGBA")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image data: {e}")


    desired_image_size = (336, 328)
    image = image.resize(desired_image_size, Image.Resampling.LANCZOS)


    desired_logo_size = (132, 82)
    logo = logo.resize(desired_logo_size, Image.Resampling.LANCZOS)

    background = Image.new("RGB", (736, 739), "white")


    coffee_x = (background.width - image.width) // 2
    coffee_y = 20 + logo.height + 10
    background.paste(image, (coffee_x, coffee_y), image)

    logo_x_centered = (background.width - logo.width) // 2
    background.paste(logo, (logo_x_centered, 20), logo)


    try:
        punchline_font = ImageFont.truetype(FONT_PATH, 46)
        button_font = ImageFont.truetype(FONT_PATH, 18)
    except IOError:
        raise HTTPException(status_code=500, detail="Font file not found")

    draw = ImageDraw.Draw(background)


    max_length = 30
    if len(punchline) > max_length:
        split_point = punchline.rfind(' ', 0, max_length)
        first_line = punchline[:split_point]
        second_line = punchline[split_point + 1:]
    else:
        first_line = punchline
        second_line = ""


    text_width, text_height = draw.textsize(first_line, font=punchline_font)
    text_x = (background.width - text_width) // 2
    punchline_y = coffee_y + image.height + 20
    draw.text((text_x, punchline_y), first_line, fill=color_hex, font=punchline_font)


    if second_line:
        text_x = (background.width - draw.textsize(second_line, font=punchline_font)[0]) // 2
        draw.text((text_x, punchline_y + text_height + 5), second_line, fill=color_hex, font=punchline_font)


    button_width, button_height = draw.textsize(button_text, font=button_font)
    button_x = (background.width - button_width) // 2
    button_y = punchline_y + text_height * 2 + 50
    draw.rectangle([button_x - 10, button_y - 10, button_x + button_width + 10, button_y + button_height + 10], fill=color_hex)
    draw.text((button_x, button_y), button_text, fill="white", font=button_font)


    img_byte_arr = BytesIO()
    background.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return Response(content=img_byte_arr, media_type="image/png")


    # TERMINAL:
# 6-)  uvicorn main:app --reload