from pydantic import validate_call

def pipeline(numero:int):
        numero_2 = extract(numero)
        numero_3 = transform(numero_2)
        numero_4 = transform(numero_3)
        return numero_4

def extract(numero:int) -> int:
        return numero+1

def transform(numero:int) -> int:
        return numero+1

def load(numero:int) -> int:
        return numero+1

# print(pipeline(55))

@validate_call
def filtrar_acima_de(lst: list[float], salario_max) -> float:
        lst_1 : list = []

        for item in lst:
                if item > salario_max:
                        lst_1.append(item)

        return lst_1

print('__name__: \n',__name__)


if __name__ == "__main__":
        lista_salarios = [3000, 4000, 150000]
        sal_max = 100000

        print(filtrar_acima_de(lst=lista_salarios, salario_max=sal_max))