import cls_client


cls_client.set_debug(True)
cls_client.set_project_slug("cls_client_example")


@cls_client.track_command()
def func():
    print("func() in example.py")


if __name__ == "__main__":
    func()
