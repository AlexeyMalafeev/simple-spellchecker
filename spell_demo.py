from src.spellchecker import SimpleSpellchecker


chkr = SimpleSpellchecker()
# print(f"{chkr.freqs1['человек'] = }")
# print(f"{chkr.freqs2[('молодой', 'человек')] = }")
# print(f"{chkr.freqs2[('говорил', 'что')] = }")
# print(f"{chkr.freqs3[('на', 'самом', 'деле')] = }")
# print(f"{chkr.freqs3[('для', 'того', 'чтобы')] = }")

print(chkr.check('Ну что ты это каждый челвек должен знать!'))
print(chkr.check('Мы шли по подъезду и стучались в каждую жверь, ожидая, что нам откроют.'))
print(chkr.check('Есть такая поговорка: на ловца и жверь бежит.'))
