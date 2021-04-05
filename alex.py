class Response:
    def __init__(self, accountNumber, provider, isValid):
        self.accountNumber = accountNumber
        self.provider = provider
        self.isValid = isValid


def group_by_account(responses):
    accounts = dict()
    for response in responses:
        if response.isValid:
            if response.accountNumber in accounts:
                accounts[response.accountNumber] = (accounts[response.accountNumber]).append(response)
            else:
                accounts[response.accountNumber] = [response]
        else:
            if response.accountNumber not in accounts:
                accounts[response.accountNumber] = None
    return accounts


if __name__ == '__main__':
    response1 = Response('123', 'Amazon', True)
    response2 = Response('456', 'Google', True)
    response3 = Response('789', 'Tesla', False)
    response4 = Response('123', 'Amazon', True)

    responses = [response1, response2, response3, response4]

    print(group_by_account(responses))
