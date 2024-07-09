# courses/utils.py
from PIL import Image, ImageDraw, ImageFont

def create_certificate_image(student, course):
    image = Image.open("certificate_template.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 60)
    draw.text((300, 300), f"Certificat de {student.user.full_name}", (0, 0, 0), font=font)
    draw.text((300, 400), f"Pour avoir complété le cours {course.nom}", (0, 0, 0), font=font)
    file_path = f"certificates/{student.user.id}_{course.id}.png"
    image.save(file_path)
    return file_path
