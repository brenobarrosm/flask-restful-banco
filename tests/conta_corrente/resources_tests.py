import json

def criar_conta(test_client, banco, agencia, conta):
    obj = {
        'banco': banco,
        'agencia': agencia,
        'conta': conta
    }

    response = test_client.post(
        '/contas',
        data=json.dumps(obj),
        content_type='application/json'
    )

    return response

def test_post_conta_corrente(test_client):

    response = criar_conta(test_client, '80', '1568', '78954')

    assert response.status_code == 201
    assert response.json['id'] is not None

def test_get_saldo(test_client):

    response = criar_conta(test_client, '80', '1568', '78954')

    response = test_client.get('/contas/1/saldo')

    assert response.status_code == 200
    assert response.json['valor'] == '0.00'

def test_put_credito(test_client):

    criar_conta(test_client, '80', '1568', '78954')

    response = test_client.put(
        '/contas/1/credito',
        data=json.dumps({"valor": "15.90"}),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['valor'] == '15.90'

def test_put_debito(test_client):

    criar_conta(test_client, '80', '1568', '78954')

    response = test_client.put(
        '/contas/1/debito',
        data=json.dumps({"valor": "4.99"}),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['valor'] == '4.99'