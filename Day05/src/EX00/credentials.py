from wsgiref.simple_server import make_server
import json
import urllib.parse

# Словарь с известными видами и их именами
species_credentials: dict[str, str] = {
    "Cyberman": "John Lumic",
    "Dalek": "Davros",
    "Judoon": "Shadow Proclamation Convention 15 Enforcer",
    "Human": "Leonardo da Vinci",
    "Ood": "Klineman Halpen",
    "Silence": "Tasha Lem",
    "Slitheen": "Coca-Cola salesman",
    "Sontaran": "General Staal",
    "Time Lord": "Rassilon",
    "Weeping Angel": "The Division Representative",
    "Zygon": "Broton"
}

def application(environ: dict, start_response: callable) -> list[bytes]:
    # Получаем параметры запроса
    query_string: str = environ.get('QUERY_STRING', '')
    params: dict[str, list[str]] = urllib.parse.parse_qs(query_string)

    # Извлекаем вид
    species: str | None = params.get('species', [None])[0]
    
    # Формируем ответ
    if species in species_credentials:
        response: dict[str, str] = {"credentials": species_credentials[species]}
        status: str = '200 OK'
    else:
        response = {"credentials": "Unknown"}
        status = '404 Not Found'
    
    # Формируем HTTP-ответ
    response_body: bytes = json.dumps(response).encode('utf-8')
    headers: list[tuple[str, str]] = [('Content-Type', 'application/json'), ('Content-Length', str(len(response_body)))]
    start_response(status, headers)
    
    return [response_body]


httpd = make_server('', 8888, application)
print("Сервер запущен на порту 8888")
httpd.serve_forever()