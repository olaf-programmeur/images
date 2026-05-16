# -*- coding: utf-8 -*-
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np
import os

SRC = r"D:\oroh\Documents\Personnel\Programmes\application_herve\images\a_modifier_temp"
DST = r"D:\oroh\Documents\Personnel\Programmes\application_herve\images"
SIZE = 300

CASCADE = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def detect_faces(img_path):
    img_cv = cv2.imread(img_path)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    faces = CASCADE.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))
    return faces, img_cv.shape[:2]


def face_center_crop(img_pil, faces, img_h, img_w, padding_ratio=0.55):
    if len(faces) == 0:
        return None

    # Bounding box englobant tous les visages détectés
    xs = [f[0] for f in faces]
    ys = [f[1] for f in faces]
    xe = [f[0] + f[2] for f in faces]
    ye = [f[1] + f[3] for f in faces]

    face_x = min(xs)
    face_y = min(ys)
    face_w = max(xe) - face_x
    face_h = max(ye) - face_y

    # Centre des visages
    cx = face_x + face_w // 2
    cy = face_y + face_h // 2

    # Taille du carré : faces + marge généreuse
    side = int(max(face_w, face_h) / padding_ratio)
    side = min(side, img_w, img_h)

    # Coin supérieur gauche du crop
    x1 = max(0, cx - side // 2)
    y1 = max(0, cy - side // 2)

    # Ajustements si on dépasse les bords
    if x1 + side > img_w:
        x1 = img_w - side
    if y1 + side > img_h:
        y1 = img_h - side

    x1, y1 = max(0, x1), max(0, y1)

    cropped = img_pil.crop((x1, y1, x1 + side, y1 + side))
    return cropped.resize((SIZE, SIZE), Image.LANCZOS)


def enhance(img):
    img = img.filter(ImageFilter.UnsharpMask(radius=1.2, percent=130, threshold=3))
    img = ImageEnhance.Contrast(img).enhance(1.15)
    img = ImageEnhance.Sharpness(img).enhance(1.2)
    img = ImageEnhance.Color(img).enhance(1.1)
    return img


for fname in ["julien.jpg", "julien_eva.jpg"]:
    src_path = os.path.join(SRC, fname)
    name = os.path.splitext(fname)[0]
    out_path = os.path.join(DST, name + ".png")

    faces, (h, w) = detect_faces(src_path)
    print(f"{fname}: {w}x{h} -> {len(faces)} visage(s) detecte(s)")
    for f in faces:
        print(f"  Visage: x={f[0]}, y={f[1]}, w={f[2]}, h={f[3]}")

    img_pil = Image.open(src_path).convert("RGB")
    result = face_center_crop(img_pil, faces, h, w)

    if result is None:
        print(f"  Aucun visage detecte, recadrage centre par defaut")
        side = min(w, h)
        x1 = (w - side) // 2
        y1 = int(h * 0.05)
        y1 = min(y1, h - side)
        result = img_pil.crop((x1, y1, x1 + side, y1 + side)).resize((SIZE, SIZE), Image.LANCZOS)

    result = enhance(result)
    result.save(out_path, "PNG", optimize=True)
    print(f"  Sauvegarde -> {out_path}")

print("\nTermine.")
