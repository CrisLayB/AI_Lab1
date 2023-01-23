######################################################################################
_author_ = "Cristian Fernando Laynez Bachez - 201281"
_copyright_ = "Universidad el Valle de Guatemala, Inteligencia Artifical 2023"
_status_ = "Student of Computer Science"

"""
Processing Image
    Tiene metodos que retornan matrices para la deteccion de patrones
    en los laberintos.

Colores conforme a los numeros en cada matriz:
    - ' ': Cuadro libre (Cuadro Blanco)
    - '#': Cuadro ocupado (Cuadro Negro)
    - 'r': Punto de inicio (Cuadro Rojo)
    - 'g': Punto de victorio (Cuadro Verde)
"""
######################################################################################

from PIL import Image

"""

"""
def discretize_image(file_image : str, rescaled_height = 30, rescaled_width = 30):
    img = Image.open(file_image)
    img.thumbnail((rescaled_height, rescaled_width))
    
    width = img.size[0]
    height = img.size[1]

    matrix = []
    for row in range(height):
        support_row = []
        for col in range(width):
            colors = img.getpixel((row, col))
            matrix.append(colors)
        matrix.append(support_row)        
    return

def test_matrix(): # Para probar por si acaso :)
    matrix = [
        ['#','#','#',' ',' ',' ',' ','#','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        ['#','#','#',' ',' ',' ',' ','#','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        ['#','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','#',' ','g',' ',' ',' '],
        ['#','#','#','#','#',' ',' ',' ',' ',' ',' ',' ','#','#','#',' ',' ',' ',' ',' '],
        ['#','#','#','#','#','#',' ',' ',' ',' ',' ',' ','#','#','#',' ',' ','#','#','#'],
        ['#',' ',' ','#','#','#',' ',' ',' ',' ',' ','#','#','#','#',' ',' ','#','#','#'],
        ['#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#','#','#',' ',' ',' ',' ',' '],
        [' ',' ','g',' ','#','#',' ',' ','#','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        ['#','#',' ',' ','#',' ',' ',' ','#','#','#','#',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','#',' ',' ','#','#','#','#',' ',' '],
        ['#','#',' ',' ','#',' ','#','#','#',' ',' ','#',' ','#','#','#','#','#',' ',' '],
        ['#','#',' ',' ',' ',' ','#','#','#',' ',' ',' ',' ','#','#','#','#','#','#',' '],
        ['#','#','#','#','#',' ',' ','#','#',' ',' ',' ',' ','#','#','#','#','#','#','#'],
        [' ',' ','#','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','#','#'],
        [' ',' ','#','#','#','#','#','#','#',' ',' ','#','#',' ',' ',' ','#','#','#','#'],
        [' ',' ','#','#','#','#','#','#','#',' ','#','#','#',' ',' ',' ','#','#','#','#'],
        ['#','#','#',' ',' ','#','#','#','#',' ',' ',' ',' ',' ',' ','r','#','#','#','#'],
        ['#','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','#','#'],
        ['#','#','#',' ',' ',' ',' ',' ',' ','#','#','#','#',' ',' ',' ','#','#','#','#'],
        ['#','#',' ',' ',' ',' ',' ',' ',' ','#','#','#','#',' ',' ',' ','#','#','#','#'],
    ]
    return matrix