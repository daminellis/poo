from exercicio_4_estoque import Eletronicos, Vestuario, Alimento

eletronico = Eletronicos("celular","flip", 10000, "xaiomi")
print(eletronico.__dict__)


vestuario = Vestuario("regata","verao",30,"vidamarinha")
print(vestuario.__dict__)

alimento = Alimento("strogonoff","pronto na hora",25,"acompanha uma maçã")
print(alimento.__dict__)