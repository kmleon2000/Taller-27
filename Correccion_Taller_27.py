def Input_Format_Info():
  equation = input('Digite la ecuacion: ')
  intervals = [
    input('Digite el valor del primer intervalo: '),
    input('Digite el valor del segundo intervalo: ')
  ]

  intervals = list(
    map(
      lambda x: int(x),
      intervals
    )
  )
  
  intervals.sort()

  formats = [('^', '**'), (' ', ''), ('%', '/')]
  for val, rep in formats:
    if equation.count(val) > 0:
      equation = equation.replace(val, rep)
  
  for num in range(1,10):
    if equation.count(str(num) + 'x') > 0:
      equation = equation.replace(str(num) + 'x', str(num) + '*x')
  
  return [equation, intervals]

def Resolve(equation:str, var:int):
  x = var
  return eval(equation)

def Calc_Area(Action:str):
  if Action.lower() == 'y':
    try:
      data = Input_Format_Info()
      Formula = data[0]
      x1 = data[1][0]
      x2 = data[1][1]
      del data
      # Definimos 10000 rectangulos pro centimetro
      n = (x2 - x1) * 10000
      Ax = (x2 - x1) / n
      h = list()
      # Definimos puntos para calcular las alturas de los rectangulos con la funcion
      for i in range(1, n + 1):
        h.append(
          x1 + (i * Ax) - (Ax / 2)
        )
      # Definimos las alturas empleando la funcion
      h = list(
        map(
          lambda x: Resolve(Formula, x),
          h
        )
      )
      # Calculamos las Areas con la formula base * altura
      a = list(
        map(
          lambda x: Ax * x,
          h
        )
      )
      # Imprimimos la suma de las Areas
      print(
        'Respuesta: ' + str(round(sum(a),4)) + ' U^2'
      )
      return Calc_Area(
        input('Deseas hacer otro Calculo? : Si[Y] No[N] ')
      )
    except:
      print('Ups!! Ocurrió un error')
      return Calc_Area(
        input('Deseas intertar un calculo de nuevo? : Si[Y] No[N] ')
      )
  elif Action.lower() == 'n':
    print('Bye-Bye!!')
  else:
    print('Error: La opcion digitada no existe')
    return Calc_Area(
      input('Deseas intentarlo de nuevo? : Si[Y] No[N] ')
    )

print('Calculadora de Area bajo la curva\n')
Calc_Area('y')