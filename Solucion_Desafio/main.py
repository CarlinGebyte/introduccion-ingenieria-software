def calculate_average():
  grades = input("Ingrese las calificaciones separadas por espacios: ").split()
  if not grades:
      print("No se ingresaron calificaciones.")
      return None
  elif any(not grade.replace('.', '', 1).isdigit() for grade in grades):
      print("Entrada inválida. Ingrese solo calificaciones numéricas.")
      return None
  elif len(grades) < 5 or len(grades) > 5:
      print("Ingrese exactamente cinco calificaciones para calcular un promedio.")
      return None

  grades = [float(grade) for grade in grades]
  avg = sum(grades) / len(grades)

  if avg >= 60:
      print('Aprobado')
  elif avg >= 40 and avg <= 59:
      print('En recuperación')
  else:
      print('Reprobado')

calculate_average()