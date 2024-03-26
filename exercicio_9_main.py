from exercicio_9_trafego import Carro, Onibus, Bicicleta

if __name__ == "__main__":
    car = Carro()
    onib = Onibus()
    bic = Bicicleta()

    origin = 'A'
    destination = 'D'

    car_rota = car.calc_rot(origin, destination)
    car_temp_viagem = car.calc_temp(car_rota)
    print(f"Carro: Rota: {car_rota}, Tempo de viagem: {car_temp_viagem} unidades de tempo")

    onib_rota = onib.calc_rot(origin, destination)
    onib_temp_viagem = onib.calc_temp(onib_rota)
    print(f"Ônibus: Rota: {onib_rota}, Tempo de viagem: {onib_temp_viagem} unidades de tempo")

    bic_rota = bic.calc_rot(origin, destination)
    bic_temp_viagem = bic.calc_temp(bic_rota)
    print(f"Bicicleta: Rota: {bic_rota}, Tempo de viagem: {bic_temp_viagem} unidades de tempo")
