# CLS client library for Python

In development.

```python
import click
import cls_client


cls_client.set_project_key("cls_pk_xxxxxxxxxxxxx")
cls_client.set_project_slug("my_cli")
cls_client.set_noninteractive_tracking(
    enabled=True,
    is_noninteractive="CI" in os.environ,
)

@cli.command()
@click.option("--check", is_flag=True, default=False)
@click.option("--env", default="production")
@click.option("--var", multiple=True, default=[])
@click.pass_context
@cls_client.track_command(include_kwargs=["check", "env"], include_env=["NETLIFY"])
def build(ctx, check, env, var):
    pass
```
