from polyglot.ext.json import JsonStore


def test_fucntion():
    pass


store = JsonStore(__file__, "testing_json_storage")

store.add(95)

print(store.filter_by_value(95))
