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
                accounts[response.accountNumber].append(response)
            else:
                accounts[response.accountNumber] = [response]
        else:
            if response.accountNumber not in accounts:
                accounts[response.accountNumber] = None
    return accounts
