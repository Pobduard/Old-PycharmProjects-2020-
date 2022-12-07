# ############################# [Doc-Strings]
class doc_string:
    def docstring(self: str):
        """Prueba del docstring wero, no hace na e na.

        De verdad, nada -.-"""
        pass

    # print(docstring.__doc__)
    # docstring()


# ############################# [Annotations]
class anno_tation:
    def annotation(self: None, valor: int, otro: str) -> str:
        """
        :param self: None
        :param valor: int
        :param otro: str
        """
        # print("Anotaciones:", annotation.__annotations__)
        int(valor + valor)
        return str(valor) + 'ola' + str(otro)


# annotation(3, "hello")
# print(annotation.__doc__)
# annotation(3, "")
# print("inicio we")
# print("no c we" + annotation(3, "nope"))
# print("final we")

# ############################### [Simple Prueba]
class Pru:
    def prueba(number: int, sum_number: int) -> int:
        """
        La suma de lo que se de + 3

        :return: int +3
        """
        print(number + sum_number)
        number += sum_number
        return number
