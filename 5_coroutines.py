def subgen():
    message = yield
    print('Subgen received:', message)
