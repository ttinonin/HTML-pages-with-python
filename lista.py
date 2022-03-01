#Here I'm using a dictionary with a lot of movies to make a table in the html,
#but you can make a webscrap file that cathes all the information that you want and just put it in

filmes = {
    "Ação":["Duro de Matar", "Busca Implacavel"],
    "Comédia":["Gente Grande 2", "Gente Grande"],
    "Suspense":["Uma noite de crime", "Ilha do Medo", "GTA 5"]
}

with open("FILE TO WRITE THE CODE", "w", encoding="utf-8") as f:
    f.write("""
        <!DOCTYPE html>
        <head>
        <title>Filmes</title>
        </head>
        <style>
        table, th, td{
            border: 1px solid black;
            text-align: center;
        }
        </style>
        <body>
        <h1>Lista de filmes</h1>
        <table>
        <tr>
    """)
    for c, v in filmes.items():
        f.write(f"<th>{c}</th></tr>")
        for e in v:
            f.write(f"<td>{e}</td></tr>")
    f.write("""
        </body>
        </html>
    """)