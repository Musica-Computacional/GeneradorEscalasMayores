### Programa que devuelve las 


import os
from os.path import basename
import sys
sys.path.append(".")


class Escalas():

    def __init__(self) -> None:
        self.circulo_quintas_mayores = ['C' ,'G' ,'D' ,'A'  ,'E'  ,'B'  ,'Gb' ,'Db' ,'Ab','Eb','Bb','F']
        self.circulo_quintas_menores = ['Am','Em','Bm','F#m','C#m','G#m','Ebm','Bbm','Fm','Cm','Gm','Dm']
        
        self.formulaEscalaMayor = [2,2,1,2,2,2,1]
        self.escalaCromatica = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B',  'C','C#','D','D#','E','F','F#']

        self.sharpsNflats = {
            'C#' :'Db',
            'C#m':'Dbm',
            'D#' :'Eb',
            'D#m':'Ebm',
            'F#' :'Gb',
            'F#m':'Gbm',
            'G#' :'Ab',
            'G#m':'Abm',
            'A#' :'Bb',
            'A#m':'Bbm',
        }

        self.romanNumbers = {
            1:'I   ',
            2:'II  ',
            3:'III ',
            4:'IV  ',
            5:'V   ',
            6:'VI  ',
            7:'VII°',
        }

    def get_sharp_from_flat(self,val):
        for key, value in self.sharpsNflats.items():
            if val == value:
                return key
        return "El acorde # no existe"

    def escaleFromNote(self,note,chords_too=False):
        scaleName = '__________________Escala de ' + note + '_________________'
        sharp = False
        if '#' in note:
            note = self.sharpsNflats.get(note)
            sharp = True

        if note in self.circulo_quintas_mayores:
            index = self.circulo_quintas_mayores.index(note)
            scale = [note]
            if note == 'C':
                scale.append(self.circulo_quintas_menores[len(self.circulo_quintas_menores)-1])
                scale.append(self.circulo_quintas_menores[index+1])
                scale.append(self.circulo_quintas_mayores[len(self.circulo_quintas_menores)-1])
                scale.append(self.circulo_quintas_mayores[index+1])
                scale.append(self.circulo_quintas_menores[index])
                scale.append(self.circulo_quintas_menores[index+2])
            elif note == 'F':
                scale.append(self.circulo_quintas_menores[index-1])
                scale.append(self.circulo_quintas_menores[0])
                scale.append(self.circulo_quintas_mayores[index-1])
                scale.append(self.circulo_quintas_mayores[0])
                scale.append(self.circulo_quintas_menores[index])
                scale.append(self.circulo_quintas_menores[1])
            elif note == 'Bb':
                scale.append(self.circulo_quintas_menores[index-1])
                scale.append(self.circulo_quintas_menores[index+1])
                scale.append(self.circulo_quintas_mayores[index-1])
                scale.append(self.circulo_quintas_menores[index])
                scale.append(self.circulo_quintas_mayores[index+1])
                scale.append(self.circulo_quintas_menores[0])
            else:                
                scale.append(self.circulo_quintas_menores[index-1])
                scale.append(self.circulo_quintas_menores[index+1])
                scale.append(self.circulo_quintas_mayores[index-1])
                scale.append(self.circulo_quintas_mayores[index+1])
                scale.append(self.circulo_quintas_menores[index])
                scale.append(self.circulo_quintas_menores[index+2])

            
            print()
            print(scaleName)
            print('-----------------------------------------------')
            if sharp:
                arranged_scale = []
                for chord in scale:
                    if('b' in chord):
                        arranged_scale.append(self.get_sharp_from_flat(chord))
                    else:
                        arranged_scale.append(chord)
                
                #last_chord = arranged_scale.pop(len(arranged_scale)-1)
                #last_diminish_chord = last_chord +'(dim)'
                #arranged_scale.append(last_diminish_chord)
                for c in range(0,len(arranged_scale)):
                    if chords_too:
                        print(self.romanNumbers.get(c+1) + ': ' + arranged_scale[c] + ' - ' + str(self.notesFromChord(arranged_scale[c])))
                    else:
                        print(self.romanNumbers.get(c+1) + ': ' + arranged_scale[c] )
                #return arranged_scale
            else: #aca es bemol
                arranged_scale = []
                for chord in scale:
                    if('#' in chord):
                        arranged_scale.append(self.sharpsNflats.get(chord))
                    else:
                        arranged_scale.append(chord)
                #last_chord = scale.pop(len(scale)-1)
                #last_diminish_chord = last_chord +'(dim)'
                #scale.append(last_diminish_chord)
                for c in range(0,len(arranged_scale)):
                    if chords_too:
                        print(self.romanNumbers.get(c+1) + ': ' + arranged_scale[c] + ' - ' + str(self.notesFromChord(arranged_scale[c],True)))
                    else:
                        print(self.romanNumbers.get(c+1) + ': ' + arranged_scale[c] )
                #return scale
            print('_______________________________________________')
            print('-----------------------------------------------')
            print()
        else:   
            print('No se puede generar una escala MAYOR a paritr de esa nota!')
            return None

    def notesFromChord(self,chord,flat_scale=False):
        # Eliminamos indicador de acorde menor, solo necesitamos el nombre, ya que la formula de la escala mayor
        # nos ayudara a construir cada acorde mayor o menor perteneciente a la escala en cuestion.

        minor = False
        flat = False
        if 'm' in chord and 'b' in chord:
            chord = chord.replace('m','') 
            chord = self.get_sharp_from_flat(chord)
            minor = True
            flat = True
        elif 'b' in chord:
            chord = self.get_sharp_from_flat(chord)
            flat = True
        elif 'm' in chord:
            chord = chord.replace('m','') 
            minor = True

        if flat_scale == True:
            flat = True

        if chord in self.escalaCromatica:
            index = self.escalaCromatica.index(chord)
            chord_notes = []

            if minor:
                first_note = 1 + index
                third_note = 4 + index
                fifth_note = 8 + index
                chord_notes.append(self.escalaCromatica[first_note-1]) #-1 por corrimiento en array
                chord_notes.append(self.escalaCromatica[third_note-1])
                chord_notes.append(self.escalaCromatica[fifth_note-1])
            else:
                first_note = 1 + index
                third_note = 5 + index
                fifth_note = 8 + index
                chord_notes.append(self.escalaCromatica[first_note-1])
                chord_notes.append(self.escalaCromatica[third_note-1])
                chord_notes.append(self.escalaCromatica[fifth_note-1])

            if flat:
                arranged_chord_notes = []
                for chord in chord_notes:
                    if '#' in chord:
                        arranged_chord_notes.append(self.sharpsNflats.get(chord))
                    else:
                        arranged_chord_notes.append(chord)
                return arranged_chord_notes
            else:
                return chord_notes
        else:
            print('La nota ingresada no existe! No se puede generar el acorde de triada.')
            return None
    

