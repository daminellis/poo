from exercicio_13_cinema import Ingresso,IngressoVIP,Ingresso3D

ingresso_normal = Ingresso(20)
ingresso_vip = IngressoVIP(20, 10)
ingresso_3d = Ingresso3D(20, 5)

print("Preço do ingresso normal:", ingresso_normal.calcular_preco())
print("Preço do ingresso VIP:", ingresso_vip.calcular_preco())
print("Preço do ingresso 3D:", ingresso_3d.calcular_preco())

print("Disponibilidade do ingresso normal:", ingresso_normal.verificar_disponibilidade())
print("Disponibilidade do ingresso VIP:", ingresso_vip.verificar_disponibilidade())
print("Disponibilidade do ingresso 3D:", ingresso_3d.verificar_disponibilidade())

print("Reserva do ingresso normal:", ingresso_normal.reservar())
print("Reserva do ingresso VIP:", ingresso_vip.reservar())
print("Reserva do ingresso 3D:", ingresso_3d.reservar())

print("Disponibilidade do ingresso normal após reserva:", ingresso_normal.verificar_disponibilidade())
print("Disponibilidade do ingresso VIP após reserva:", ingresso_vip.verificar_disponibilidade())
print("Disponibilidade do ingresso 3D após reserva:", ingresso_3d.verificar_disponibilidade())
