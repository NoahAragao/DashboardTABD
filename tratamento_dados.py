import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)


df_alunos = pd.read_csv('C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_alunos.csv')
df_disciplinas = pd.read_csv('C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_curso_disciplina.csv')
df_professores = pd.read_csv('C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_professor_disciplina.csv')

# print("Alunos:")
# print(df_alunos.head())
# print("\nDisciplinas:")
# print(df_disciplinas.head())
# print("\nProfessores:")
# print(df_professores.head())

csv_path = 'C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_alunos.csv'
csv_path2 = 'C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_professor_disciplina.csv'
csv_path3 = 'C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_curso_disciplina.csv'

# # Carregar o arquivo CSV
# df_alunos = pd.read_csv(csv_path)

# # Verificar se a coluna 'valor_desconto' existe
# if 'valor_desconto' in df_alunos.columns:
#     # Dividir os valores por 10 e arredondar para 1 casa decimal
#     df_alunos['valor_desconto'] = (df_alunos['valor_desconto'] / 10).round(1)
#     print("Coluna 'valor_desconto' modificada:")
#     print(df_alunos['valor_desconto'].head())
# else:
#     print("A coluna 'valor_desconto' não foi encontrada no DataFrame.")

# # Sobrescrever o arquivo original com os dados atualizados
# df_alunos.to_csv(csv_path, index=False)
# print(f"Arquivo CSV original atualizado em: {csv_path}")

# if 'email' in df_alunos.columns:
#     df_alunos = df_alunos.drop(columns=['email'])
#     print("A coluna 'email' foi removida.")
# else:
#     print("A coluna 'email' não foi encontrada no DataFrame.")

# # Sobrescrever o arquivo original com os dados atualizados
# df_alunos.to_csv(csv_path, index=False)
# print(f"Arquivo CSV original atualizado sem a coluna 'email' em: {csv_path}")

# if 'email_professor' in df_professores.columns:
#     df_professores = df_professores.drop(columns=['email_professor'])
#     print("A coluna 'email' foi removida.")
# else:
#     print("A coluna 'email' não foi encontrada no DataFrame.")

# Substituir os valores da coluna 'status'
# if 'status' in df_alunos.columns:
#     df_alunos['status'] = df_alunos['status'].replace({'I': 'Inativo', 'A': 'Matriculado'})
#     print("Os valores da coluna 'status' foram atualizados.")
# else:
#     print("A coluna 'status' não foi encontrada no DataFrame.")

# # Sobrescrever o arquivo original com os dados atualizados
# df_alunos.to_csv(csv_path, index=False)
# print(f"Arquivo CSV original atualizado com os valores da coluna 'status' alterados em: {csv_path}")

# Carregar o arquivo CSV
# df_alunos = pd.read_csv(csv_path)

# # Remover prefixos como Sr, Srta, Sra, Dr, Dra no início da coluna de nomes
# if 'nome_aluno' in df_alunos.columns:
#     df_alunos['nome_aluno'] = df_alunos['nome_aluno'].str.replace(r'^(Sr.\.?|Srta.|Sra.|Dr.\.?|Dra.)\s+', '', regex=True)
#     print("Prefixos removidos dos nomes.")
# else:
#     print("A coluna 'nome' não foi encontrada no DataFrame.")

# # Sobrescrever o arquivo original com os dados atualizados
# df_alunos.to_csv(csv_path, index=False)
# print(f"Arquivo CSV original atualizado com os nomes sem prefixos salvo em: {csv_path}")

# # Função para remover duplicatas de alunos com status "Matriculado"
# def remover_duplicados_matriculados(df, coluna_nome='nome_aluno', coluna_status='status'):
#     # Filtrar os alunos com status "Matriculado"
#     df_matriculados = df[df[coluna_status] == 'Matriculado']

#     # Identificar duplicatas por nome e status "Matriculado"
#     duplicatas = df_matriculados.duplicated(subset=coluna_nome, keep='first')

#     # Remover as duplicatas do DataFrame original
#     df_sem_duplicatas = df[~((df[coluna_status] == 'Matriculado') & duplicatas)]

#     return df_sem_duplicatas

# # Remover duplicatas
# df_alunos_limpo = remover_duplicados_matriculados(df_alunos)

# # Salvar o DataFrame atualizado no arquivo CSV
# df_alunos_limpo.to_csv(csv_path, index=False)

# print("Duplicatas removidas e arquivo atualizado com sucesso!")

# def encontrar_duplicados_com_status_matriculado(df, coluna_nome='nome_aluno', coluna_status='status'):
#     # Filtrar os alunos com status "matriculado"
#     matriculados = df[df[coluna_status] == 'Matriculado']
    
#     # Encontrar os alunos duplicados
#     duplicados = matriculados[coluna_nome].value_counts()

#     # Filtrar os alunos que têm mais de 1 status "matriculado"
#     alunos_duplicados = duplicados[duplicados > 1]
    
#     return alunos_duplicados

# # Encontrar os alunos com mais de 1 status "matriculado"
# duplicados = encontrar_duplicados_com_status_matriculado(df_alunos)

# # Exibir os duplicados no terminal
# if not duplicados.empty:
#     print("Alunos com mais de 1 status 'Matriculado':")
#     print(duplicados)
# else:
#     print("Não há alunos com mais de 1 status 'matriculado'.")

# # Sobrescrever o arquivo original com os dados atualizados
# df_professores.to_csv(csv_path2, index=False)
# print(f"Arquivo CSV original atualizado sem a coluna 'email' em: {csv_path2}")

