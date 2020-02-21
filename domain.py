class Relationship:
	"""Classe que representa um relacionamento entre DataTables

	Essa classe tem todas as informações que identificam um relacionamento entre tabelas.
	Em qual coluna ele existe, de onde vem e para onde vai.
	"""
	def __init__(self,name,_from,to,on):
		"""Construtor

			Args:
				name: Nome
				from: Tabela de onde sai
				to: Tabela para onde vai
				on: Instância de coluna onde existe

		"""

		self._name = name
		self._from = _from
		self._to = to
		self._on = on

class DataTable:
	"""Representa uma tabela de dados.

		Essa classe representa uma tabela de dados do portal
		da transparência. Deve ser capaz de validar linhas inseridas de acordo com as colunas que possui.
		As linhas inseridas ficam registradas dentro dela.

		Attributes:
			name: Nome da tabela
			columns: [Lista de colunas]
			data: [Lista de dados]

	"""
	def __init__(self,name):
		"""Construtor

			Args:
				name: Nome da tabela

		"""
		self._name = name
		self._columns = []
		self._data = []
		self._references =[]
		self._referenced = []


	def add_column(self, name, kind, description):
		column = Column(name, kind, description)
		self._columns.append(column)
		return column


	def add_references(self, name, to, on):
		"""Cria uma referência dessa tabela para uma outra tabela

		Args:
			name: nome da relação
			to: instância da tabela apontada
			on: instância da coluna em que existe a relação

		"""
		relationship = Relationship(name, self, to, on)
		self._references.append(relationship)

	def add_referenced(self, name, by, on):
		"""Cria uma referência para outra tabela que aponta para essa.

			Args:
				name: noemda relação
				by: instância da tabela que aponta para essa
				on: instância da coluna em que existe a relação

		"""
		relationship = Relationship(name, by, self, on)
		self._referenced.append(relationship)

class Column:
	"""Representa uma coluna em uma DataTable

		Essa classe contém as informações de uma colunae deve validar um dado de acordo com o tipo de dado configurado no construtor.

		Attibutes:
			name: Nome da coluna
			kind: Tipo do Dado(varchar, bigint, int etc...)
			description: Descrição da coluna

	"""
	def __init__(self, name, kind, description):
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


class PrimaryKey(Column):

	def __init__(self, table, name, kind, description=None):
		super().__init__(name, kind, description=description)
		self._is_pk = True

	def __str__(self):
		_str = "Col: {} : {} {}".format(self._name, self._kind, self._description)

		return "{} - {}".format('PK', _str)
