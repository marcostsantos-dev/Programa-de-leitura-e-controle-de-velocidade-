# Programa-de-leitura-e-controle-de-velocidade-

LIMITE_VELOCIDADE = 80
MULTA_POR_KM = 7.00

#Entrada da velocidade do veiculo em float
velocidade = float(input("Digite a velocidade do veiculo: "))

#Analiza se a  velocidade esta dentro do limite estipulado ou se o veiculo deve ser multado.
if velocidade <= 80:
    print(f"\nVocê esta a {velocidade} Km/h ")
    if velocidade == 80:
        print("\nMas tenha atenção o limite MÁXIMO da via é de 80 Km/h, 🚨cuidado!🚨")
#Se o veicúlo exceder a velocidade em até 1,24% emite um alerta
elif velocidade < 81:
    print("\nVOCÊ EXCEDEU O LIMITE DE VELOCIDADE DE 80 Km/h EM ATÉ 1,24%")
    print("\033[33m\n# DESTA VEZ VOCÊ SÓ SERÁ ADVERTIDO #\033[0m")

#Calcula o valor da multa e diz quanto o motorista deve pagar
elif velocidade >= 81:
        excesso_de_velocidade = velocidade - LIMITE_VELOCIDADE
        valor_total_multa = excesso_de_velocidade * MULTA_POR_KM
        print("\033[41m\nVOCÊ FOI MULTADO!!!\033[0m")
        print("O limite de Velocidade é de 80Km/h")
        print(f"Você excedeu a velocidade em + de: {excesso_de_velocidade} Km/h")
        print(f"\nO valor total da multa é: R$ {valor_total_multa:.2f}")
