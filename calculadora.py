import ast
import operator
import sys
import os

# Operadores matemáticos permitidos
OPERADORES = {
    ast.Add: operator.add,  # Suma (+)
    ast.Sub: operator.sub,  # Resta (-)
    ast.Mult: operator.mul,  # Multiplicación (*)
    ast.Div: operator.truediv,  # División (/)
    ast.FloorDiv: operator.floordiv,  # División entera (//)
    ast.Mod: operator.mod,  # Módulo (%)
    ast.Pow: operator.pow,  # Potencia (**)
    ast.USub: operator.neg,  # Negativo (-x)
    ast.UAdd: operator.pos,  # Positivo (+x)
}


def evaluar_nodo(nodo):
  if isinstance(nodo, ast.Constant) and isinstance(nodo.value, (int, float)):
    return nodo.value
  elif isinstance(nodo, ast.BinOp):
    izquierda = evaluar_nodo(nodo.left)
    derecha = evaluar_nodo(nodo.right)
    operador = OPERADORES.get(type(nodo.op))
    if operador:
      return operador(izquierda, derecha)
  elif isinstance(nodo, ast.UnaryOp):
    operando = evaluar_nodo(nodo.operand)
    operador = OPERADORES.get(type(nodo.op))
    if operador:
      return operador(operando)

  raise ValueError("Operación o símbolo no permitido")


def calcular(expresion):
  # Reemplazar '^' por '**' por comodidad si el usuario usa '^' para potencias
  expresion = expresion.replace("^", "**")
  arbol = ast.parse(expresion, mode="eval")
  return evaluar_nodo(arbol.body)


def main():
  # sys.argv[0] es el nombre del script, los argumentos empiezan en el índice 1
  operaciones = sys.argv[1:]
  mi_calculo = os.getenv("MI_CALCULO")
  if mi_calculo is not None:
      operaciones.append(mi_calculo)

  if not operaciones:
    print('Uso: python calculadora.py "<operacion1>" "<operacion2>" ...')
    print('Ejemplo: python calculadora.py "2 + 2" "10 * 5" "(4 + 6) / 2"')
    sys.exit(1)

  for op in operaciones:
    try:
      resultado = calcular(op)
      print(f"{op} = {resultado}")
    except ZeroDivisionError:
      print(f"{op} = Error (División por cero)")
    except Exception:
      print(f"{op} = Error (Expresión inválida)")


if __name__ == "__main__":
  main()
