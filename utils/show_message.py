__OKGREEN__ = "\033[92m"
__FAIL__ = "\033[91m"


def showMessage(message: str, success: bool = True):
    print(
        f"\n\n{success and __OKGREEN__ or __FAIL__}{success and 'SUCCESS :: ' or 'FAILURE :: '}{message}\n"
    )