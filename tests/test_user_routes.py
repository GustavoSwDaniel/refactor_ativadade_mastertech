def test_acessar_rota_list_user_retornar_status_200(client):
    resp = client.get("/users")
    assert resp.status_code == 200


def test_find_user_exist(client):
    resp = client.get("/user/1")
    assert resp.status_code == 200


def test_find_user_not_exist(client):
    resp = client.get("/user/1000")
    assert resp.status_code == 404


def test_new_user(new_user):
    assert new_user.name == "Gustavo Daniel"
    assert new_user.email == "gustavo@gustavo.com"
    assert new_user.cpf == "00000000000"
