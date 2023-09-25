from fastapi import FastAPI, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware

from .database import cursor

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens (domínios)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos HTTP
)
@app.get("/contador/{carga}")
def contador(carga: str = Path(..., title="Número da Carga")):
    cursor.execute(f"""
        SELECT DISTINCT
            CONVERT(varchar, rom.Cod_filial_volume) + '-' +
            CONVERT(varchar, rom.Serie_volume) + '-' +
            CONVERT(varchar, rom.Num_volume) AS ID
        FROM
            tbSaidas s WITH(NOLOCK)
        INNER JOIN
            tbSaidasItemRom rom WITH(NOLOCK) ON s.Chave_fato = rom.Chave_fato
        -- INNER JOIN tbVolume v WITH(NOLOCK) ON rom.Num_volume = v.Num_volume AND v.Serie_volume = rom.Serie_volume
        WHERE
            s.Serie_carga = '001' AND
            s.Num_carga = '{carga}'
    """)
    
    results = cursor.fetchall()

    count = len(results)
    
    return {"count": count}
