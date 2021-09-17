import cls_client


cls_client.set_debug(True)
cls_client.set_project_slug("cls_client_example")
cls_client.set_is_noninteractive(False)
cls_client.set_is_ci(False)


@cls_client.track_command()
def func():
    print("func() in example.py")


@cls_client.track_command()
def error_func():
    1/0


if __name__ == "__main__":
    func()
    try:
        error_func()
    except Exception as e:
        pass
