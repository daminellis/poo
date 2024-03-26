from exercicio_14_rts import Soldado,Tanque,Aeronave,Unidade

soldado1 = Soldado("Soldado1")
tanque1 = Tanque("Tanque1")
aeronave1 = Aeronave("Aeronave1")
inimigo = Unidade("Inimigo")

soldado1.mover("Posição 1")
tanque1.atacar(inimigo)
aeronave1.atacar(inimigo)
inimigo.defender()
