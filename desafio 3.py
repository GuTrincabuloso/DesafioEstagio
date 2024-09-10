
faturamento = [200.0, 450.0, 0.0, 150.0, 0.0, 700.0, 0.0, 130.0, 850.0, 90.0]  # Exemplo de dados


valores = [valor for valor in faturamento if valor > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Dias acima da média: {dias_acima_da_media}")
