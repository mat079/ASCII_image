import numpy as np
import cv2

#Standard ascii levels
ascii_levels = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^'. "
#10 ascii levels
ascii_10levels = "@%#*+=-:. "

#Transformation d'un niveau de gris en caractère
def greyToASCII(asciiLevels, greyValue):
    num_chars = len(asciiLevels)
    temp = asciiLevels[min(int((255-greyValue)*(num_chars/255)), num_chars - 1)]
    return(temp)

#Parcours de l'image pour transformer les niveaux de gris en caractères
def toASCII(img, rows = 80, cols = 180):
    #redimenssionnement
    height, width = img.shape
    cell_width = width / cols
    cell_height = height / rows

    #parcours
    result = ""
    for i in range(rows):
        for j in range(cols):
            gray = np.mean(
            img[int(i * cell_height):min(int((i + 1) * cell_height), height), int(j * cell_width):min(int((j + 1) * cell_width), width)]
            )
            result += greyToASCII(ascii_10levels,gray)
        result += '\n'
    return result

def main():
    #demande à l'utilisateur le nom de l'image à transformer
    print("\nChoississez l'image à transformer, NE PAS OUBLIER L'EXTENSION (Exemple : tiger.jpg)")
    src =input()
    print("\nChoississez le nom du fichier où sauvegarder l'image ASCCI \nNE PAS OUBLIER L'EXTENSION (Exemple : fichier.txt)")
    dest =input()
    #Lecture de l'image
    img = cv2.imread(src,0)
    height, width = img.shape

    #Transformation en ASCII
    AsciiImg = toASCII(img)

    #Sauvegarde dans un fichier
    with open(dest, "w") as fichier:
	    fichier.write(AsciiImg)
    print("Image ASCII sauvegardée dans " +dest)



if __name__ == '__main__':
    main()
