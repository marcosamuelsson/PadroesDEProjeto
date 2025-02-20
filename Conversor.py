from abc import ABC, abstractmethod

# 1. Criando a interface de conversores (AbstractProduct)
class Conversor(ABC):
    @abstractmethod
    def converter(self, numero: int) -> str:
        pass

# 2. Implementando o conversor de decimal para binário (ConcreteProduct)
class ConversorDecimalBinario(Conversor):
    def converter(self, numero: int) -> str:
        return bin(numero)[2:]

# 3. Implementando a Abstract Factory
class ConversorFactory(ABC):
    @abstractmethod
    def criar_conversor(self) -> Conversor:
        pass

# 4. Fábrica concreta que cria o conversor de decimal para binário (ConcreteFactory)
class ConversorDecimalBinarioFactory(ConversorFactory):
    def criar_conversor(self) -> Conversor:
        return ConversorDecimalBinario()

# 5. Cliente
def cliente(fabrica: ConversorFactory, numero: int) -> str:
    conversor = fabrica.criar_conversor()
    return conversor.converter(numero)

# Usando a Abstract Factory
numero_decimal = 189
fabrica_binario = ConversorDecimalBinarioFactory()
resultado_binario = cliente(fabrica_binario, numero_decimal)

print(f"O número decimal {numero_decimal} em binário é: {resultado_binario}")