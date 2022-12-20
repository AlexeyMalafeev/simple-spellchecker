from src.spellchecker import SimpleSpellchecker


chkr = SimpleSpellchecker(print_steps=True)

print(chkr.check('Ну что ты это каждый челвек должен знать!'))
print(chkr.check('Мы шли по подъезду и стучались в каждую жверь, ожидая, что нам откроют.'))
print(chkr.check('Есть такая поговорка: на ловца и жверь бежит.'))
