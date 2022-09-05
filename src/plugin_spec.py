
import pluggy

hookspec = pluggy.HookspecMarker(project_name="datastore")

@hookspec
def my_plugin(config):
    """Print formatted output"""