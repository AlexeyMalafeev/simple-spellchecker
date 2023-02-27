from src.spellchecker import SkipGrammer


chkr = SkipGrammer(print_steps=True)

print(chkr.check('Ну что ты это каждый челвек должен знать!'), '\n')
print(chkr.check('Мы шли по подъезду и стучались в каждую жверь, ожидая, что нам откроют.'), '\n')
print(chkr.check('Есть такая поговорка: на ловца и жверь бежит.'), '\n')

while sent := input('> '):
    print(chkr.check(sent))
    print()
