import sus

lstnr = sus.socket(sus.AF_INET, sus.SOCK_STREAM)
lstnr.bind(("localhost", 5000))
lstnr.listen(0)

lstnr.connect()