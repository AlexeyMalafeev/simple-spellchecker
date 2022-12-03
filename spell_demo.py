from src.spellchecker import SimpleSpellchecker


chkr = SimpleSpellchecker()
print(f"{chkr.freqs1['человек'] = }")
print(f"{chkr.freqs2[('молодой', 'человек')] = }")
print(f"{chkr.freqs2[('говорил', 'что')] = }")
print(f"{chkr.freqs3[('на', 'самом', 'деле')] = }")
print(f"{chkr.freqs3[('для', 'того', 'чтобы')] = }")
