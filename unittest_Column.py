import decimal
import unittest

class Column:
	"""Representa uma coluna em uma DataTable

		Essa classe contém as informações de uma colunae deve validar um dado de acordo com o tipo de dado configurado no construtor.

		Attibutes:
			name: Nome da coluna
			kind: Tipo do Dado(varchar, bigint, int etc...)
			description: Descrição da coluna

	"""
	def __init__(self, name, kind, description=""):
		"""Construtor

			Args:
				name: Nome da Coluna
				kind: Tipo do Dado(varchar, bigint, int etc...)
				description: Descrição da coluna

		"""
		self._name = name
		self._kind = kind
		self._description = description

	def __str__(self):
		_str = "Col: {} : {} {}".format(self._name, self._kind, self._description)
		return _str

	@staticmethod
	def validate(kind, data):
		if kind == 'bigint':
			if isinstance(data, int):
				return True
			return False
		elif kind == 'varchar':
			if isinstance(data, str):
				return True
			return False
		elif kind == 'numeric':
			try:
				val = decimal.Decimal(data)
			except:
				return False
			return True

class Columntest(unittest.TestCase):
	def test_validate_bigint(self):
		self.assertTrue(Column.validate('bigint', 100))
		self.assertTrue(not Column.validate('bigint', 10.1))
		self.assertTrue(not Column.validate('bigint', 'Texto'))

	def test_validate_numeric(self):
		self.assertTrue(Column.validate('numeric', 10.1))
		self.assertTrue(Column.validate('numeric', 100))
		self.assertTrue(not Column.validate('numeric', 'Texto'))

	def test_validate_varchar(self):
		self.assertTrue(Column.validate('varchar', 'Texto'))
		self.assertTrue(not Column.validate('varchar', 100))
		self.assertTrue(not Column.validate('varchar', 10.1))



if __name__ == "__main__":
	unittest.main()
