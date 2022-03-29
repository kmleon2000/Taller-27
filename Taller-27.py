import sympy as sp

def SolicitarDatos():
  ec = input('Digite la ecuacion: ')
  ec = ec.replace('^','**')
  ec = ec.replace(' ','')

  for num in range(1,10):
    if ec.count(str(num) + 'x'):
      ec = ec.replace(str(num) + 'x', str(num) + '*x')
  
  start_n = input('Digite el numero del inico del intervalo: ')
  end_n = input('Digite el numero del fin del intervalo: ')

  return (ec, (start_n, end_n))

def AreaBajoCurva(resolve:str):
  if resolve.lower() == 'y':
    data = SolicitarDatos()
    x = sp.Symbol('x')
    y = eval(data[0])
    res = sp.integrate(y,(x,data[1][0],data[1][1]))
    print(
      'El área bajo la curva es: ' +
      str(
        round(
          abs(
            eval(
              str(res)
            )
          ), 3
        )
      ) + 
      ' u^2'
    )
    return AreaBajoCurva(
      input('Desea realizar un nuevo calculo? Si[Y] No[N]: ')
    )
  if resolve.lower() == 'n':
    print('Bye-Bye...')
  else:
    print('Error: la opcion no exite')
    return AreaBajoCurva(
      input('Desea realizar un nuevo calculo? Si[Y] No[N]: ')
    )

print('Calculadora de area bajo la curva\n')
AreaBajoCurva('Y')