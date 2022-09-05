import pluggy

hookimpl = pluggy.HookimplMarker(project_name="datastore")

@hookimpl
def print_output(config):
    """Print output"""
    print(f"This is from plugin7_pluggy {config}")
 
