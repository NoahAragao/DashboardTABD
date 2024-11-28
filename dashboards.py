import plotly.express as px
import pandas as pd
import panel as pn

df_alunos = pd.read_csv('C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_alunos.csv')
df_curso = pd.read_csv('C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_curso_disciplina.csv')
df_professores = pd.read_csv('C:/Users/mvna2/Documents/Programacao/TrabalhoBancodeDados/tb_professor_disciplina.csv')


curso_counts = df_alunos['nome_curso'].value_counts()
status_count = df_alunos['status'].value_counts()
media_por_curso = df_alunos.groupby("nome_curso")["media_global"].mean().reset_index()
media_por_curso = media_por_curso.sort_values(by="media_global", ascending=False)
media_professores = df_professores.groupby(['nome_professor', 'nome_departamento'], as_index=False)['media_global_professor'].mean()

df_alunos_matriculados = df_alunos[df_alunos['status'] == 'Matriculado']
alunos_por_semestre = df_alunos_matriculados.groupby('semestre_atual').size().reset_index(name='quantidade_alunos_matriculados')

df_alunos_inativos = df_alunos[df_alunos['status'] == 'Inativo']
alunos_inativos_por_semestre = df_alunos_inativos.groupby('semestre_atual').size().reset_index(name='quantidade_alunos_inativos')

alunos_inativos = df_alunos[df_alunos['status'] == 'Inativo']

total_alunos_por_curso = df_alunos.groupby('nome_curso').size().reset_index(name='total_alunos')
inativos_por_curso = alunos_inativos.groupby('nome_curso').size().reset_index(name='alunos_inativos')
taxa_evasao = pd.merge(total_alunos_por_curso, inativos_por_curso, on='nome_curso', how='left')
taxa_evasao['alunos_inativos'] = taxa_evasao['alunos_inativos'].fillna(0) 
taxa_evasao['taxa_evasao'] = (taxa_evasao['alunos_inativos'] / taxa_evasao['total_alunos']) * 100
top5_cursos_evasao = taxa_evasao.nlargest(5, 'taxa_evasao')


fig = px.pie(
    names=curso_counts.index,  
    values=curso_counts.values,  
    title="Cursos Mais Populares")


fig2 = px.pie(
    names=status_count.index,
    values = status_count.values,
    title="Comparação entre Quantidade de Alunos Matriculados"
)

fig3 = px.bar(
    media_por_curso,
    x="nome_curso",
    y="media_global",
    color="nome_curso",
    title="Cursos com Maiores Medias",
    labels={"media_global": "Media Global", "nome_curso": "Cursos"},
)

fig3.update_layout(
    xaxis_title="Cursos",
    yaxis_title="Média Global",
    yaxis=dict(range=[7.9, 8.1]),
    showlegend=False, 
    width=450,
)

fig4 = px.bar(
    media_professores,
    x='nome_professor',
    y='media_global_professor',
    title="Média Global dos Professores",
    color='nome_departamento',
    hover_data=['nome_departamento'],
)

fig4.update_layout(
    xaxis=dict(
        title="Nome do Professor",
        tickangle=-45,
        showticklabels=True,
        rangeslider=dict(visible=True),
        range=[0, 100]
    ),
    yaxis=dict(
        title="Média Global do Professor",
        range=[7.8, 8.2],
    ),
    dragmode="zoom",
    height=600,
    width=1000,
    showlegend=True
)

fig5 = px.line(
    alunos_por_semestre,
    x='semestre_atual',
    y='quantidade_alunos_matriculados',
    title="Quantidade de Alunos Matriculados por Semestre",
    markers=True
)

fig5.update_traces(line_color='red')

fig5.update_layout(
    xaxis_title="Semestre Atual",
    yaxis_title="Quantidade de Alunos Matriculados",
    height=600,
    width=700
)

fig6 = px.line(
    alunos_inativos_por_semestre,
    x='semestre_atual',
    y='quantidade_alunos_inativos',
    title="Quantidade de Alunos Inativos por Semestre",
    markers=True
)

fig6.update_layout(
    xaxis_title="Semestre Atual",
    yaxis_title="Quantidade de Alunos Inativos",
    height=600,
    width=700
)

fig7 = px.bar(
    top5_cursos_evasao,
    x='nome_curso',
    y='taxa_evasao',
    title="5 Cursos com a Maior Taxa de Evasão",
)

fig7.update_layout(
    yaxis=dict(
        range=[56, 59],
    ),
)

fig8 = px.pie(
    df_alunos, 
    names='tipo_desconto', 
    title='Tipos de Desconto dos Alunos', 
)


pn.extension()
fig = pn.pane.Plotly(fig)
fig2 = pn.pane.Plotly(fig2)
fig3 = pn.pane.Plotly(fig3)
fig4 = pn.pane.Plotly(fig4)
fig5 = pn.pane.Plotly(fig5)
fig6 = pn.pane.Plotly(fig6)
fig7 = pn.pane.Plotly(fig7)
fig8 = pn.pane.Plotly(fig8)

dashboard = pn.Column(
    "Dashboard Geral Universidade",
    pn.Row(
        fig,
        fig2,
        align="center"
    ),pn.Row(
        fig3,
        fig4,
        align="center"
    ), pn.Row(
        fig5,
        fig6,
        align="center"
    ), pn.Row(
        fig7,
        fig8,
        align="center"
    ),
)

dashboard.servable()

if __name__ == "__main__":
    dashboard.show()


