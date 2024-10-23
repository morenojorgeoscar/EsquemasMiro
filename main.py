import cv2
import numpy as np

def crear_esquema_digital(imagen_path):
    # Cargar la imagen original
    image = cv2.imread(imagen_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar un desenfoque para reducir ruido
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detección de bordes
    edges = cv2.Canny(blurred, 50, 150)

    # Encontrar contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Crear una imagen blanca para el resultado
    output_image = np.ones_like(image) * 255  # Imagen blanca

    for contour in contours:
        # Aproximar el contorno a una forma simple
        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Dibujar la forma aproximada en la imagen de salida
        if len(approx) == 3:
            # Triángulo
            cv2.polylines(output_image, [approx], isClosed=True, color=(0, 255, 0), thickness=2)
        elif len(approx) == 4:
            # Cuadrado o rectángulo
            cv2.polylines(output_image, [approx], isClosed=True, color=(0, 0, 255), thickness=2)
        elif len(approx) > 4:
            # Polígono
            cv2.polylines(output_image, [approx], isClosed=True, color=(255, 0, 0), thickness=2)

    # Guardar el resultado en un archivo
    cv2.imwrite('./img/resultado.png', output_image)

# Reemplaza 'ruta/a/tu/imagen.png' con la ruta de tu imagen
crear_esquema_digital('./img/esquema.jpg')
