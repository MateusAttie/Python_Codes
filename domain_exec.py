from domain import DataTable

def main():
	"""table_empreendimento = DataTable("Empreendimento")
	col_id = table_empreendimento.add_column('IdEmnpreendimento','bigint')
	col_aditivo = table_empreendimento.add_column('IdAditivo','bigint')
	col_alerta = table_empreendimento.add_column('IdAlerta','bigint')

	table_aditivo = DataTable("Aditivo")
	col_id = table_aditivo.add_column('IdAtivo','bigint')
	col_emp_id = table_empreendimento.add_column('IdEmpreendimento','bigint')
	table_empreendimento.add_references('IdAditivo', table_aditivo, col_aditivo)
	table_aditivo.add_referenced('IdAditivo', table_empreendimento, col_emp_id)
	"""

	table = DataTable("Empreendimento")
	print(Column('IdEmpreendimento', 'bigint'))
	print(PrimaryKey(table, 'IdEmpreendimento', 'bigint'))


	if __name__ == '__main__':
		main()