# if 'endereco' in df_professores.columns:
#     df_professores = df_professores.drop(columns=['endereco'])
#     print("A coluna 'endereco' foi removida.")
# else:
#     print("A coluna 'endereco' não foi encontrada no DataFrame.")

# # Sobrescrever o arquivo original com os dados atualizados
# df_professores.to_csv(csv_path2, index=False)
# print(f"Arquivo CSV original atualizado sem a coluna 'endereco' em: {csv_path2}")

# if 'telefone' in df_professores.columns:
#     df_professores = df_professores.drop(columns=['telefone'])
#     print("A coluna 'telefone' foi removida.")
# else:
#     print("A coluna 'telefone' não foi encontrada no DataFrame.")

# # Sobrescrever o arquivo original com os dados atualizados
# df_professores.to_csv(csv_path2, index=False)
# print(f"Arquivo CSV original atualizado sem a coluna 'telefone' em: {csv_path2}")

# # Carregar o arquivo CSV
# df_professores = pd.read_csv(csv_path2)

# # Obter valores únicos da coluna 'semestre'
# valores_unicos_semestre = df_professores['semestre'].drop_duplicates().sort_values()

# # Exibir os valores únicos
# print("Valores únicos da coluna 'semestre':")
# print(valores_unicos_semestre.to_list())

# contagem_semestres = df_professores['semestre'].value_counts()

# # Exibir os resultados
# print("Quantidade de vezes que cada semestre aparece:")
# print(contagem_semestres)

# # Carregar o arquivo CSV
# df_curso_disciplina = pd.read_csv(csv_path3)

# # Multiplicar os valores da coluna 'duracao' por 2
# df_curso_disciplina['duracao'] = df_curso_disciplina['duracao'] * 2

# # Limitar os valores acima de 9 para 9
# df_curso_disciplina['duracao'] = df_curso_disciplina['duracao'].apply(lambda x: min(x, 9))

# # Salvar as alterações no mesmo arquivo
# df_curso_disciplina.to_csv(csv_path3, index=False)

# print("Arquivo atualizado com sucesso!")

# df_curso_disciplina = pd.read_csv(csv_path3)

# # Selecionar as colunas 'nome_curso' e 'duracao'
# dados_unicos = df_curso_disciplina[['nome_curso', 'duracao']].drop_duplicates()

# # Exibir os valores únicos
# print("Valores únicos de 'nome_curso' e 'duracao':")
# print(dados_unicos)

# import pandas as pd
# import random

# # Caminhos dos arquivos CSV
# alunos_csv_path = 'C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_alunos.csv'

# # Criar um dicionário para associar cursos e suas respectivas durações
# cursos_duracoes = {
#     "Redes de Computadores": 6,
#     "Ciência da Computação": 8,
#     "Engenharia de Software": 8,
#     "Segurança da Informação": 8,
#     "Data Science": 8,
#     "Inteligência Artificial": 8,
#     "Engenharia Elétrica": 9,
#     "Engenharia de Controle e Automação": 9,
#     "Engenharia de Produção": 8,
#     "Engenharia Mecânica": 9,
#     "Engenharia Civil": 9,
#     "Engenharia Química": 9,
#     "Medicina": 9,
#     "Enfermagem": 8,
#     "Fisioterapia": 8,
#     "Biomedicina": 8,
#     "Farmácia": 8,
#     "Odontologia": 9,
#     "Biologia": 8,
#     "Genética": 8,
#     "Microbiologia": 8,
#     "Ecologia": 8,
#     "Botânica": 8,
#     "Zoologia": 8
# }

# # Carregar o arquivo de alunos
# df_alunos = pd.read_csv(alunos_csv_path)

# # Adicionar a coluna 'semestre_atual' com valores aleatórios
# def atribuir_semestre(nome_curso):
#     if nome_curso in cursos_duracoes:
#         return random.randint(1, cursos_duracoes[nome_curso])
#     return None  # Caso o curso não esteja na lista, deixar como vazio

# df_alunos['semestre_atual'] = df_alunos['nome_curso'].apply(atribuir_semestre)

# # Salvar as alterações no mesmo arquivo
# df_alunos.to_csv(alunos_csv_path, index=False)

# print("Coluna 'semestre_atual' adicionada com sucesso!")


# media_por_departamento = df_alunos.groupby(["nome_departamento", "semestre_atual"])["media_global"].mean().reset_index()
# df_professores = df_professores.merge(media_por_departamento, on=["nome_departamento", "semestre_atual"], how="left")
# media_professores = df_professores.groupby(["nome_professor", "nome_departamento"])["media_global"].mean().reset_index()
# media_professores.rename(columns={"media_global": "media_global_professor"}, inplace=True)
# df_professores = df_professores.merge(media_professores[['nome_professor', 'media_global_professor']], on='nome_professor', how='left')
# df_professores['media_global_professor'] = df_professores['media_global_professor'].round(2)
# df_professores.to_csv("C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_professor_disciplina.csv", index=False)

# professores_multidepartamento = (
#     df_professores.groupby('nome_professor')['nome_departamento']
#     .nunique()
#     .reset_index()
# )
# professores_multidepartamento = professores_multidepartamento[
#     professores_multidepartamento['nome_departamento'] > 1
# ]

# # Filtrar os professores que não estão em múltiplos departamentos
# df_professores = df_professores[
#     ~df_professores['nome_professor'].isin(professores_multidepartamento['nome_professor'])
# ]

# # Salvar de volta no CSV original
# df_professores.to_csv('C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_professor_disciplina.csv', index=False)