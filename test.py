from polyglot.ext.json import JsonStore

def test_fucntion():
	pass

store = JsonStore(__file__, "testing_json_storage")
print(store.keys)

store.add(9)

print(store.get())