def welcome():
    #os.system('cls')
    print("¡¡Bienvenido al generador de escalas MAYORES!!")
    print("Para generar tu escala MAYOR debes ingresar el nombre de una nota cualquiera en notación americana (C,D,E,F,G,A,B). ")
    print("Puedes agregar bemoles y sostenidos siguiendo el patron de generacion de escalas mayores dictado por el circulo de quintas. ")
    print()
    print()
    print("Ante las dudas... prueba, prueba y prueba! ...¡COMENZEMOS!")
    print()
    print()

def menu():
    #os.system('cls')
    print("Seleccione una opción. (Sostenidos = '#', Bemoles = 'b')")
    print("\t1. Generar escala mayor a partir de nota base")
    print("\t2. Mostrar triada a partir de especificació acorde")
    print("\t3. Generar escala y acordes a partir de nota base ")
    print("\t4. Adios musical")


def main():
    obj = Escalas()

    welcome()
    while True:

        menu()
        option = input('Ingrese una opcion: ')

        if(option == '1'):
            note_name = input('Ingrese el nombre de la nota para obtener una escala: ')
            obj.escaleFromNote(note_name)

        elif(option == '2'):
            chord_name = input('Ingrese el acorde para obtener sus primeras tres notas: ')
            chord = obj.notesFromChord(chord_name)
            print(chord)

        elif(option == '3'):
            note_name = input('Ingrese el nombre de la nota para obtener una escala y sus acordes: ')
            obj.escaleFromNote(note_name,True)

        elif(option == '4'):

            print('Adios')
            break


if __name__ == "__main__":
    main()



