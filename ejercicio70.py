mensaje = input('Inserta tu mensaje:')
valor = int(input('Ingrese el valor de cambio'))

nuevomensaje = " "

for ch in mensaje:
    if ch >= "a" and ch <= "z":
        pos = ord(ch) - ord("a")
        pos = (pos + valor) % 26
        nuevo  = chr(pos + ord ("a"))
        nuevomensaje = nuevomensaje + nuevo
    elif ch >= "A" and ch <= "Z":
        pos = ord(ch) - ord("A")
        pos = (pos + valor) % 26
        nuevo  = chr(pos + ord ("A"))
        nuevomensaje = nuevomensaje + nuevo
else:
    nuevomensaje = nuevomensaje + ch
print("El mensaje cambiado es:", nuevomensaje)