# целевой класс, с которым будет работать код основной программы (main_code)
class Target:

    def request(self):
        return "Класс Target: здесь всё хорошо"


# неправильно заданный / сформированный / находящийся в доработке код (класс)
# не может быть напрямую использован через (main_code) в виду своих недостатков
# требует доработки / исправления от Adapter'а
class Adaptee:

    def specific_request(self):
        return "@#(*jg9jkS()Dfk90530yhfsdf)(kmКласс Target: здесь всё хорошо#($NG9m()F*DM()WE()DF#@$)(YK"


# благодаря множественному наследованию обоих классов мы можем "адаптировать" Adaptee к Target
class Adapter(Target, Adaptee):

    def request(self):
        adaptee_temp = self.specific_request()
        return f"Адаптер: (после адаптирования) {adaptee_temp[adaptee_temp.find('К'):adaptee_temp.rfind('о') + 1]}"


def main_code(target: "Target"):
    print(target.request())


if __name__ == "__main__":

    target = Target()
    adaptee = Adaptee()
    adapter = Adapter()

    main_code(target)
    print(f"Адаптируемый класс: {adaptee.specific_request()}")
    main_code(adapter)
