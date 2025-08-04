from copyconst.colour import Colour
import copy

red=Colour("red")
pink=Colour("pink")


palette=[red,pink]          #list banai
warmtones=palette.copy()    #dosri list banai by copying contents of first list

palette[0].name="scarlet"   #changes made in palette

print(warmtones[0].name)    #warmtones also effected #cuz INDIRECT ALIASING (do alag list mein same object reference hona)
#since the dono list ke index [0] per same object tha isliyen both lists were effected when changes were made object

#DEEP COPY
deep=copy.deepcopy(palette)   

deep[0].name="neon"


print(deep[0].name)
print(palette[0].name)

