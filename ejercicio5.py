#In many jurisdictions a small deposit is added to drink containers to encourage peopleto recycle them. In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit. Write a program that reads the number of containers of each size from the user. Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar sign and always displays exactly two decimal places.


chico = float(input('Cuantos envases de 1 litro o menos tienes?'))
grande= float(input('Cuantos envases de mas de 1 litro tienes?'))


print('Tu reembolso total es de $', 0.10 * chiico + 0.25 * grande)